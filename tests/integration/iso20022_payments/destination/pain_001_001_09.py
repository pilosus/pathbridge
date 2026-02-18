from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class GroupHeader85:
    msg_id: str = field(metadata={"name": "MsgId"})


@dataclass
class PostalAddress24:
    ctry: str = field(metadata={"name": "Ctry"})
    adr_line: list[str] = field(default_factory=list, metadata={"name": "AdrLine"})


@dataclass
class PartyIdentification135:
    nm: str = field(metadata={"name": "Nm"})
    pstl_adr: PostalAddress24 | None = field(default=None, metadata={"name": "PstlAdr"})


@dataclass
class AccountIdentification4Choice:
    iban: str = field(metadata={"name": "IBAN"})


@dataclass
class CashAccount38:
    id: AccountIdentification4Choice = field(metadata={"name": "Id"})


@dataclass
class PaymentIdentification7:
    end_to_end_id: str = field(metadata={"name": "EndToEndId"})


@dataclass
class AmountType4Choice:
    instd_amt: str = field(metadata={"name": "InstdAmt"})


@dataclass
class CreditTransferTransaction39:
    pmt_id: PaymentIdentification7 = field(metadata={"name": "PmtId"})
    amt: AmountType4Choice = field(metadata={"name": "Amt"})
    cdtr: PartyIdentification135 = field(metadata={"name": "Cdtr"})
    cdtr_acct: CashAccount38 = field(metadata={"name": "CdtrAcct"})


@dataclass
class PaymentInstruction30:
    pmt_inf_id: str = field(metadata={"name": "PmtInfId"})
    reqd_exctn_dt: str = field(metadata={"name": "ReqdExctnDt"})
    dbtr: PartyIdentification135 = field(metadata={"name": "Dbtr"})
    cdt_trf_tx_inf: list[CreditTransferTransaction39] = field(
        default_factory=list, metadata={"name": "CdtTrfTxInf"}
    )


@dataclass
class CustomerCreditTransferInitiationV09:
    grp_hdr: GroupHeader85 = field(metadata={"name": "GrpHdr"})
    pmt_inf: list[PaymentInstruction30] = field(
        default_factory=list, metadata={"name": "PmtInf"}
    )


@dataclass
class Document:
    cstmr_cdt_trf_initn: CustomerCreditTransferInitiationV09 = field(
        metadata={"name": "CstmrCdtTrfInitn"}
    )

    class Meta:
        name = "Document"
