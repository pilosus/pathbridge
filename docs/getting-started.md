# Getting Started

## Core API

PathBridge exposes four primary public functions:

- `compile_rules(rules)` -> compile raw mapping rules into regex-backed runtime rules.
- `translate_location(location, compiled_rules)` -> translate one validator location.
- `insert_error(root, facade_path, message)` -> insert one message into nested dict.
- `to_marshmallow(items, compiled_rules)` -> bulk translation into error dict.

## 1. Define Rules

Rules map destination/document paths to facade/application paths:

```python
rules = {
    "Return[1]/Contact[1]/Phone[1]": "person/phones[0]",
    "Return[1]/Contact[1]/Phone[2]": "person/phones[1]",
}
```

Destination paths are usually XPath-like and may include namespace prefixes.
If you prefer not to write rules manually, use `make_shape` (shaper) and
`build_rules` (tracer) from `pathbridge.extras`.

## 2. Compile Once

```python
from pathbridge import compile_rules

compiled = compile_rules(rules)
```

Compile once at startup and reuse `compiled` in request/validation flows.

## 3. Translate Validator Paths

```python
from pathbridge import translate_location

translate_location("/Return[1]/Contact[1]/Phone[2]", compiled)
# "person/phones[1]"
```

## 4. Build Marshmallow-Style Errors

```python
from pathbridge import to_marshmallow

items = [
    ("/Return[1]/Contact[1]/Phone[2]", "Invalid phone"),
    ("/Return[1]/Contact[1]/Phone[1]", "Required field"),
]

errors = to_marshmallow(items, compiled)
```

Result shape:

```python
{
    "person": {
        "phones": {
            1: ["Invalid phone"],
            0: ["Required field"],
        }
    }
}
```

## Matching Behavior Notes

- Matching is case-insensitive.
- Namespace prefixes are tolerated.
- Extra leading path prefixes in validator locations are tolerated.
- Facade templates can convert one-based validator indices into zero-based application
  indices where appropriate.
