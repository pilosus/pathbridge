# CLI

PathBridge provides the `pathbridge` CLI.

## Version

```bash
pathbridge --version
```

## Compile Command

`pathbridge compile` generates a Python module that contains raw and/or compiled rules.

```bash
pathbridge compile \
  --output-dir . \
  --output-package mtr.translation_rules \
  --output-module compiled \
  --facade-class ./tests/integration/hmrc_main_tax_return/facade/mtr_facade.py:MTR \
  --destination-module ./tests/integration/hmrc_main_tax_return/destination/mtr_v1_1.py \
  --facade-to-destination ./tests/integration/hmrc_main_tax_return/converter/mtr_converter.py:to_mtr_v1_1 \
  --shape-list-len 10 \
  --facade-root-tag mtr
```

## Required Arguments

- `--output-package`: dotted package name for generated output.
- `--facade-class`: facade dataclass reference (`module:Class` or `path.py:Class`).
- `--destination-module`: destination module path or import path.
- `--facade-to-destination`: converter callable reference (`module:function` or `path.py:function`).

## Useful Options

- `--output-dir`: where package tree is created (default: current directory).
- `--output-module`: generated filename without `.py` (default: `compiled_rules`).
- `--emit`: `both`, `raw`, or `compiled`.
- `--shape-list-len`: list length used by shape generator.
- `--shape-override PATH=VALUE`: repeatable shape overrides.
- `--facade-root-tag`: root facade segment.
- `--lift-functions NAME`: repeatable helper functions to preserve tracing tags.
