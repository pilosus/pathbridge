from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ISO20022ErrorFixture:
    code: str
    location: str
    message: str
    expected_facade_path: str | None
    source: str


SCHEMA_REFERENCES: tuple[tuple[str, str], ...] = (
    ("pain.001.001.03 (legacy)", "https://www.iso20022.org/message/14316/download"),
    ("pain.001.001.09", "https://www.iso20022.org/message/14346/download"),
    ("pain.001.001.12 (current)", "https://www.iso20022.org/message/22909/download"),
    ("pacs.008.001.13 (current)", "https://www.iso20022.org/message/23229/download"),
    ("camt.053.001.13 (current)", "https://www.iso20022.org/message/23168/download"),
)


XSD_ERROR_FIXTURES: tuple[ISO20022ErrorFixture, ...] = (
    ISO20022ErrorFixture(
        code="cvc-complex-type.2.4.a",
        location="/Document[1]/CstmrCdtTrfInitn[1]/PmtInf[1]/ReqdExctnDt[1]",
        message=(
            "cvc-complex-type.2.4.a: Invalid content was found starting with "
            "element 'ReqdExctnDt'."
        ),
        expected_facade_path=(
            "payment_request/customer_credit_transfer_initiation/"
            "payment_infos[0]/requested_execution_date"
        ),
        source="https://knowledge.xmldation.com/support/validator/cvc-complex-type-2-4-a",
    ),
    ISO20022ErrorFixture(
        code="cvc-pattern-valid",
        location=(
            "/ns2:Document[1]/ns2:CstmrCdtTrfInitn[1]/ns2:PmtInf[1]/"
            "ns2:CdtTrfTxInf[1]/ns2:PmtId[1]/ns2:EndToEndId[1]"
        ),
        message=(
            "cvc-pattern-valid: Value does not satisfy the EndToEndId pattern "
            "constraint."
        ),
        expected_facade_path=(
            "payment_request/customer_credit_transfer_initiation/"
            "payment_infos[0]/credit_transfers[0]/end_to_end_id"
        ),
        source="https://knowledge.xmldation.com/support/validator",
    ),
    ISO20022ErrorFixture(
        code="cvc-totalDigits-valid",
        location=(
            "/DataPDU[1]/Body[1]/Document[1]/CstmrCdtTrfInitn[1]/PmtInf[1]/"
            "CdtTrfTxInf[2]/Amt[1]/InstdAmt[1]"
        ),
        message=(
            "cvc-totalDigits-valid: Value '-12.999' exceeds the allowed number "
            "of fraction digits."
        ),
        expected_facade_path=(
            "payment_request/customer_credit_transfer_initiation/"
            "payment_infos[0]/credit_transfers[1]/amount"
        ),
        source="https://knowledge.xmldation.com/support/validator",
    ),
    ISO20022ErrorFixture(
        code="cvc-enumeration-valid",
        location=(
            "/Document[1]/CstmrCdtTrfInitn[1]/PmtInf[2]/CdtTrfTxInf[1]/"
            "Cdtr[1]/PstlAdr[1]/Ctry[1]"
        ),
        message=(
            "cvc-enumeration-valid: Value 'ZZ' is not facet-valid with respect "
            "to country code enumeration."
        ),
        expected_facade_path=(
            "payment_request/customer_credit_transfer_initiation/"
            "payment_infos[1]/credit_transfers[0]/creditor/postal_address/country"
        ),
        source="https://knowledge.xmldation.com/support/validator",
    ),
    ISO20022ErrorFixture(
        code="cvc-elt.1",
        location="/Document[1]/Foo[1]",
        message=("cvc-elt.1: Cannot find the declaration of element 'Foo'."),
        expected_facade_path=None,
        source="https://knowledge.xmldation.com/support/validator/cvc-elt-1",
    ),
)


BUSINESS_REJECTION_FIXTURES: tuple[ISO20022ErrorFixture, ...] = (
    ISO20022ErrorFixture(
        code="AM04",
        location=(
            "/Document[1]/CstmrCdtTrfInitn[1]/PmtInf[1]/CdtTrfTxInf[2]/"
            "Amt[1]/InstdAmt[1]"
        ),
        message=("AM04: Insufficient funds on debtor account."),
        expected_facade_path=(
            "payment_request/customer_credit_transfer_initiation/"
            "payment_infos[0]/credit_transfers[1]/amount"
        ),
        source=(
            "https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/"
            "2024-11/EPC135-18%20v6.0%20Guidance%20on%20Reason%20Codes%20for%20"
            "SCT%20R-transactions.pdf"
        ),
    ),
    ISO20022ErrorFixture(
        code="AC03",
        location=(
            "/Envelope[1]/Document[1]/CstmrCdtTrfInitn[1]/PmtInf[2]/"
            "CdtTrfTxInf[3]/CdtrAcct[1]/Id[1]/IBAN[1]"
        ),
        message=("AC03: Invalid creditor account number (IBAN)."),
        expected_facade_path=(
            "payment_request/customer_credit_transfer_initiation/"
            "payment_infos[1]/credit_transfers[2]/creditor/iban"
        ),
        source=(
            "https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/"
            "2024-11/EPC135-18%20v6.0%20Guidance%20on%20Reason%20Codes%20for%20"
            "SCT%20R-transactions.pdf"
        ),
    ),
    ISO20022ErrorFixture(
        code="RC01",
        location="/Document[1]/CstmrCdtTrfInitn[1]/PmtInf[3]/Dbtr[1]/Nm[1]",
        message=("RC01: Debtor agent identifier is invalid."),
        expected_facade_path=(
            "payment_request/customer_credit_transfer_initiation/"
            "payment_infos[2]/debtor_name"
        ),
        source=(
            "https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/"
            "2024-11/EPC135-18%20v6.0%20Guidance%20on%20Reason%20Codes%20for%20"
            "SCT%20R-transactions.pdf"
        ),
    ),
    ISO20022ErrorFixture(
        code="FF01",
        location="/Document[1]/AppHdr[1]/Fr[1]/FIId[1]",
        message=("FF01: Invalid file format in the submitted payment message."),
        expected_facade_path=None,
        source=(
            "https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/"
            "2024-11/EPC135-18%20v6.0%20Guidance%20on%20Reason%20Codes%20for%20"
            "SCT%20R-transactions.pdf"
        ),
    ),
)
