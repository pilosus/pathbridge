# Real-life Examples

PathBridge includes multiple end-to-end integration examples you can reuse as
templates for your own validators and converters.

## HMRC Main Tax Return (XSD/XPath)

- Code: [tests/integration/hmrc_main_tax_return](https://github.com/pilosus/pathbridge/tree/main/tests/integration/hmrc_main_tax_return)
- Validator shape: XML/XSD with deep XPath error locations
- Highlights:
  - generated destination dataclasses from HMRC schema (`xsdata`)
  - hand-written facade dataclasses and converter
  - translation of HMRC-style locations to facade paths and Marshmallow errors

Run:

```bash
uv run pytest -vvs tests/integration/hmrc_main_tax_return/test_mtr.py
```

## OpenAPI JSON Schema (Request/Response)

- Code: [tests/integration/openapi_json_schema](https://github.com/pilosus/pathbridge/tree/main/tests/integration/openapi_json_schema)
- Validator shape: OpenAPI request/response JSON schema validation errors
- Highlights:
  - request and response validation in one integration flow
  - fixtures for realistic JSON schema violations (format, enum, minimum, pattern)
  - `_meta` misses coverage for unmapped/out-of-shape locations

Run:

```bash
uv run pytest -vvs tests/integration/openapi_json_schema/test_openapi_json_schema.py
```

## ISO 20022 Payments (XML + Business Rejections)

- Code: [tests/integration/iso20022_payments](https://github.com/pilosus/pathbridge/tree/main/tests/integration/iso20022_payments)
- Validator shape: payment XML location errors plus business rejection reason codes
- Highlights:
  - `pain.001`-style path mapping with list-heavy structures
  - fixtures for schema-style errors (`cvc-*`) and business reasons (`AM04`, `AC03`, `RC01`)
  - namespace/envelope prefix handling and Marshmallow folding

Run:

```bash
uv run pytest -vvs tests/integration/iso20022_payments/test_iso20022_payments.py
```
