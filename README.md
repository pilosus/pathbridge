# PathBridge

> Bridge validator locations (XPath/JSONPath/JSON Pointer) back to your application model paths, and emit structured errors (Marshmallow-ready).

[![PyPI version](https://img.shields.io/pypi/v/pathbridge.svg)](https://pypi.org/project/pathbridge/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/pathbridge.svg)](https://pypi.org/project/pathbridge/)

## Why

Validators (XSD/Schematron, JSON Schema) report failures at **document locations** (XPath/JSONPath).  
Your users need errors on **your model** (Pydantic/Marshmallow/dataclasses). PathBridge converts between the two.

- Prefix & case tolerant (e.g., `hd:`, `MTR:`).
- Fixes 1-based indices to Python 0-based.
- Works with plain mappings or an optional tracer (add-on) that learns rules from your converter.

## Install

```bash
pip install pathbridge
```

## Quick start

```python
from pathbridge import compile_rules, translate_location, to_marshmallow

# 1. Provide or load rules: destination path -> facade (your app models) path 
rules = {
    "Return[1]/Contact[1]/Phone[1]": "person/phones[0]",
    "Return[1]/Contact[1]/Phone[2]": "person/phones[1]",
}

compiled = compile_rules(rules)

# 2. Translate validator location (e.g. from Schematron SVRL)
loc = "/Return[1]/Contact[1]/Phone[2]"
print(translate_location(loc, compiled))
# "person/phones[1]"

# 3. Transform error location into a Marshmallow-style error dict
errors = to_marshmallow([(loc, "Invalid phone")], compiled)
# {'person': {'phones': {1: ['Invalid phone']}}}
```
