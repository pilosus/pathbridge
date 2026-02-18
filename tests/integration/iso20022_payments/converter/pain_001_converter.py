from __future__ import annotations

import tests.integration.iso20022_payments.destination.pain_001_001_09 as pain
import tests.integration.iso20022_payments.facade.payment_facade as facade


def _normalize_country_code(value: str) -> str:
    return value.strip().upper()


def _normalize_iban(value: str) -> str:
    return value.replace(" ", "").upper()


def to_pain_001_001_09(data: facade.PaymentInitiationRequest) -> pain.Document:
    customer = data.customer_credit_transfer_initiation
    return pain.Document(
        cstmr_cdt_trf_initn=pain.CustomerCreditTransferInitiationV09(
            grp_hdr=pain.GroupHeader85(msg_id=customer.message_id),
            pmt_inf=[
                pain.PaymentInstruction30(
                    pmt_inf_id=info.payment_info_id,
                    reqd_exctn_dt=info.requested_execution_date,
                    dbtr=pain.PartyIdentification135(
                        nm=info.debtor_name,
                        pstl_adr=None,
                    ),
                    cdt_trf_tx_inf=[
                        pain.CreditTransferTransaction39(
                            pmt_id=pain.PaymentIdentification7(
                                end_to_end_id=transfer.end_to_end_id
                            ),
                            amt=pain.AmountType4Choice(instd_amt=transfer.amount),
                            cdtr=pain.PartyIdentification135(
                                nm=transfer.creditor.name,
                                pstl_adr=pain.PostalAddress24(
                                    ctry=_normalize_country_code(
                                        transfer.creditor.postal_address.country
                                    ),
                                    adr_line=transfer.creditor.postal_address.address_line,
                                ),
                            ),
                            cdtr_acct=pain.CashAccount38(
                                id=pain.AccountIdentification4Choice(
                                    iban=_normalize_iban(transfer.creditor.iban)
                                )
                            ),
                        )
                        for transfer in info.credit_transfers
                    ],
                )
                for info in customer.payment_infos
            ],
        )
    )

