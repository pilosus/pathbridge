# OpenAPI JSON Schema Integration

Real-world-style integration example for OpenAPI request/response validation
errors translated into application-facing paths.

## What it covers

- Request body validation failures (format, minimum, pattern)
- Response body validation failures (enum, type)
- Unmapped errors routed to `_meta.misses`
- End-to-end mapping flow:
  - `build_rules(...)` from a facade -> destination converter
  - `translate_location(...)` for individual validator locations
  - `to_marshmallow(...)` for nested, API-ready error payloads

## Files

```
openapi_json_schema/
├── schema/
│   └── openapi_3_1_order_api.yaml
├── destination/
│   └── order_api_document.py
├── facade/
│   └── order_api_facade.py
├── converter/
│   └── order_api_converter.py
├── fixtures/
│   └── errors.py
└── test_openapi_json_schema.py
```

## Run this integration test

```bash
uv run pytest -vvs tests/integration/openapi_json_schema/test_openapi_json_schema.py
```
