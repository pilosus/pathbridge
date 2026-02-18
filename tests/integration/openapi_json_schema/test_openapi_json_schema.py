from __future__ import annotations

import pytest

from pathbridge import compile_rules, to_marshmallow, translate_location
from pathbridge.extras import build_rules, make_shape
from pathbridge.types import CompiledRulesT, RawRulesMapT
from tests.integration.openapi_json_schema.converter.order_api_converter import (
    to_order_api_validation_document,
)
from tests.integration.openapi_json_schema.destination import (
    order_api_document as destination,
)
from tests.integration.openapi_json_schema.facade import order_api_facade as facade
from tests.integration.openapi_json_schema.fixtures.errors import (
    OPENAPI_ERROR_FIXTURES,
    OpenAPIValidationErrorFixture,
)

TRACE_LIFT_FUNCTIONS = ("_normalize_email",)


@pytest.fixture(scope="module")
def openapi_rules() -> RawRulesMapT:
    shape = make_shape(facade.ApiValidationFacade, list_len=5)
    return build_rules(
        destination_module=destination,
        facade_to_destination=to_order_api_validation_document,
        facade_shape=shape,
        lift_functions=TRACE_LIFT_FUNCTIONS,
        facade_root_tag="api_validation",
    )


@pytest.fixture(scope="module")
def openapi_compiled_rules(openapi_rules: RawRulesMapT) -> CompiledRulesT:
    return compile_rules(openapi_rules)


def test_build_rules_contains_expected_openapi_paths(
    openapi_rules: RawRulesMapT,
) -> None:
    assert (
        openapi_rules["validation[1]/request[1]/body[1]/orderId[1]"]
        == "api_validation/request/body/order_id"
    )
    assert (
        openapi_rules["validation[1]/request[1]/body[1]/customer[1]/email[1]"]
        == "api_validation/request/body/customer/email"
    )
    assert (
        openapi_rules["validation[1]/request[1]/body[1]/items[1]/qty[1]"]
        == "api_validation/request/body/items[0]/quantity"
    )
    assert (
        openapi_rules["validation[1]/response[1]/body[1]/status[1]"]
        == "api_validation/response/body/status"
    )
    assert (
        openapi_rules[
            "validation[1]/response[1]/body[1]/data[1]/lines[1]/totalAmount[1]"
        ]
        == "api_validation/response/body/data/lines[0]/total_amount"
    )


@pytest.mark.parametrize(
    ("error",),
    [(item,) for item in OPENAPI_ERROR_FIXTURES],
    ids=lambda item: item.code,
)
def test_translate_location_maps_openapi_request_response_errors(
    openapi_compiled_rules: CompiledRulesT,
    error: OpenAPIValidationErrorFixture,
) -> None:
    assert translate_location(error.location, openapi_compiled_rules) == (
        error.expected_facade_path
    )


def test_to_marshmallow_folds_openapi_request_and_response_errors(
    openapi_compiled_rules: CompiledRulesT,
) -> None:
    used = OPENAPI_ERROR_FIXTURES[0:5]
    errors = [(item.location, item.message) for item in used]
    result = to_marshmallow(errors, openapi_compiled_rules)

    assert result == {
        "api_validation": {
            "request": {
                "body": {
                    "customer": {"email": [OPENAPI_ERROR_FIXTURES[0].message]},
                    "items": {
                        1: {"quantity": [OPENAPI_ERROR_FIXTURES[1].message]},
                        2: {"sku": [OPENAPI_ERROR_FIXTURES[2].message]},
                    },
                },
            },
            "response": {
                "body": {
                    "status": [OPENAPI_ERROR_FIXTURES[3].message],
                    "data": {
                        "lines": {
                            1: {"total_amount": [OPENAPI_ERROR_FIXTURES[4].message]}
                        }
                    },
                },
            },
        }
    }


def test_to_marshmallow_reports_unmatched_openapi_locations_in_meta(
    openapi_compiled_rules: CompiledRulesT,
) -> None:
    # Index 8 is outside generated list_len=5 shape and should not match.
    out_of_shape = (
        "/ingress[1]/validation[1]/request[1]/body[1]/items[8]/qty[1]",
        "99 is greater than the maximum of 50",
    )
    unmapped = OPENAPI_ERROR_FIXTURES[5]
    result = to_marshmallow(
        [out_of_shape, (unmapped.location, unmapped.message)],
        openapi_compiled_rules,
        include_meta=True,
    )

    assert result == {
        "_meta": {
            "total": 2,
            "matched": 0,
            "missed": 2,
            "misses": [
                {
                    "location": out_of_shape[0],
                    "message": out_of_shape[1],
                },
                {
                    "location": unmapped.location,
                    "message": unmapped.message,
                },
            ],
        }
    }
