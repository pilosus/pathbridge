from __future__ import annotations

import pytest

from pathbridge import compile_rules, to_marshmallow, translate_location
from pathbridge.extras import build_rules, make_shape
from pathbridge.types import CompiledRulesT, RawRulesMapT
from tests.integration.iso20022_payments.converter.pain_001_converter import (
    to_pain_001_001_09,
)
from tests.integration.iso20022_payments.destination import pain_001_001_09
from tests.integration.iso20022_payments.facade import payment_facade
from tests.integration.iso20022_payments.fixtures.errors import (
    BUSINESS_REJECTION_FIXTURES,
    XSD_ERROR_FIXTURES,
    ISO20022ErrorFixture,
)

TRACE_LIFT_FUNCTIONS = ("_normalize_country_code", "_normalize_iban")


@pytest.fixture(scope="module")
def iso_rules() -> RawRulesMapT:
    shape = make_shape(payment_facade.PaymentInitiationRequest, list_len=5)
    return build_rules(
        destination_module=pain_001_001_09,
        facade_to_destination=to_pain_001_001_09,
        facade_shape=shape,
        lift_functions=TRACE_LIFT_FUNCTIONS,
        facade_root_tag="payment_request",
    )


@pytest.fixture(scope="module")
def iso_compiled_rules(iso_rules: RawRulesMapT) -> CompiledRulesT:
    return compile_rules(iso_rules)


def test_build_rules_contains_expected_iso20022_paths(iso_rules: RawRulesMapT) -> None:
    assert (
        iso_rules["Document[1]/CstmrCdtTrfInitn[1]/GrpHdr[1]/MsgId[1]"]
        == "payment_request/customer_credit_transfer_initiation/message_id"
    )
    assert (
        iso_rules["Document[1]/CstmrCdtTrfInitn[1]/PmtInf[1]/ReqdExctnDt[1]"]
        == "payment_request/customer_credit_transfer_initiation/payment_infos[0]/requested_execution_date"
    )
    assert (
        iso_rules[
            "Document[1]/CstmrCdtTrfInitn[1]/PmtInf[1]/CdtTrfTxInf[1]/Amt[1]/InstdAmt[1]"
        ]
        == "payment_request/customer_credit_transfer_initiation/payment_infos[0]/credit_transfers[0]/amount"
    )
    assert (
        iso_rules[
            "Document[1]/CstmrCdtTrfInitn[1]/PmtInf[1]/CdtTrfTxInf[1]/CdtrAcct[1]/Id[1]/IBAN[1]"
        ]
        == "payment_request/customer_credit_transfer_initiation/payment_infos[0]/credit_transfers[0]/creditor/iban"
    )
    assert (
        iso_rules[
            "Document[1]/CstmrCdtTrfInitn[1]/PmtInf[1]/CdtTrfTxInf[1]/Cdtr[1]/PstlAdr[1]/Ctry[1]"
        ]
        == "payment_request/customer_credit_transfer_initiation/payment_infos[0]/credit_transfers[0]/creditor/postal_address/country"
    )


@pytest.mark.parametrize(
    ("error",),
    [(item,) for item in (*XSD_ERROR_FIXTURES, *BUSINESS_REJECTION_FIXTURES)],
    ids=lambda item: item.code,
)
def test_translate_location_maps_real_world_iso20022_errors(
    iso_compiled_rules: CompiledRulesT,
    error: ISO20022ErrorFixture,
) -> None:
    assert translate_location(error.location, iso_compiled_rules) == (
        error.expected_facade_path
    )


def test_to_marshmallow_folds_mixed_iso20022_errors(
    iso_compiled_rules: CompiledRulesT,
) -> None:
    used = (
        XSD_ERROR_FIXTURES[0],
        XSD_ERROR_FIXTURES[1],
        XSD_ERROR_FIXTURES[2],
        XSD_ERROR_FIXTURES[3],
        BUSINESS_REJECTION_FIXTURES[1],
        BUSINESS_REJECTION_FIXTURES[2],
    )
    errors = [(item.location, item.message) for item in used]
    result = to_marshmallow(errors, iso_compiled_rules)

    assert result == {
        "payment_request": {
            "customer_credit_transfer_initiation": {
                "payment_infos": {
                    0: {
                        "requested_execution_date": [XSD_ERROR_FIXTURES[0].message],
                        "credit_transfers": {
                            0: {"end_to_end_id": [XSD_ERROR_FIXTURES[1].message]},
                            1: {"amount": [XSD_ERROR_FIXTURES[2].message]},
                        },
                    },
                    1: {
                        "credit_transfers": {
                            0: {
                                "creditor": {
                                    "postal_address": {
                                        "country": [XSD_ERROR_FIXTURES[3].message]
                                    }
                                }
                            },
                            2: {
                                "creditor": {
                                    "iban": [BUSINESS_REJECTION_FIXTURES[1].message]
                                }
                            },
                        }
                    },
                    2: {"debtor_name": [BUSINESS_REJECTION_FIXTURES[2].message]},
                }
            }
        }
    }


def test_to_marshmallow_reports_unmatched_iso20022_errors_in_meta(
    iso_compiled_rules: CompiledRulesT,
) -> None:
    used = (XSD_ERROR_FIXTURES[4], BUSINESS_REJECTION_FIXTURES[3])
    errors = [(item.location, item.message) for item in used]
    result = to_marshmallow(errors, iso_compiled_rules, include_meta=True)

    assert result == {
        "_meta": {
            "total": 2,
            "matched": 0,
            "missed": 2,
            "misses": [
                {
                    "location": XSD_ERROR_FIXTURES[4].location,
                    "message": XSD_ERROR_FIXTURES[4].message,
                },
                {
                    "location": BUSINESS_REJECTION_FIXTURES[3].location,
                    "message": BUSINESS_REJECTION_FIXTURES[3].message,
                },
            ],
        }
    }
