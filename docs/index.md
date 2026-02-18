# PathBridge

PathBridge helps you translate validator-reported locations (XPath/JSONPath/JSON Pointer)
back to your application model paths and build structured validation errors.

## Why PathBridge

Validators report failures against document locations. Your application usually needs
errors attached to facade or DTO fields. PathBridge bridges that gap:

- Compile destination-to-facade mapping rules once.
- Translate runtime validator locations quickly.
- Emit nested error dictionaries compatible with Marshmallow-style structures.
- Prefer automation over manual rules: `make_shape` (shaper) and `build_rules`
  (tracer) can generate mappings from your destination classes and converter.

## Install

```bash
pip install pathbridge
```

## Quick Start

```python
from pathbridge import compile_rules, translate_location, to_marshmallow

rules = {
    "Return[1]/Contact[1]/Phone[1]": "person/phones[0]",
    "Return[1]/Contact[1]/Phone[2]": "person/phones[1]",
}

compiled = compile_rules(rules)
location = "/Return[1]/Contact[1]/Phone[2]"

print(translate_location(location, compiled))
# person/phones[1]

errors = to_marshmallow([(location, "Invalid phone")], compiled)
# {"person": {"phones": {1: ["Invalid phone"]}}}
```

## Next Steps

- Read [Getting Started](getting-started.md) for path-matching behavior and usage details.
- Use [Extras](extras.md) to generate rules by tracing your converter automatically.
- Use the [CLI](cli.md) to generate importable Python modules with compiled rules.
- Explore [Real-life Examples](real-life-example.md) for HMRC MTR, OpenAPI, and ISO 20022 integrations.
