from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True, slots=True)
class PostalAddress:
    country: str
    address_line: list[str]


@dataclass(frozen=True, kw_only=True, slots=True)
class Creditor:
    name: str
    iban: str
    postal_address: PostalAddress


@dataclass(frozen=True, kw_only=True, slots=True)
class CreditTransfer:
    end_to_end_id: str
    amount: str
    creditor: Creditor


@dataclass(frozen=True, kw_only=True, slots=True)
class PaymentInfo:
    payment_info_id: str
    requested_execution_date: str
    debtor_name: str
    credit_transfers: list[CreditTransfer]


@dataclass(frozen=True, kw_only=True, slots=True)
class CustomerCreditTransferInitiation:
    message_id: str
    payment_infos: list[PaymentInfo]


@dataclass(frozen=True, kw_only=True, slots=True)
class PaymentInitiationRequest:
    customer_credit_transfer_initiation: CustomerCreditTransferInitiation

