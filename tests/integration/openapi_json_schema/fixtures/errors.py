from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class OpenAPIValidationErrorFixture:
    code: str
    location: str
    message: str
    expected_facade_path: str | None
    source: str


OPENAPI_SCHEMA_REFERENCES: tuple[tuple[str, str], ...] = (
    (
        "OpenAPI Specification 3.1.0",
        "https://spec.openapis.org/oas/v3.1.0",
    ),
    (
        "JSON Schema Validation Draft 2020-12",
        "https://json-schema.org/draft/2020-12/json-schema-validation",
    ),
)


OPENAPI_ERROR_FIXTURES: tuple[OpenAPIValidationErrorFixture, ...] = (
    OpenAPIValidationErrorFixture(
        code="request.format",
        location="/ingress[1]/validation[1]/request[1]/body[1]/customer[1]/email[1]",
        message="'foo-at-example.com' is not a 'email'",
        expected_facade_path="api_validation/request/body/customer/email",
        source="https://json-schema.org/draft/2020-12/json-schema-validation",
    ),
    OpenAPIValidationErrorFixture(
        code="request.minimum",
        location="/ingress[1]/validation[1]/request[1]/body[1]/items[2]/qty[1]",
        message="-1 is less than the minimum of 1",
        expected_facade_path="api_validation/request/body/items[1]/quantity",
        source="https://json-schema.org/draft/2020-12/json-schema-validation",
    ),
    OpenAPIValidationErrorFixture(
        code="request.pattern",
        location="/ingress[1]/validation[1]/request[1]/body[1]/items[3]/sku[1]",
        message="'abc-12' does not match '^[A-Z0-9-]+$'",
        expected_facade_path="api_validation/request/body/items[2]/sku",
        source="https://json-schema.org/draft/2020-12/json-schema-validation",
    ),
    OpenAPIValidationErrorFixture(
        code="response.enum",
        location="/gateway[1]/validation[1]/response[1]/body[1]/status[1]",
        message="'PENDING_APPROVAL' is not one of ['accepted', 'rejected']",
        expected_facade_path="api_validation/response/body/status",
        source="https://spec.openapis.org/oas/v3.1.0",
    ),
    OpenAPIValidationErrorFixture(
        code="response.type",
        location=(
            "/gateway[1]/validation[1]/response[1]/body[1]/data[1]/"
            "lines[2]/totalAmount[1]"
        ),
        message="'12.5x' is not of type 'string' with numeric-money format",
        expected_facade_path="api_validation/response/body/data/lines[1]/total_amount",
        source="https://spec.openapis.org/oas/v3.1.0",
    ),
    OpenAPIValidationErrorFixture(
        code="response.unmapped",
        location="/validation[1]/response[1]/headers[1]/x-request-id[1]",
        message="Header x-request-id does not satisfy the schema",
        expected_facade_path=None,
        source="https://spec.openapis.org/oas/v3.1.0",
    ),
)
