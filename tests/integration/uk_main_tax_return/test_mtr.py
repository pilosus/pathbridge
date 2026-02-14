from dataclasses import dataclass

import pytest

pytest.importorskip("xsdata.models.datatype")

from pathbridge import compile_rules, to_marshmallow, translate_location
from pathbridge.extras import build_rules, make_shape
from pathbridge.types import CompiledRulesT, RawRulesMapT
from tests.integration.uk_main_tax_return.converter.mtr_converter import to_mtr_v1_1
from tests.integration.uk_main_tax_return.destination import mtr_v1_1 as destination
from tests.integration.uk_main_tax_return.facade import mtr_facade as facade

TRACE_LIFT_FUNCTIONS = (
    "_yes",
    "_yes_no",
    "_tax_payer_status",
    "_student_loan_plan",
    "_postgraduate_loan_plan",
    "_attachment_file_format",
    "decimal_str_or_none",
    "xml_date_or_none",
    "decode_attachment",
)


@dataclass
class HMRCXPathError:
    code: int
    location: str
    message: str


ERROR_SA110_TOTAL_TAX_DUE_DECIMAL = HMRCXPathError(
    code=6492,
    location="/hd:GovTalkMessage[1]/hd:Body[1]/MTR:IRenvelope[1]/MTR:MTR[1]/MTR:SA110[1]/MTR:SelfAssessment[1]/MTR:TotalTaxEtcDue[1]",
    message="Self calculation case. The total tax due in box [CAL1] does not agree with the calculated value of £2,000.00. The difference is -£6,000.00. Please check.",
)


ERROR_SA103S_BUSINESS_DETAILS_DESCRIPTION_STR = HMRCXPathError(
    code=4065,
    location="/hd:GovTalkMessage[1]/hd:Body[1]/MTR:IRenvelope[1]/MTR:MTR[1]/MTR:SA103S[1]/MTR:BusinessDetails[1]/MTR:BusinessDescription[1]",
    message="Invalid content found at element 'BusinessDescription'",
)

ERROR_SA100_BLIND_PERSONS_ALLOWANCE_DEEPLY_NESTED = HMRCXPathError(
    code=4065,
    location="/hd:GovTalkMessage[1]/hd:Body[1]/MTR:IRenvelope[1]/MTR:MTR[1]/MTR:SA100[1]/MTR:TaxReliefs[1]/MTR:BlindPersonsAllowance[1]/MTR:BlindPersonsAllowanceDetails[1]/MTR:LocalAuthorityName[1]",
    message="Invalid content found at element 'LocalAuthorityName'",
)

# ProfitsLossesNICsAndCIS is an object, not a list, so the location
# cannot exist, cannot be shaped by shaper, and cannot be translated
ERROR_SA103S_PNL_LIST_IN_LIST_PATH_DOES_NOT_EXIST = HMRCXPathError(
    code=6183,
    location="/hd:GovTalkMessage[1]/hd:Body[1]/MTR:IRenvelope[1]/MTR:MTR[1]/MTR:SA103S[7]/MTR:ProfitsLossesNICsAndCIS[8]/MTR:NetBusinessLossForTax[2]",
    message="The amount in box [SSE32] must equal [SSE23] plus [SSE24] plus [SSE24.1] plus  [SSE25] plus [SSE25.1] plus [SSE25.2] minus ([SSE21/SSE22] plus [SSE26] plus [SSE27]) if positive or zero. Please check.",
)


@pytest.fixture(scope="module")
def mtr_rules() -> RawRulesMapT:
    shape = make_shape(facade.MTR, list_len=10)
    return build_rules(
        model_module=destination,
        converter=to_mtr_v1_1,
        shape=shape,
        lift=TRACE_LIFT_FUNCTIONS,
        root_tag="mtr",
        destination_prefix="MTR",
    )


@pytest.fixture(scope="module")
def mtr_compiled_rules(mtr_rules: RawRulesMapT) -> CompiledRulesT:
    return compile_rules(mtr_rules)


def test_build_rules_contains_expected_real_world_paths(
    mtr_rules: RawRulesMapT,
) -> None:
    assert (
        mtr_rules["MTR:MTR[1]/MTR:Sa110[1]/MTR:SelfAssessment[1]/MTR:TotalTaxEtcDue[1]"]
        == "mtr/sa110/self_assessment/total_tax_etc_due"
    )
    assert (
        mtr_rules[
            "MTR:MTR[1]/MTR:Sa103S[1]/MTR:BusinessDetails[1]/MTR:BusinessDescription[1]"
        ]
        == "mtr/sa103s[0]/business_details/business_description"
    )
    assert (
        mtr_rules[
            "MTR:MTR[1]/MTR:Sa100[1]/MTR:TaxReliefs[1]/MTR:BlindPersonsAllowance[1]/MTR:BlindPersonsAllowanceDetails[1]/MTR:LocalAuthorityName[1]"
        ]
        == "mtr/sa100/tax_reliefs/blind_persons_allowance/blind_persons_allowance_details/local_authority_name"
    )
    assert (
        mtr_rules["MTR:MTR[1]/MTR:Sa103S[1]/MTR:BusinessDetails[1]"]
        == "mtr/sa103s[0]/business_details"
    )


