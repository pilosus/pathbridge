import re

from pathbridge.compiler import compile_rules
from pathbridge.types import RawRulesMapT


def test_compile_rules_accepts_xpath_like_keys(xpath_rules: RawRulesMapT) -> None:
    compiled = compile_rules(xpath_rules)

    assert isinstance(compiled, list)
    assert compiled

    for pattern, facade in compiled:
        assert isinstance(pattern, re.Pattern)
        assert isinstance(facade, str)
        assert facade.startswith("/")


def test_compile_rules_escapes_xpath_metacharacters(xpath_rules: RawRulesMapT) -> None:
    compiled = compile_rules(xpath_rules)

    pred_key = "/GovTalkMessage/Body/IRenvelope/IRheader/Keys/Key[@Type='UTR']"
    pred_rule = next((p for p in compiled if p[1] == "/taxpayer/utr"), None)
    assert pred_rule is not None

    pattern, _facade = pred_rule
    # It must match the exact destination location
    assert pattern.search(pred_key)


def test_compile_rules_handles_index_wildcard(xpath_rules: RawRulesMapT) -> None:
    """
    Wildcard in rules should match indexed occurrences like [...][1], [...][2], etc.
    """
    compiled = compile_rules(xpath_rules)

    # This destination should be matched by the SelfEmployment[*]/Turnover rule
    destination = (
        "/GovTalkMessage/Body/IRenvelope/IRbody/SA103S/SelfEmployment[2]/Turnover"
    )

    # Find the compiled rule whose facade is turnover
    rule = next((p for p in compiled if p[1] == "/self_employment/[i]/turnover"), None)
    assert rule is not None

    pattern, _facade = rule
    assert pattern.search(destination)


def test_compile_rules_is_deterministic(xpath_rules: RawRulesMapT) -> None:
    c_1 = compile_rules(xpath_rules)
    c_2 = compile_rules(xpath_rules)

    norm_1 = [(p.pattern, f) for p, f in c_1]
    norm_2 = [(p.pattern, f) for p, f in c_2]
    assert norm_1 == norm_2


def test_compile_rules_matches_expected_compiled_rules(
    xpath_rules: RawRulesMapT,
) -> None:
    """
    Compiled patterns are flexible:
    - ^.*? prefix allows arbitrary leading content
    - (?:[A-Za-z][\\w.-]*:)? allows optional namespace prefixes
    - (?:\\[\\d+\\])? allows optional indices on segments without explicit index
    - (?P<iN>\\d+) captures indices from wildcard [*] segments
    """
    compiled = compile_rules(xpath_rules)
    actual = [(pattern.pattern, facade) for pattern, facade in compiled]

    # Helper for building expected patterns
    ns = r"(?:[A-Za-z][\w.-]*:)?"  # optional namespace prefix
    opt_idx = r"(?:\[\d+\])?"  # optional index
    cap_idx = r"\[(?P<i0>\d+)\]"  # captured index

    prefix = (
        rf"^.*?/{ns}GovTalkMessage{opt_idx}/{ns}Body{opt_idx}/{ns}IRenvelope{opt_idx}"
    )

    expected = [
        (
            rf"{prefix}/{ns}IRbody{opt_idx}/{ns}SA100{opt_idx}/{ns}YourName{opt_idx}/{ns}FirstName{opt_idx}$",
            "/taxpayer/name/first",
        ),
        (
            rf"{prefix}/{ns}IRbody{opt_idx}/{ns}SA100{opt_idx}/{ns}YourName{opt_idx}/{ns}Surname{opt_idx}$",
            "/taxpayer/name/last",
        ),
        (
            rf"{prefix}/{ns}IRheader{opt_idx}/{ns}Keys{opt_idx}/{ns}Key\[@Type='UTR'\]$",
            "/taxpayer/utr",
        ),
        (
            rf"{prefix}/{ns}IRheader{opt_idx}/{ns}Keys{opt_idx}/{ns}Key{opt_idx}$",
            "/taxpayer/key",
        ),
        (
            rf"{prefix}/{ns}IRbody{opt_idx}/{ns}SA103S{opt_idx}/{ns}SelfEmployment{cap_idx}/{ns}BusinessName{opt_idx}$",
            "/self_employment/[i]/business_name",
        ),
        (
            rf"{prefix}/{ns}IRbody{opt_idx}/{ns}SA103S{opt_idx}/{ns}SelfEmployment{cap_idx}/{ns}Turnover{opt_idx}$",
            "/self_employment/[i]/turnover",
        ),
        (
            rf"{prefix}/{ns}IRbody{opt_idx}/{ns}SA103S{opt_idx}/{ns}SelfEmployment{cap_idx}/{ns}Expenses{opt_idx}/{ns}Total{opt_idx}$",
            "/self_employment/[i]/expenses/total",
        ),
        (
            rf"{prefix}/{ns}IRbody{opt_idx}/{ns}SA100{opt_idx}/{ns}Income{opt_idx}/{ns}Interest{cap_idx}/{ns}Amount{opt_idx}$",
            "/income/interest/[i]/amount",
        ),
    ]

    assert actual == expected
