# Extras

`pathbridge.extras` provides helpers for generating mapping rules from your real
converter code instead of writing rules by hand.

## `make_shape(...)`

Build a sample facade object (including nested dataclasses/lists) used for tracing.

```python
from pathbridge.extras import make_shape

shape = make_shape(FacadeModel, list_len=2)
```

You can customize defaults:

```python
from decimal import Decimal

shape = make_shape(
    FacadeModel,
    list_len=2,
    type_defaults={str: "sample", int: 42, Decimal: Decimal("1.23")},
)
```

## `build_rules(...)`

Trace a converter call and extract destination-to-facade mapping rules.

```python
from pathbridge.extras import build_rules

rules = build_rules(
    destination_module=destination_module,
    facade_to_destination=convert,
    facade_shape=shape,
    facade_root_tag="facade",
)
```

## `trace_converter(...)`

For lower-level control, use the context manager directly:

```python
from pathbridge.extras import trace_converter

with trace_converter(
    destination_module=destination_module,
    facade_to_destination=convert,
    facade_root_tag="facade",
) as run:
    result, rules = run(shape)
```

## Typical Flow

1. Create shape with `make_shape`.
2. Generate rules with `build_rules`.
3. Compile rules with `compile_rules`.
4. Translate runtime validator failures with `to_marshmallow`.
