from typing import Any

import pytest

from pathbridge.adapter import to_marshmallow
from pathbridge.compiler import compile_rules
from pathbridge.types import ErrorItemT, RawRulesMapT


@pytest.fixture()
def compiled(xpath_rules: RawRulesMapT):
    return compile_rules(xpath_rules)


@pytest.mark.parametrize(
    "location,message,expected",
    [
        (
            "/GovTalkMessage/Body/IRenvelope/IRbody/SA100/YourName/FirstName",
            "Missing element",
            {"taxpayer": {"name": {"first": ["Missing element"]}}},
        ),
        (
            "/GovTalkMessage/Body/IRenvelope/IRbody/SA100/YourName/Surname",
            "Invalid value",
            {"taxpayer": {"name": {"last": ["Invalid value"]}}},
        ),
        (
            "/GovTalkMessage/Body/IRenvelope/IRbody/SA100/Income/Interest[1]/Amount",
            "Must be a number",
            {"income": {"interest": {"[i]": {"amount": ["Must be a number"]}}}},
        ),
        (
            "/GovTalkMessage/Body/IRenvelope/IRbody/SA103S/SelfEmployment[2]/Turnover",
            "Too large",
            {"self_employment": {"[i]": {"turnover": ["Too large"]}}},
        ),
        (
            "/GovTalkMessage/Body/IRenvelope/IRbody/SA103S/SelfEmployment[2]/Expenses/Total",
            "Too small",
            {"self_employment": {"[i]": {"expenses": {"total": ["Too small"]}}}},
        ),
    ],
)
def test_to_marshmallow_adapter_maps_xpath_locations(
    compiled,
    location: str,
    message: str,
    expected: dict[str, Any],
) -> None:
    errors: list[ErrorItemT] = [(location, message)]
    result = to_marshmallow(errors, compiled)

    assert result == expected


def test_to_marshmallow_adapter_ignores_unmatched_locations(compiled) -> None:
    errors: list[ErrorItemT] = [
        ("/GovTalkMessage/Body/IRenvelope/IRbody/SA100/SomeOtherNode", "Whatever"),
    ]
    out = to_marshmallow(errors, compiled)
    assert out == {}


def test_to_marshmallow_adapter_ignores_unmatched_locations_calculates_meta(
    compiled,
) -> None:
    errors: list[ErrorItemT] = [
        ("/GovTalkMessage/Body/IRenvelope/IRbody/SA100/SomeOtherNode", "Whatever"),
    ]
    out = to_marshmallow(errors, compiled, include_meta=True)
    expected = {
        "_meta": {
            "matched": 0,
            "total": 1,
            "missed": 1,
            "misses": [
                {
                    "location": "/GovTalkMessage/Body/IRenvelope/IRbody/SA100/SomeOtherNode",
                    "message": "Whatever",
                }
            ],
        }
    }
    assert out == expected


def test_to_marshmallow_adapter_more_specific_predicate_wins(
    xpath_rules: RawRulesMapT,
) -> None:
    """
    Key[@Type='UTR'] should map to /taxpayer/utr, not the generic /taxpayer/key.
    """
    compiled = compile_rules(xpath_rules)

    errors: list[ErrorItemT] = [
        ("/GovTalkMessage/Body/IRenvelope/IRheader/Keys/Key[@Type='UTR']", "Bad UTR"),
    ]
    out = to_marshmallow(errors, compiled)
    assert out == {"taxpayer": {"utr": ["Bad UTR"]}}


def test_to_marshmallow_adapter_does_not_mutate_input(compiled) -> None:
    errors: list[ErrorItemT] = [
        (
            "/GovTalkMessage/Body/IRenvelope/IRbody/SA100/YourName/FirstName",
            "Missing element",
        ),
    ]
    before = list(errors)
    _ = to_marshmallow(errors, compiled)
    assert errors == before
