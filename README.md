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

## Extras

`pathbridge.extras` provides helper utilities for generating rules from your
converter:

- `make_shape(...)`: build a populated sample facade object.
- `build_rules(...)`: trace a sample conversion and produce `Destination -> Facade`
  mapping rules.

### Extras example

```python
import dataclasses
import types

from pathbridge import compile_rules, to_marshmallow
from pathbridge.extras import build_rules, make_shape


@dataclasses.dataclass
class FacadeName:
    first: str
    last: str


@dataclasses.dataclass
class Facade:
    name: FacadeName
    phones: list[str]


@dataclasses.dataclass
class NameXml:
    first_name: str = dataclasses.field(metadata={"name": "FirstName"})
    surname: str = dataclasses.field(metadata={"name": "Surname"})


@dataclasses.dataclass
class ReturnXml:
    name: NameXml = dataclasses.field(metadata={"name": "YourName"})
    phones: list[str] = dataclasses.field(metadata={"name": "Phone"})

    class Meta:
        name = "Return"


def convert(src: Facade) -> ReturnXml:
    return ReturnXml(
        name=NameXml(first_name=src.name.first, surname=src.name.last),
        phones=src.phones,
    )


shape = make_shape(Facade, list_len=2)
rules = build_rules(
    model_module=types.SimpleNamespace(ReturnXml=ReturnXml, NameXml=NameXml),
    converter=convert,
    shape=shape,
    root_tag="facade",
)

compiled = compile_rules(rules)
errors = to_marshmallow(
    [
        ("/Return[1]/NameXml[1]/FirstName[1]", "Required field"),
        ("/Return[1]/Phone[2]/Phone[1]", "Invalid phone"),
    ],
    compiled,
)

print(rules)
# {
#   'Return[1]/NameXml[1]/FirstName[1]': 'facade/name/first',
#   'Return[1]/Phone[2]/Phone[1]': 'facade/phones[1]',
#   ...
# }
print(errors)
# {
#   'facade': {
#     'name': {'first': ['Required field']},
#     'phones': {1: ['Invalid phone']},
#   }
# }
```

### Custom shape defaults

`make_shape(...)` accepts `type_defaults` so you can override generated defaults
for specific types:

```python
from decimal import Decimal

shape = make_shape(
    Facade,
    list_len=2,
    type_defaults={
        str: "sample",
        int: 42,
        Decimal: Decimal("1.23"),
    },
)
```
