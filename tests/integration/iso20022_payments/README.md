# ISO 20022 Payments

Real-world integration example for customer credit transfer initiation
(`pain.001`) with fixture corpora for:

- schema validation errors (XPath + `cvc-*` style messages)
- payment business rejections (`AM04`, `AC03`, `RC01`, `FF01`)

## Why this integration exists

HMRC proves deep XSD mapping. This package adds a second production-style domain:
payments. It validates that PathBridge handles:

- repeating payment blocks (`PmtInf[*]`, `CdtTrfTxInf[*]`)
- namespace-prefixed paths (for example `ns2:Document`)
- envelope/header prefixes before the business document
- a mix of strict XSD errors and business-level reason codes

## Structure

```
iso20022_payments/
├── schema/
│   └── README.md                      # official schema and error sources
├── destination/
│   └── pain_001_001_09.py             # compact destination dataclasses
├── facade/
│   └── payment_facade.py              # app-facing model
├── converter/
│   └── pain_001_converter.py          # facade -> destination converter
├── fixtures/
│   └── errors.py                      # curated XSD + business error corpus
└── test_iso20022_payments.py
```

## Running only this integration test

```bash
uv run pytest -vvs tests/integration/iso20022_payments/test_iso20022_payments.py
```
