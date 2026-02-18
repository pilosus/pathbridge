# UK Main Tax Return

A real-world example of UK Main Tax Return (MTR) XML schema, version 1.1, generated 31 October 2025. 
Source: [HMRC](https://www.gov.uk/government/publications/self-assessment-technical-specifications-2026-for-individual-returns)

## Structure

```
hmrc_main_tax_return/
├── schema/
│   └── MTR-v1-1.xsd              # HMRC XSD schema (source of truth)
├── destination/
│   └── mtr_v1_1.py                # auto-generated from XSD via xsdata
├── facade/
│   └── mtr_facade.py              # hand-written app-level dataclasses
└── converter/
    ├── mtr_converter.py           # facade -> destination converter
    └── utils.py                   # shared conversion helpers
```

- `schema/` - the original HMRC XSD file, kept as-is for reference and regeneration.
- `destination/` - Python dataclasses **auto-generated** from the XSD by
  [xsdata](https://xsdata.readthedocs.io/). Mirrors the XML structure 1:1.
  Do not edit by hand; regenerate with:
  ```bash
  uv run xsdata generate schema/MTR-v1-1.xsd --package destination
  ```
- `facade/` - **hand-written** dataclasses that represent the same tax return
  in an app-friendly shape (clean names, native Python types like `Decimal`,
  `date`, `StrEnum`).
- `converter/` - translates facade objects into destination (xsdata) objects
  so they can be serialised to XML.
