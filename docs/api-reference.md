# API Reference

## Public Imports

```python
from pathbridge import (
    compile_rules,
    translate_location,
    insert_error,
    to_marshmallow,
)
```

## `compile_rules(rules)`

Compiles a raw mapping of destination paths to facade paths.

- Input type: `dict[str, str]`
- Output type: sequence of `(compiled_regex, facade_template)`

## `translate_location(location, compiled_rules)`

Translates one validator-reported location to one facade path.

- Returns `str` when matched.
- Returns `None` when no rule matches.

## `insert_error(root, facade_path, message)`

Inserts `message` into a nested error dictionary at `facade_path`.

- Mutates `root` in place.
- Tolerates keyed and indexed path segments.

## `to_marshmallow(items, compiled_rules, *, default_message="Invalid", include_meta=False)`

Converts input error items into a Marshmallow-style nested dictionary.

Accepted `items` formats:

- iterable of `(location, message)` tuples
- iterable of dicts with `location` and `message`/`text`
- iterable of objects exposing `.location` and `.text`

When `include_meta=True`, `_meta` is added with totals and misses.

## Extras Module

```python
from pathbridge.extras import make_shape, build_rules, trace_converter
```

- `make_shape(...)`: generate sample facade instances.
- `build_rules(...)`: trace converter once and return destination-to-facade rules.
- `trace_converter(...)`: low-level tracing context manager.
