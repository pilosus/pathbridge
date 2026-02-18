# ISO 20022 Schema Sources

This integration test package uses a compact hand-written destination model to keep
tests fast and deterministic. For full-scale regression tests, use the official XSDs:

- `pain.001.001.03` (legacy): https://www.iso20022.org/message/14316/download
- `pain.001.001.09`: https://www.iso20022.org/message/14346/download
- `pain.001.001.12` (current): https://www.iso20022.org/message/22909/download
- `pacs.008.001.13` (current): https://www.iso20022.org/message/23229/download
- `camt.053.001.13` (current): https://www.iso20022.org/message/23168/download

Validation/business error examples in this package are based on:

- XML validator examples: https://knowledge.xmldation.com/support/validator
- EPC reason-code guidance (SCT R-transactions):
  https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2024-11/EPC135-18%20v6.0%20Guidance%20on%20Reason%20Codes%20for%20SCT%20R-transactions.pdf