@pytest.mark.parametrize(
    ("error", "expected_path"),
    [
        (
            ERROR_SA110_TOTAL_TAX_DUE_DECIMAL,
            "mtr/sa110/self_assessment/total_tax_etc_due",
        ),
        (
            ERROR_SA103S_BUSINESS_DETAILS_DESCRIPTION_STR,
            "mtr/sa103s[0]/business_details/business_description",
        ),
        (
            ERROR_SA100_BLIND_PERSONS_ALLOWANCE_DEEPLY_NESTED,
            "mtr/sa100/tax_reliefs/blind_persons_allowance/blind_persons_allowance_details/local_authority_name",
        ),
    ],
)
def test_translate_location_maps_known_hmrc_errors(
    mtr_compiled_rules: CompiledRulesT,
    error: HMRCXPathError,
    expected_path: str,
) -> None:
    assert translate_location(error.location, mtr_compiled_rules) == expected_path


def test_translate_location_maps_high_sa103s_index_when_nested_indices_match(
    mtr_compiled_rules: CompiledRulesT,
) -> None:
    location = "/hd:GovTalkMessage[1]/hd:Body[1]/MTR:IRenvelope[1]/MTR:MTR[1]/MTR:SA103S[7]/MTR:ProfitsLossesNICsAndCIS[1]/MTR:NetBusinessLossForTax[1]"
    assert (
        translate_location(location, mtr_compiled_rules)
        == "mtr/sa103s[6]/profits_losses_nics_and_cis/net_business_loss_for_tax"
    )


def test_to_marshmallow_folds_real_world_errors(
    mtr_compiled_rules: CompiledRulesT,
) -> None:
    errors = [
        (
            ERROR_SA110_TOTAL_TAX_DUE_DECIMAL.location,
            ERROR_SA110_TOTAL_TAX_DUE_DECIMAL.message,
        ),
        (
            ERROR_SA103S_BUSINESS_DETAILS_DESCRIPTION_STR.location,
            ERROR_SA103S_BUSINESS_DETAILS_DESCRIPTION_STR.message,
        ),
        (
            ERROR_SA100_BLIND_PERSONS_ALLOWANCE_DEEPLY_NESTED.location,
            ERROR_SA100_BLIND_PERSONS_ALLOWANCE_DEEPLY_NESTED.message,
        ),
    ]
    result = to_marshmallow(errors, mtr_compiled_rules)

    assert result == {
        "mtr": {
            "sa110": {
                "self_assessment": {
                    "total_tax_etc_due": [ERROR_SA110_TOTAL_TAX_DUE_DECIMAL.message]
                }
            },
            "sa103s": {
                0: {
                    "business_details": {
                        "business_description": [
                            ERROR_SA103S_BUSINESS_DETAILS_DESCRIPTION_STR.message
                        ]
                    }
                }
            },
            "sa100": {
                "tax_reliefs": {
                    "blind_persons_allowance": {
                        "blind_persons_allowance_details": {
                            "local_authority_name": [
                                ERROR_SA100_BLIND_PERSONS_ALLOWANCE_DEEPLY_NESTED.message
                            ]
                        }
                    }
                }
            },
        }
    }


def test_to_marshmallow_reports_unmatched_real_world_error_in_meta(
    mtr_compiled_rules: CompiledRulesT,
) -> None:
    result = to_marshmallow(
        [
            (
                ERROR_SA103S_PNL_LIST_IN_LIST_PATH_DOES_NOT_EXIST.location,
                ERROR_SA103S_PNL_LIST_IN_LIST_PATH_DOES_NOT_EXIST.message,
            )
        ],
        mtr_compiled_rules,
        include_meta=True,
    )

    assert (
        translate_location(ERROR_SA103S_PNL_LIST_IN_LIST_PATH_DOES_NOT_EXIST.location, mtr_compiled_rules)
        is None
    )
    assert result == {
        "_meta": {
            "total": 1,
            "matched": 0,
            "missed": 1,
            "misses": [
                {
                    "location": ERROR_SA103S_PNL_LIST_IN_LIST_PATH_DOES_NOT_EXIST.location,
                    "message": ERROR_SA103S_PNL_LIST_IN_LIST_PATH_DOES_NOT_EXIST.message,
                }
            ],
        }
    }
