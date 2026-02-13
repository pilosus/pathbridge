from pathbridge import compile_rules, translate_location


def test_translate_location_distinguishes_explicit_indices() -> None:
    rules = {
        "Return[1]/Contact[1]/Phone[1]": "person/phones[0]",
        "Return[1]/Contact[1]/Phone[2]": "person/phones[1]",
    }
    compiled = compile_rules(rules)
    assert translate_location("/Return[1]/Contact[1]/Phone[1]", compiled) == (
        "person/phones[0]"
    )
    assert translate_location("/Return[1]/Contact[1]/Phone[2]", compiled) == (
        "person/phones[1]"
    )
