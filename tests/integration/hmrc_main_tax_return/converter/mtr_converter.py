from __future__ import annotations

import tests.integration.hmrc_main_tax_return.destination.mtr_v1_1 as mtr
import tests.integration.hmrc_main_tax_return.facade.mtr_facade as d
from tests.integration.hmrc_main_tax_return.converter.utils import (
    decimal_str_or_none,
    decode_attachment,
    xml_date_or_none,
)

#
# Mappings & Other Constants
#

YES_NO_MAPPING: dict[d.MTRYesNoType, mtr.MtrYesNoType] = {
    d.MTRYesNoType.YES: mtr.MtrYesNoType.YES,
    d.MTRYesNoType.NO: mtr.MtrYesNoType.NO,
}

YES_MAPPING: dict[d.MTRYesType, mtr.MtrYesType] = {
    d.MTRYesType.YES: mtr.MtrYesType.YES,
}

TAX_PAYER_STATUS_MAPPING: dict[
    d.TaxPayerStatus, mtr.YourPersonalDetailsTaxpayerStatus
] = {
    d.TaxPayerStatus.C: mtr.YourPersonalDetailsTaxpayerStatus.C,
    d.TaxPayerStatus.S: mtr.YourPersonalDetailsTaxpayerStatus.S,
    d.TaxPayerStatus.U: mtr.YourPersonalDetailsTaxpayerStatus.U,
}

STUDENT_LOAN_PLAN_MAPPING: dict[
    d.MTRStudentLoanPlanType, mtr.StudentLoanRepaymentsPlanType
] = {
    d.MTRStudentLoanPlanType.PLAN1: mtr.StudentLoanRepaymentsPlanType.VALUE_01,
    d.MTRStudentLoanPlanType.PLAN2: mtr.StudentLoanRepaymentsPlanType.VALUE_02,
    d.MTRStudentLoanPlanType.PLAN4: mtr.StudentLoanRepaymentsPlanType.VALUE_04,
}

POSTGRADUATE_LOAN_PLAN_MAPPING: dict[
    d.MTRPostgraduateLoanPlanType, mtr.StudentLoanRepaymentsPostgraduateLoanPlanType
] = {
    d.MTRPostgraduateLoanPlanType.PLAN3: mtr.StudentLoanRepaymentsPostgraduateLoanPlanType.VALUE_03,
}


ATTACHMENT_FILE_FORMAT_MAPPING: dict[
    d.MTRAttachmentFileFormat, mtr.AttachmentFileFormat
] = {
    d.MTRAttachmentFileFormat.PDF: mtr.AttachmentFileFormat.PDF,
}


#
# Public API
#


def to_mtr_v1_1(data: d.MTR) -> mtr.Mtr:
    result = mtr.Mtr(
        declaration=_get_declaration(data),
        sa100=_get_sa100(data),
        sa102=_get_102(data),
        sa102_m=_get_102m(data),
        sa103_s=_get_103s(data),
        sa103_f=_get_103f(data),
        sa104_s=_get_104s(data),
        sa104_f=_get_104f(data),
        sa105=_get_105(data),
        sa106=_get_106(data),
        sa107=_get_sa107(data),
        sa108=_get_sa108(data),
        sa109=_get_sa109(data),
        sa110=_get_sa110(data),
        welsh_return=_yes(data.welsh_return),
        taxpayer_name=data.taxpayer_name,
        attached_files=_get_attached_files(data),
        amended_return=_yes(data.amended_return),
    )
    return result


#
# Helpers
#


def _tax_payer_status(value: d.TaxPayerStatus) -> mtr.YourPersonalDetailsTaxpayerStatus:
    return TAX_PAYER_STATUS_MAPPING[value]


def _student_loan_plan(
    value: d.MTRStudentLoanPlanType | None,
) -> mtr.StudentLoanRepaymentsPlanType | None:
    if value is None:
        return None
    return STUDENT_LOAN_PLAN_MAPPING[value]


def _postgraduate_loan_plan(
    value: d.MTRPostgraduateLoanPlanType | None,
) -> mtr.StudentLoanRepaymentsPostgraduateLoanPlanType | None:
    if value is None:
        return None
    return POSTGRADUATE_LOAN_PLAN_MAPPING[value]


def _attachment_file_format(
    value: d.MTRAttachmentFileFormat,
) -> mtr.AttachmentFileFormat:
    return ATTACHMENT_FILE_FORMAT_MAPPING[value]


def _yes_no(value: d.MTRYesNoType | None) -> mtr.MtrYesNoType | None:
    if value is None:
        return None
    return YES_NO_MAPPING[value]


def _yes(value: d.MTRYesType | None) -> mtr.MtrYesType | None:
    if value is None:
        return None
    return YES_MAPPING[value]


def _get_declaration(data: d.MTR) -> mtr.Mtr.Declaration:
    return mtr.Mtr.Declaration(
        individual_declaration=_yes(data.declaration.individual_declaration),
        agent_declaration=_yes(data.declaration.agent_declaration),
    )


def _get_sa100(data: d.MTR) -> mtr.Mtr.Sa100:
    return mtr.Mtr.Sa100(
        your_personal_details=mtr.Mtr.Sa100.YourPersonalDetails(
            taxpayer_status=_tax_payer_status(
                data.sa100.personal_details.taxpayer_status
            ),
            date_of_birth=xml_date_or_none(data.sa100.personal_details.dob),
            new_address=mtr.Mtr.Sa100.YourPersonalDetails.NewAddress(
                address_line1=data.sa100.personal_details.new_address.line1,
                address_line2=data.sa100.personal_details.new_address.line2,
                address_line3=data.sa100.personal_details.new_address.line3,
                address_line4=data.sa100.personal_details.new_address.line4,
                postcode=data.sa100.personal_details.new_address.postcode,
                effective_from=xml_date_or_none(
                    data.sa100.personal_details.new_address.effective_from
                ),
            )
            if data.sa100.personal_details.new_address
            else None,
            telephone_number=data.sa100.personal_details.phone_number,
        ),
        your_tax_return=mtr.Mtr.Sa100.YourTaxReturn(
            employment_schedule=_yes(data.sa100.tax_return.employment_schedule),
            number_of_employment_schedules=data.sa100.tax_return.number_of_employment_schedules
            if data.sa100.tax_return.number_of_employment_schedules
            else None,
            minister_of_religion_schedule=_yes(
                data.sa100.tax_return.minister_of_religion
            ),
            number_of_minister_of_religion_schedules=data.sa100.tax_return.number_of_minister_of_religion_schedules
            if data.sa100.tax_return.number_of_minister_of_religion_schedules
            else None,
            full_self_employment_schedule=_yes(
                data.sa100.tax_return.full_self_employment_schedule
            ),
            number_of_full_self_employment_schedules=data.sa100.tax_return.number_of_full_self_employment_schedules
            if data.sa100.tax_return.number_of_full_self_employment_schedules
            else None,
            short_self_employment_schedule=_yes(
                data.sa100.tax_return.short_self_employment_schedule
            ),
            number_of_short_self_employment_schedules=data.sa100.tax_return.number_of_short_self_employment_schedules
            if data.sa100.tax_return.number_of_short_self_employment_schedules
            else None,
            lloyds_underwriter_schedule=_yes(
                data.sa100.tax_return.lloyds_underwriter_schedule
            ),
            full_partnership_schedule=_yes(
                data.sa100.tax_return.full_partnership_schedule
            ),
            number_of_full_partnership_schedules=data.sa100.tax_return.number_of_full_partnership_schedules
            if data.sa100.tax_return.number_of_full_partnership_schedules
            else None,
            short_partnership_schedule=_yes(
                data.sa100.tax_return.short_partnership_schedule
            ),
            number_of_short_partnership_schedules=data.sa100.tax_return.number_of_short_partnership_schedules
            if data.sa100.tax_return.number_of_short_partnership_schedules
            else None,
            ukproperty_schedule=_yes(data.sa100.tax_return.uk_property_schedule),
            foreign_schedule=_yes(data.sa100.tax_return.foreign_schedule),
            trusts_schedule=_yes(data.sa100.tax_return.trust_schedule),
            capital_gains_schedule=_yes(data.sa100.tax_return.capital_gains_schedule),
            capital_gains_computation_attached=_yes(
                data.sa100.tax_return.capital_gains_computation_attached
            ),
            residence_figschedule=_yes(
                data.sa100.tax_return.resident_remittance_schedule
            ),
            additional_information_schedule=_yes(
                data.sa100.tax_return.additional_information_schedule
            ),
        )
        if data.sa100.tax_return
        else None,
        student_loan_repayments=mtr.Mtr.Sa100.StudentLoanRepayments(
            income_contingent_student_loan_notification=_yes(
                data.sa100.student_loan_repayments.income_contingent_student_loan_notification
            ),
            student_loan_repayment_deducted_amount=decimal_str_or_none(
                data.sa100.student_loan_repayments.student_loan_repayment_deducted_amount
            ),
            postgraduate_loan_repayment_deducted_amount=decimal_str_or_none(
                data.sa100.student_loan_repayments.postgraduate_loan_repayment_deducted_amount
            ),
            plan_type=_student_loan_plan(
                data.sa100.student_loan_repayments.student_loan_plan_type
            ),
            postgraduate_loan_plan_type=_postgraduate_loan_plan(
                data.sa100.student_loan_repayments.postgraduate_loan_plan_type
            ),
        )
        if data.sa100.student_loan_repayments
        else None,
        income=mtr.Mtr.Sa100.Income(
            ukinterest_and_dividends=mtr.Mtr.Sa100.Income.UkinterestAndDividends(
                taxed_bank_building_society_etc_interest=decimal_str_or_none(
                    data.sa100.income.uk_interest_and_dividends.taxed_bank_building_society_etc_interest
                ),
                untaxed_ukinterest_etc=decimal_str_or_none(
                    data.sa100.income.uk_interest_and_dividends.untaxed_uk_interest_etc
                ),
                untaxed_foreign_interest=decimal_str_or_none(
                    data.sa100.income.uk_interest_and_dividends.untaxed_foreign_interest
                ),
                company_dividends=decimal_str_or_none(
                    data.sa100.income.uk_interest_and_dividends.company_dividends
                ),
                unit_trust_etc_dividends=decimal_str_or_none(
                    data.sa100.income.uk_interest_and_dividends.unit_trust_etc_dividends
                ),
                foreign_dividends=decimal_str_or_none(
                    data.sa100.income.uk_interest_and_dividends.foreign_dividends
                ),
                tax_taken_off_foreign_dividends=decimal_str_or_none(
                    data.sa100.income.uk_interest_and_dividends.tax_taken_off_foreign_dividends
                ),
            )
            if data.sa100.income.uk_interest_and_dividends
            else None,
            state_benefits=mtr.Mtr.Sa100.Income.StateBenefits(
                annual_state_pension=decimal_str_or_none(
                    data.sa100.income.state_benefits.annual_state_pension
                ),
                state_pension_lump_sum=decimal_str_or_none(
                    data.sa100.income.state_benefits.state_pension_lump_sum
                ),
                tax_taken_off_pension_lump_sum=decimal_str_or_none(
                    data.sa100.income.state_benefits.tax_taken_off_pension_lump_sum
                ),
                other_pensions_and_retirement_annuities=decimal_str_or_none(
                    data.sa100.income.state_benefits.other_pensions_and_retirement_annuities
                ),
                tax_taken_off_pensions_and_retirement_annuities=decimal_str_or_none(
                    data.sa100.income.state_benefits.tax_taken_off_pensions_and_retirement_annuities
                ),
                incapacity_benefit=decimal_str_or_none(
                    data.sa100.income.state_benefits.incapacity_benefit
                ),
                tax_taken_off_incapacity_benefit=decimal_str_or_none(
                    data.sa100.income.state_benefits.tax_taken_off_incapacity_benefit
                ),
                jobseekers_allowance=decimal_str_or_none(
                    data.sa100.income.state_benefits.jobseekers_allowance
                ),
                other_state_pensions_and_benefits=decimal_str_or_none(
                    data.sa100.income.state_benefits.other_state_pensions_and_benefits
                ),
            )
            if data.sa100.income.state_benefits
            else None,
            other_ukincome=mtr.Mtr.Sa100.Income.OtherUkincome(
                other_taxable_income_details=mtr.Mtr.Sa100.Income.OtherUkincome.OtherTaxableIncomeDetails(
                    other_taxable_income=decimal_str_or_none(
                        data.sa100.income.other_uk_income.other_taxable_income_details.other_taxable_income
                    ),
                    tax_taken_off_other_taxable_income=decimal_str_or_none(
                        data.sa100.income.other_uk_income.other_taxable_income_details.tax_taken_off_other_taxable_income
                    ),
                )
                if data.sa100.income.other_uk_income.other_taxable_income_details
                else None,
                allowable_expenses=decimal_str_or_none(
                    data.sa100.income.other_uk_income.allowable_expenses
                ),
                deemed_income_or_benefits=decimal_str_or_none(
                    data.sa100.income.other_uk_income.deemed_income_or_benefits
                ),
                description_of_other_income=data.sa100.income.other_uk_income.description_of_other_income,
            )
            if data.sa100.income.other_uk_income
            else None,
        )
        if data.sa100.income
        else None,
        tax_reliefs=mtr.Mtr.Sa100.TaxReliefs(
            pensions=mtr.Mtr.Sa100.TaxReliefs.Pensions(
                payments_to_registered_pension_schemes=decimal_str_or_none(
                    data.sa100.tax_reliefs.pensions.payments_to_registered_pension_schemes
                ),
                one_off_registered_pension_schemes_payments=decimal_str_or_none(
                    data.sa100.tax_reliefs.pensions.one_off_registered_pension_schemes_payments
                ),
                retirement_annuity_contract_payments=decimal_str_or_none(
                    data.sa100.tax_reliefs.pensions.retirement_annuity_contract_payments
                ),
                employer_pension_scheme_payments=decimal_str_or_none(
                    data.sa100.tax_reliefs.pensions.employer_pension_scheme_payments
                ),
                non_ukoverseas_pension_scheme_payments=decimal_str_or_none(
                    data.sa100.tax_reliefs.pensions.non_uk_overseas_pension_scheme_payments
                ),
            )
            if data.sa100.tax_reliefs.pensions
            else None,
            charitable_giving=mtr.Mtr.Sa100.TaxReliefs.CharitableGiving(
                gift_aid_payments_made_in_year=decimal_str_or_none(
                    data.sa100.tax_reliefs.charitable_giving.gift_aid_payments_made_in_year
                ),
                one_off_gift_aid_payments=decimal_str_or_none(
                    data.sa100.tax_reliefs.charitable_giving.one_off_gift_aid_payments
                ),
                gift_aid_payments_carried_back_to_previous_year=decimal_str_or_none(
                    data.sa100.tax_reliefs.charitable_giving.gift_aid_payments_carried_back_to_previous_year
                ),
                gift_aid_payments_brought_back_from_later_year=decimal_str_or_none(
                    data.sa100.tax_reliefs.charitable_giving.gift_aid_payments_brought_back_from_later_year
                ),
                shares_gifted_to_charity=decimal_str_or_none(
                    data.sa100.tax_reliefs.charitable_giving.shares_gifted_to_charity
                ),
                land_and_buildings_gifted_to_charity=decimal_str_or_none(
                    data.sa100.tax_reliefs.charitable_giving.land_and_buildings_gifted_to_charity
                ),
            )
            if data.sa100.tax_reliefs.charitable_giving
            else None,
            blind_persons_allowance=mtr.Mtr.Sa100.TaxReliefs.BlindPersonsAllowance(
                blind_persons_allowance_details=mtr.Mtr.Sa100.TaxReliefs.BlindPersonsAllowance.BlindPersonsAllowanceDetails(
                    registered_blind=_yes(
                        data.sa100.tax_reliefs.blind_persons_allowance.blind_persons_allowance_details.registered_blind
                    ),
                    surplus_blind_persons_allowance_to_spouse=_yes(
                        data.sa100.tax_reliefs.blind_persons_allowance.blind_persons_allowance_details.surplus_blind_persons_allowance_to_spouse
                    ),
                    local_authority_name=data.sa100.tax_reliefs.blind_persons_allowance.blind_persons_allowance_details.local_authority_name,
                )
                if data.sa100.tax_reliefs.blind_persons_allowance.blind_persons_allowance_details
                else None,
                surplus_blind_persons_allowance_from_spouse=_yes(
                    data.sa100.tax_reliefs.blind_persons_allowance.surplus_blind_persons_allowance_from_spouse
                ),
            )
            if data.sa100.tax_reliefs.blind_persons_allowance
            else None,
        )
        if data.sa100.tax_reliefs
        else None,
        high_income_child_benefit_charge=mtr.Mtr.Sa100.HighIncomeChildBenefitCharge(
            amount_received=decimal_str_or_none(
                data.sa100.high_income_child_benefit_charge.amount_received
            ),
            number_of_children=data.sa100.high_income_child_benefit_charge.number_of_children,
            date_stopped_receiving_all_child_benefit_payments=xml_date_or_none(
                data.sa100.high_income_child_benefit_charge.date_stopped_receiving_all_child_benefit_payments
            ),
        )
        if data.sa100.high_income_child_benefit_charge
        else None,
        marriage_allowance=mtr.Mtr.Sa100.MarriageAllowance(
            spouse_first_name=data.sa100.marriage_allowance.spouse_first_name,
            spouse_last_name=data.sa100.marriage_allowance.spouse_last_name,
            spouse_nino=data.sa100.marriage_allowance.spouse_nino,
            spouse_date_of_birth=xml_date_or_none(
                data.sa100.marriage_allowance.spouse_date_of_birth
            ),
            date_of_marriage_or_civil_partnership=xml_date_or_none(
                data.sa100.marriage_allowance.date_of_marriage_or_civil_partnership
            ),
        )
        if data.sa100.marriage_allowance
        else None,
        marriage_allowance_transferred_in=_yes(
            data.sa100.marriage_allowance_transferred_in
        ),
        marriage_allowance_transferred_out=_yes(
            data.sa100.marriage_allowance_transferred_out
        ),
        finishing_your_tax_return=mtr.Mtr.Sa100.FinishingYourTaxReturn(
            tax_refunded_or_set_off=decimal_str_or_none(
                data.sa100.finishing_tax_return.tax_refunded_or_set_off
            ),
            not_paid_enough=mtr.Mtr.Sa100.FinishingYourTaxReturn.NotPaidEnough(
                tax_owed_not_to_be_coded_out=_yes(
                    data.sa100.finishing_tax_return.not_paid_enough.tax_owed_not_to_be_coded_out
                ),
                non_payeincome_not_to_be_coded_out=_yes(
                    data.sa100.finishing_tax_return.not_paid_enough.non_paye_income_not_to_be_coded_out
                ),
            )
            if data.sa100.finishing_tax_return.not_paid_enough
            else None,
            paid_too_much=mtr.Mtr.Sa100.FinishingYourTaxReturn.PaidTooMuch(
                payment_details=mtr.Mtr.Sa100.FinishingYourTaxReturn.PaidTooMuch.PaymentDetails(
                    bank_account_details=mtr.Mtr.Sa100.FinishingYourTaxReturn.PaidTooMuch.PaymentDetails.BankAccountDetails(
                        bank_or_building_society_name=data.sa100.finishing_tax_return.paid_too_much.payment_details.bank_account_details.bank_or_building_society_name,
                        account_holder_or_nominee_name=data.sa100.finishing_tax_return.paid_too_much.payment_details.bank_account_details.account_holder_or_nominee_name,
                        branch_sort_code=data.sa100.finishing_tax_return.paid_too_much.payment_details.bank_account_details.branch_sort_code,
                        account_number=data.sa100.finishing_tax_return.paid_too_much.payment_details.bank_account_details.account_number,
                        building_society_reference_number=data.sa100.finishing_tax_return.paid_too_much.payment_details.bank_account_details.building_society_reference_number,
                    )
                    if data.sa100.finishing_tax_return.paid_too_much.payment_details.bank_account_details
                    else None,
                    nominee_details=mtr.Mtr.Sa100.FinishingYourTaxReturn.PaidTooMuch.PaymentDetails.NomineeDetails(
                        nominee_name_given=_yes(
                            data.sa100.finishing_tax_return.paid_too_much.payment_details.nominee_details.nominee_name_given
                        ),
                        nominee_is_tax_adviser=_yes(
                            data.sa100.finishing_tax_return.paid_too_much.payment_details.nominee_details.nominee_is_tax_adviser
                        ),
                        nominee_address=mtr.MtrSaaddressStructure(
                            line=data.sa100.finishing_tax_return.paid_too_much.payment_details.nominee_details.nominee_address.line,
                            short_line=data.sa100.finishing_tax_return.paid_too_much.payment_details.nominee_details.nominee_address.short_line,
                            post_code=data.sa100.finishing_tax_return.paid_too_much.payment_details.nominee_details.nominee_address.post_code,
                        )
                        if data.sa100.finishing_tax_return.paid_too_much.payment_details.nominee_details.nominee_address
                        else None,
                    )
                    if data.sa100.finishing_tax_return.paid_too_much.payment_details.nominee_details
                    else None,
                )
                if data.sa100.finishing_tax_return.paid_too_much.payment_details
                else None,
                no_bank_or_building_society_account=_yes(
                    data.sa100.finishing_tax_return.paid_too_much.no_bank_or_building_society_account
                ),
            )
            if data.sa100.finishing_tax_return.paid_too_much
            else None,
            tax_adviser=mtr.Mtr.Sa100.FinishingYourTaxReturn.TaxAdviser(
                tax_adviser=data.sa100.finishing_tax_return.tax_adviser.tax_adviser,
                tax_adviser_phone_number=data.sa100.finishing_tax_return.tax_adviser.tax_adviser_phone_number,
                tax_adviser_address=mtr.MtrSaaddressStructure(
                    line=data.sa100.finishing_tax_return.tax_adviser.tax_adviser_address.line,
                    short_line=data.sa100.finishing_tax_return.tax_adviser.tax_adviser_address.short_line,
                    post_code=data.sa100.finishing_tax_return.tax_adviser.tax_adviser_address.post_code,
                )
                if data.sa100.finishing_tax_return.tax_adviser.tax_adviser_address
                else None,
                tax_advisers_reference=data.sa100.finishing_tax_return.tax_adviser.tax_advisers_reference,
            )
            if data.sa100.finishing_tax_return.tax_adviser
            else None,
            signing_your_form=mtr.Mtr.Sa100.FinishingYourTaxReturn.SigningYourForm(
                other_information_space=data.sa100.finishing_tax_return.signing_your_form.other_information_space,
                provisional_figures=_yes(
                    data.sa100.finishing_tax_return.signing_your_form.provisional_figures
                ),
                capacity_of_person_signing=data.sa100.finishing_tax_return.signing_your_form.capacity_of_person_signing,
                name_of_person_signed_for=data.sa100.finishing_tax_return.signing_your_form.name_of_person_signed_for,
                name_of_person_signing=data.sa100.finishing_tax_return.signing_your_form.name_of_person_signing,
                address_of_person_signing=mtr.MtrSaaddressStructure(
                    line=data.sa100.finishing_tax_return.signing_your_form.address_of_person_signing.line,
                    short_line=data.sa100.finishing_tax_return.signing_your_form.address_of_person_signing.short_line,
                    post_code=data.sa100.finishing_tax_return.signing_your_form.address_of_person_signing.post_code,
                )
                if data.sa100.finishing_tax_return.signing_your_form.address_of_person_signing
                else None,
            )
            if data.sa100.finishing_tax_return.signing_your_form
            else None,
        )
        if data.sa100.finishing_tax_return
        else None,
        chargeable_event_gains=decimal_str_or_none(data.sa100.chargeable_event_gains),
    )


def _get_sa110(data: d.MTR) -> mtr.Mtr.Sa110 | None:
    return (
        mtr.Mtr.Sa110(
            self_assessment=mtr.Mtr.Sa110.SelfAssessment(
                total_tax_etc_due=decimal_str_or_none(
                    data.sa110.self_assessment.total_tax_etc_due
                ),
                student_loan_repayment_due=decimal_str_or_none(
                    data.sa110.self_assessment.student_loan_repayment_due
                ),
                postgraduate_loan_repayment_due=decimal_str_or_none(
                    data.sa110.self_assessment.postgraduate_loan_repayment_due
                ),
                class4_nics_due=decimal_str_or_none(
                    data.sa110.self_assessment.class4_nics_due
                ),
                class2_nics_due=decimal_str_or_none(
                    data.sa110.self_assessment.class2_nics_due
                ),
                capital_gains_tax_due=decimal_str_or_none(
                    data.sa110.self_assessment.capital_gains_tax_due
                ),
                pension_charges_due=decimal_str_or_none(
                    data.sa110.self_assessment.pension_charges_due
                ),
            ),
            underpaid_tax=mtr.Mtr.Sa110.UnderpaidTax(
                underpaid_tax_for_earlier_years_included_in_code=decimal_str_or_none(
                    data.sa110.underpaid_tax.underpaid_tax_for_earlier_years_included_in_code
                ),
                underpaid_tax_for_year_included_in_future_code=decimal_str_or_none(
                    data.sa110.underpaid_tax.underpaid_tax_for_year_included_in_future_code
                ),
                outstanding_debt_coded_out_amount=decimal_str_or_none(
                    data.sa110.underpaid_tax.outstanding_debt_coded_out_amount
                ),
            ),
            payments_on_account=mtr.Mtr.Sa110.PaymentsOnAccount(
                claim_to_reduce_payments_on_account=_yes(
                    data.sa110.payments_on_account.claim_to_reduce_payments_on_account
                ),
                first_payment_on_account=decimal_str_or_none(
                    data.sa110.payments_on_account.first_payment_on_account
                ),
            )
            if data.sa110.payments_on_account
            else None,
            surplus_allowances=mtr.Mtr.Sa110.SurplusAllowances(
                surplus_blind_persons_allowance=decimal_str_or_none(
                    data.sa110.surplus_allowances.surplus_blind_persons_allowance
                ),
                surplus_married_couples_allowance=decimal_str_or_none(
                    data.sa110.surplus_allowances.surplus_married_couples_allowance
                ),
            )
            if data.sa110.surplus_allowances
            else None,
            adjustments_to_tax_due=mtr.Mtr.Sa110.AdjustmentsToTaxDue(
                increase_in_tax_from_adjustment_to_earlier_years=decimal_str_or_none(
                    data.sa110.adjustments_to_tax_due.increase_in_tax_from_adjustment_to_earlier_years
                ),
                decrease_in_tax_from_adjustment_to_earlier_years=decimal_str_or_none(
                    data.sa110.adjustments_to_tax_due.decrease_in_tax_from_adjustment_to_earlier_years
                ),
                next_years_repayment_claimed_now=decimal_str_or_none(
                    data.sa110.adjustments_to_tax_due.next_years_repayment_claimed_now
                ),
            )
            if data.sa110.adjustments_to_tax_due
            else None,
            any_other_information_space=data.sa110.any_other_information_space,
        )
        if data.sa110
        else None
    )


def _get_102(data: d.MTR) -> list[mtr.Mtr.Sa102]:
    return (
        [
            mtr.Mtr.Sa102(
                employment=mtr.Mtr.Sa102.Employment(
                    pay_from_employment=decimal_str_or_none(
                        sa102.employment.pay_from_employment
                    ),
                    payrolled_benefits=decimal_str_or_none(
                        sa102.employment.payrolled_benefits
                    ),
                    tax_taken_off_pay=decimal_str_or_none(
                        sa102.employment.tax_taken_off_pay
                    ),
                    total_class1_nicable_earnings=decimal_str_or_none(
                        sa102.employment.total_class1_nicable_earnings
                    ),
                    tips_and_other_payments=decimal_str_or_none(
                        sa102.employment.tips_and_other_payments
                    ),
                    employer_payereference=sa102.employment.employer_paye_reference,
                    employers_name=sa102.employment.employers_name,
                    company_director=_yes_no(sa102.employment.company_director),
                    date_ceased_being_adirector=xml_date_or_none(
                        sa102.employment.date_ceased_being_a_director
                    ),
                    close_company=_yes_no(sa102.employment.close_company),
                    close_company_name=sa102.employment.close_company_name,
                    company_registration_no=sa102.employment.company_registration_number,
                    close_company_dividend=decimal_str_or_none(
                        sa102.employment.close_company_dividend
                    ),
                    percentage_shareholding=sa102.employment.percentage_shareholding,
                    off_payroll_working=_yes(sa102.employment.off_payroll_working),
                ),
                benefits=mtr.Mtr.Sa102.Benefits(
                    company_cars_and_vans_benefit=decimal_str_or_none(
                        sa102.benefits.company_cars_and_vans_benefit
                    ),
                    fuel_for_cars_and_vans=decimal_str_or_none(
                        sa102.benefits.fuel_for_cars_and_vans
                    ),
                    private_medical_dental_insurance=decimal_str_or_none(
                        sa102.benefits.private_medical_dental_insurance
                    ),
                    vouchers_credit_cards_excess_mileage_allowance=decimal_str_or_none(
                        sa102.benefits.vouchers_credit_cards_excess_mileage_allowance
                    ),
                    goods_etc_provided_by_employer=decimal_str_or_none(
                        sa102.benefits.goods_etc_provided_by_employer
                    ),
                    accommodation_provided_by_employer=decimal_str_or_none(
                        sa102.benefits.accommodation_provided_by_employer
                    ),
                    other_benefits=decimal_str_or_none(sa102.benefits.other_benefits),
                    expenses_payments_received=decimal_str_or_none(
                        sa102.benefits.expenses_payments_received
                    ),
                )
                if sa102.benefits
                else None,
                expenses=mtr.Mtr.Sa102.Expenses(
                    business_travel_and_subsistence=decimal_str_or_none(
                        sa102.expenses.business_travel_and_subsistence
                    ),
                    fixed_expenses_deductions=decimal_str_or_none(
                        sa102.expenses.fixed_expenses_deductions
                    ),
                    professional_fees_and_subscriptions=decimal_str_or_none(
                        sa102.expenses.professional_fees_and_subscriptions
                    ),
                    other_expenses_and_capital_allowances=decimal_str_or_none(
                        sa102.expenses.other_expenses_and_capital_allowances
                    ),
                )
                if sa102.expenses
                else None,
            )
            for sa102 in data.sa102
        ]
        if data.sa102
        else []
    )


def _get_102m(data: d.MTR) -> list[mtr.Mtr.Sa102M]:
    return (
        [
            mtr.Mtr.Sa102M(
                income=mtr.Mtr.Sa102M.Income(
                    nature_of_post=sa102m.income.nature_of_post,
                    salary_or_stipend=decimal_str_or_none(
                        sa102m.income.salary_or_stipend
                    ),
                    payrolled_benefits=decimal_str_or_none(
                        sa102m.income.payrolled_benefits
                    ),
                    tax_taken_off_salary_stipend=decimal_str_or_none(
                        sa102m.income.tax_taken_off_salary_stipend
                    ),
                    total_class1_nicable_earnings=decimal_str_or_none(
                        sa102m.income.total_class1_nicable_earnings
                    ),
                    fees_and_offerings=decimal_str_or_none(
                        sa102m.income.fees_and_offerings
                    ),
                    vicarage_manse_expenses=decimal_str_or_none(
                        sa102m.income.vicarage_manse_expenses
                    ),
                    personal_expenses_etc_paid=decimal_str_or_none(
                        sa102m.income.personal_expenses_etc_paid
                    ),
                    excess_mileage_allowance_etc=decimal_str_or_none(
                        sa102m.income.excess_mileage_allowance_etc
                    ),
                    round_sum_expenses_and_rent_allowances=decimal_str_or_none(
                        sa102m.income.round_sum_expenses_and_rent_allowances
                    ),
                    tax_taken_off_round_sum_expenses=decimal_str_or_none(
                        sa102m.income.tax_taken_off_round_sum_expenses
                    ),
                    other_income_from_post=decimal_str_or_none(
                        sa102m.income.other_income_from_post
                    ),
                    tax_taken_off_other_income=decimal_str_or_none(
                        sa102m.income.tax_taken_off_other_income
                    ),
                    total_income_as_minister_of_religion=decimal_str_or_none(
                        sa102m.income.total_income_as_minister_of_religion
                    ),
                )
                if sa102m.income
                else None,
                benefits_and_expense_payments_to_you=mtr.Mtr.Sa102M.BenefitsAndExpensePaymentsToYou(
                    vicarage_services_benefit=decimal_str_or_none(
                        sa102m.benefits_and_expense_payments_to_you.vicarage_services_benefit
                    ),
                    car_provided=decimal_str_or_none(
                        sa102m.benefits_and_expense_payments_to_you.car_provided
                    ),
                    fuel_for_car_provided=decimal_str_or_none(
                        sa102m.benefits_and_expense_payments_to_you.fuel_for_car_provided
                    ),
                    interest_free_loans=decimal_str_or_none(
                        sa102m.benefits_and_expense_payments_to_you.interest_free_loans
                    ),
                    expenses_payments_made=decimal_str_or_none(
                        sa102m.benefits_and_expense_payments_to_you.expenses_payments_made
                    ),
                    other_benefits=decimal_str_or_none(
                        sa102m.benefits_and_expense_payments_to_you.other_benefits
                    ),
                    total_benefits_and_expenses=decimal_str_or_none(
                        sa102m.benefits_and_expense_payments_to_you.total_benefits_and_expenses
                    ),
                )
                if sa102m.benefits_and_expense_payments_to_you
                else None,
                income_benefits_and_expenses_received=decimal_str_or_none(
                    sa102m.income_benefits_and_expenses_received
                ),
                expenses_paid_by_you=mtr.Mtr.Sa102M.ExpensesPaidByYou(
                    travelling_expenses_and_capital_allowances=decimal_str_or_none(
                        sa102m.expenses_paid_by_you.travelling_expenses_and_capital_allowances
                    ),
                    maintenance_and_repairs_etc=decimal_str_or_none(
                        sa102m.expenses_paid_by_you.maintenance_and_repairs_etc
                    ),
                    rent_expenses=decimal_str_or_none(
                        sa102m.expenses_paid_by_you.rent_expenses
                    ),
                    other_expenses=decimal_str_or_none(
                        sa102m.expenses_paid_by_you.other_expenses
                    ),
                    total_expenses_paid=decimal_str_or_none(
                        sa102m.expenses_paid_by_you.total_expenses_paid
                    ),
                )
                if sa102m.expenses_paid_by_you
                else None,
                service_benefit_cap=mtr.Mtr.Sa102M.ServiceBenefitCap(
                    gross_income=decimal_str_or_none(
                        sa102m.service_benefit_cap.gross_income
                    ),
                    backpay_received_after_year_end=decimal_str_or_none(
                        sa102m.service_benefit_cap.backpay_received_after_year_end
                    ),
                    earlier_years_backpay_received_in_year=decimal_str_or_none(
                        sa102m.service_benefit_cap.earlier_years_backpay_received_in_year
                    ),
                    pension_scheme_payments=decimal_str_or_none(
                        sa102m.service_benefit_cap.pension_scheme_payments
                    ),
                    net_income=decimal_str_or_none(
                        sa102m.service_benefit_cap.net_income
                    ),
                    ten_percent_of_net_income=decimal_str_or_none(
                        sa102m.service_benefit_cap.ten_percent_of_net_income
                    ),
                    amount_paid_toward_service_benefit=decimal_str_or_none(
                        sa102m.service_benefit_cap.amount_paid_toward_service_benefit
                    ),
                    payments_made_and_service_benefit_received=decimal_str_or_none(
                        sa102m.service_benefit_cap.payments_made_and_service_benefit_received
                    ),
                    service_benefit_cap=decimal_str_or_none(
                        sa102m.service_benefit_cap.service_benefit_cap
                    ),
                )
                if sa102m.service_benefit_cap
                else None,
                other_income=mtr.Mtr.Sa102M.OtherIncome(
                    chaplaincy_and_other_income=decimal_str_or_none(
                        sa102m.other_income.chaplaincy_and_other_income
                    ),
                    tax_taken_of_other_income=decimal_str_or_none(
                        sa102m.other_income.tax_taken_of_other_income
                    ),
                )
                if sa102m.other_income
                else None,
                taxable_income=mtr.Mtr.Sa102M.TaxableIncome(
                    taxable_income_minus_expenses=decimal_str_or_none(
                        sa102m.taxable_income.taxable_income_minus_expenses
                    ),
                    total_tax_taken_off=decimal_str_or_none(
                        sa102m.taxable_income.total_tax_taken_off
                    ),
                )
                if sa102m.taxable_income
                else None,
            )
            for sa102m in data.sa102m
        ]
        if data.sa102m
        else []
    )


def _get_103s(data: d.MTR) -> list[mtr.Mtr.Sa103S]:
    return (
        [
            mtr.Mtr.Sa103S(
                business_details=mtr.Mtr.Sa103S.BusinessDetails(
                    business_description=sa103s.business_details.business_description,
                    business_address_postcode=sa103s.business_details.business_address_postcode
                    if sa103s.business_details.business_address_postcode
                    else None,
                    change_of_business_details=_yes(
                        sa103s.business_details.change_of_business_details
                    ),
                    foster_etc_carer_indicator=_yes(
                        sa103s.business_details.foster_etc_carer_indicator
                    ),
                    did_your_business_start=_yes_no(
                        sa103s.business_details.did_your_business_start
                    ),
                    date_business_started=xml_date_or_none(
                        sa103s.business_details.date_business_started
                    ),
                    did_your_business_cease=_yes_no(
                        sa103s.business_details.did_your_business_cease
                    ),
                    date_business_ceased=xml_date_or_none(
                        sa103s.business_details.date_business_ceased
                    ),
                    date_business_books_are_made_up_to=xml_date_or_none(
                        sa103s.business_details.date_business_books_are_made_up_to
                    ),
                    election_to_opt_out_of_cash_basis=_yes(
                        sa103s.business_details.election_to_opt_out_of_cash_basis
                    ),
                ),
                business_income=mtr.Mtr.Sa103S.BusinessIncome(
                    turnover=decimal_str_or_none(sa103s.business_income.turnover),
                    other_business_income=decimal_str_or_none(
                        sa103s.business_income.other_business_income
                    ),
                    trading_income_allowance=decimal_str_or_none(
                        sa103s.business_income.trading_income_allowance
                    ),
                )
                if sa103s.business_income
                else None,
                allowable_business_expenses=mtr.Mtr.Sa103S.AllowableBusinessExpenses(
                    cost_of_goods=decimal_str_or_none(
                        sa103s.allowable_business_expenses.cost_of_goods
                    ),
                    car_van_and_travel_expenses=decimal_str_or_none(
                        sa103s.allowable_business_expenses.car_van_and_travel_expenses
                    ),
                    wages_salaries_and_staff_costs=decimal_str_or_none(
                        sa103s.allowable_business_expenses.wages_salaries_and_staff_costs
                    ),
                    rent_and_other_property_costs=decimal_str_or_none(
                        sa103s.allowable_business_expenses.rent_and_other_property_costs
                    ),
                    repairs_and_maintenance_costs=decimal_str_or_none(
                        sa103s.allowable_business_expenses.repairs_and_maintenance_costs
                    ),
                    accountancy_and_legal_fees=decimal_str_or_none(
                        sa103s.allowable_business_expenses.accountancy_and_legal_fees
                    ),
                    interest_and_finance_charges=decimal_str_or_none(
                        sa103s.allowable_business_expenses.interest_and_finance_charges
                    ),
                    phone_and_other_office_costs=decimal_str_or_none(
                        sa103s.allowable_business_expenses.phone_and_other_office_costs
                    ),
                    other_allowable_business_expenses=decimal_str_or_none(
                        sa103s.allowable_business_expenses.other_allowable_business_expenses
                    ),
                    total_allowable_expenses=decimal_str_or_none(
                        sa103s.allowable_business_expenses.total_allowable_expenses
                    ),
                )
                if sa103s.allowable_business_expenses
                else None,
                net_profit_or_loss=decimal_str_or_none(sa103s.net_profit_or_loss),
                capital_allowances=mtr.Mtr.Sa103S.CapitalAllowances(
                    annual_investment_allowance=decimal_str_or_none(
                        sa103s.capital_allowances.annual_investment_allowance
                    ),
                    allowance_for_small_balance_of_unrelieved_expenditure=decimal_str_or_none(
                        sa103s.capital_allowances.allowance_for_small_balance_of_unrelieved_expenditure
                    ),
                    zero_emission_car_allowance=decimal_str_or_none(
                        sa103s.capital_allowances.zero_emission_car_allowance
                    ),
                    other_capital_allowances=decimal_str_or_none(
                        sa103s.capital_allowances.other_capital_allowances
                    ),
                    the_structures_and_buildings_allowance=decimal_str_or_none(
                        sa103s.capital_allowances.the_structures_and_buildings_allowance
                    ),
                    freeport_and_investment_zones_structures_and_buildings_allowance=decimal_str_or_none(
                        sa103s.capital_allowances.freeport_and_investment_zones_structures_and_buildings_allowance
                    ),
                    total_balancing_charges=decimal_str_or_none(
                        sa103s.capital_allowances.total_balancing_charges
                    ),
                )
                if sa103s.capital_allowances
                else None,
                taxable_profits=mtr.Mtr.Sa103S.TaxableProfits(
                    own_goods_and_services=decimal_str_or_none(
                        sa103s.taxable_profits.own_goods_and_services
                    ),
                    net_business_profit_for_tax=decimal_str_or_none(
                        sa103s.taxable_profits.net_business_profit_for_tax
                    ),
                    loss_brought_forward=decimal_str_or_none(
                        sa103s.taxable_profits.loss_brought_forward
                    ),
                    any_other_business_income=decimal_str_or_none(
                        sa103s.taxable_profits.any_other_business_income
                    ),
                )
                if sa103s.taxable_profits
                else None,
                profits_losses_nics_and_cis=mtr.Mtr.Sa103S.ProfitsLossesNicsAndCis(
                    total_taxable_business_profits=decimal_str_or_none(
                        sa103s.profits_losses_nics_and_cis.total_taxable_business_profits
                    ),
                    net_business_loss_for_tax=decimal_str_or_none(
                        sa103s.profits_losses_nics_and_cis.net_business_loss_for_tax
                    ),
                    loss_of_year_set_against_other_income=decimal_str_or_none(
                        sa103s.profits_losses_nics_and_cis.loss_of_year_set_against_other_income
                    ),
                    loss_to_carry_back=decimal_str_or_none(
                        sa103s.profits_losses_nics_and_cis.loss_to_carry_back
                    ),
                    total_loss_to_carry_forward=decimal_str_or_none(
                        sa103s.profits_losses_nics_and_cis.total_loss_to_carry_forward
                    ),
                    pay_class2_nicvoluntarily=_yes(
                        sa103s.profits_losses_nics_and_cis.pay_class2_nic_voluntarily
                    ),
                    class2_nicamount=decimal_str_or_none(
                        sa103s.profits_losses_nics_and_cis.class2_nic_amount
                    ),
                    class4_nicexempt=_yes(
                        sa103s.profits_losses_nics_and_cis.class4_nic_exempt
                    ),
                    sub_contractors_tax_deduction=decimal_str_or_none(
                        sa103s.profits_losses_nics_and_cis.sub_contractors_tax_deduction
                    ),
                )
                if sa103s.profits_losses_nics_and_cis
                else None,
            )
            for sa103s in data.sa103s
        ]
        if data.sa103s
        else []
    )


def _get_103f(data: d.MTR) -> list[mtr.Mtr.Sa103F]:
    return (
        [
            mtr.Mtr.Sa103F(
                business_details=mtr.Mtr.Sa103F.BusinessDetails(
                    business_name=sa103f.business_details.business_name,
                    business_description=sa103f.business_details.business_description,
                    business_address_first_line=sa103f.business_details.business_address_first_line,
                    business_address_postcode=sa103f.business_details.business_address_postcode,
                    change_of_business_details=_yes(
                        sa103f.business_details.change_of_business_details
                    ),
                    did_your_business_start=_yes_no(
                        sa103f.business_details.did_your_business_start
                    ),
                    date_business_started=xml_date_or_none(
                        sa103f.business_details.date_business_started
                    ),
                    did_your_business_cease=_yes_no(
                        sa103f.business_details.did_your_business_cease
                    ),
                    date_business_ceased=xml_date_or_none(
                        sa103f.business_details.date_business_ceased
                    ),
                    date_accounting_period_starts=xml_date_or_none(
                        sa103f.business_details.date_accounting_period_starts
                    ),
                    date_accounting_period_ends=xml_date_or_none(
                        sa103f.business_details.date_accounting_period_ends
                    ),
                    election_to_opt_out_of_cash_basis=_yes(
                        sa103f.business_details.election_to_opt_out_of_cash_basis
                    ),
                ),
                other_information=mtr.Mtr.Sa103F.OtherInformation(
                    special_arrangements_apply=_yes(
                        sa103f.other_information.special_arrangements_apply
                    ),
                    information_provided_last_year=_yes(
                        sa103f.other_information.information_provided_last_year
                    ),
                )
                if sa103f.other_information
                else None,
                business_income=mtr.Mtr.Sa103F.BusinessIncome(
                    turnover=decimal_str_or_none(sa103f.business_income.turnover),
                    other_business_income=decimal_str_or_none(
                        sa103f.business_income.other_business_income
                    ),
                    trading_income_allowance=decimal_str_or_none(
                        sa103f.business_income.trading_income_allowance
                    ),
                )
                if sa103f.business_income
                else None,
                business_expenses=mtr.Mtr.Sa103F.BusinessExpenses(
                    total_expenses=mtr.Mtr.Sa103F.BusinessExpenses.TotalExpenses(
                        cost_of_goods=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.cost_of_goods
                        ),
                        subcontractor_costs=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.subcontractor_costs
                        ),
                        wages_salaries_and_staff_costs=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.wages_salaries_and_staff_costs
                        ),
                        car_van_and_travel_expenses=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.car_van_and_travel_expenses
                        ),
                        rent_and_other_property_costs=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.rent_and_other_property_costs
                        ),
                        repairs_and_maintenance_costs=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.repairs_and_maintenance_costs
                        ),
                        phone_and_other_office_costs=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.phone_and_other_office_costs
                        ),
                        advertising_and_entertainment_costs=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.advertising_and_entertainment_costs
                        ),
                        bank_and_loan_interest=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.bank_and_loan_interest
                        ),
                        other_finance_charges=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.other_finance_charges
                        ),
                        debts_written_off=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.debts_written_off
                        ),
                        accountancy_and_legal_fees=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.accountancy_and_legal_fees
                        ),
                        depreciation_and_loss_profit_on_sale=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.depreciation_and_loss_profit_on_sale
                        ),
                        other_business_expenses=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.other_business_expenses
                        ),
                        total_expenses=decimal_str_or_none(
                            sa103f.business_expenses.total_expenses.total_expenses
                        ),
                    )
                    if sa103f.business_expenses.total_expenses
                    else None,
                    disallowable_expenses=mtr.Mtr.Sa103F.BusinessExpenses.DisallowableExpenses(
                        disallowable_cost_of_goods=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_cost_of_goods
                        ),
                        disallowable_subcontractor_costs=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_subcontractor_costs
                        ),
                        disallowable_staff_costs=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_staff_costs
                        ),
                        disallowable_car_and_travel_expenses=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_car_and_travel_expenses
                        ),
                        disallowable_rent_and_other_property_costs=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_rent_and_other_property_costs
                        ),
                        disallowable_repairs_and_maintenance_costs=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_repairs_and_maintenance_costs
                        ),
                        disallowable_phone_and_other_office_costs=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_phone_and_other_office_costs
                        ),
                        disallowable_advertising_and_entertainment_costs=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_advertising_and_entertainment_costs
                        ),
                        disallowable_bank_and_loan_interest=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_bank_and_loan_interest
                        ),
                        disallowable_other_finance_charges=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_other_finance_charges
                        ),
                        disallowable_debts_written_off=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_debts_written_off
                        ),
                        disallowable_accountancy_and_legal_fees=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_accountancy_and_legal_fees
                        ),
                        disallowable_depreciation_and_loss_profit_on_sale=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_depreciation_and_loss_profit_on_sale
                        ),
                        disallowable_other_business_expenses=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.disallowable_other_business_expenses
                        ),
                        total_disallowable_expenses=decimal_str_or_none(
                            sa103f.business_expenses.disallowable_expenses.total_disallowable_expenses
                        ),
                    )
                    if sa103f.business_expenses.disallowable_expenses
                    else None,
                )
                if sa103f.business_expenses
                else None,
                net_profit_loss=decimal_str_or_none(sa103f.net_profit_loss),
                capital_allowances=mtr.Mtr.Sa103F.CapitalAllowances(
                    annual_investment_allowance=decimal_str_or_none(
                        sa103f.capital_allowances.annual_investment_allowance
                    ),
                    annual_allowances_at_higher_rate=decimal_str_or_none(
                        sa103f.capital_allowances.annual_allowances_at_higher_rate
                    ),
                    annual_allowances_at_lower_rate=decimal_str_or_none(
                        sa103f.capital_allowances.annual_allowances_at_lower_rate
                    ),
                    zero_emission_goods_vehicle_allowance=decimal_str_or_none(
                        sa103f.capital_allowances.zero_emission_goods_vehicle_allowance
                    ),
                    zero_emission_car_allowance=decimal_str_or_none(
                        sa103f.capital_allowances.zero_emission_car_allowance
                    ),
                    the_structures_and_buildings_allowance=decimal_str_or_none(
                        sa103f.capital_allowances.the_structures_and_buildings_allowance
                    ),
                    freeport_and_investment_zones_structures_and_buildings_allowance=decimal_str_or_none(
                        sa103f.capital_allowances.freeport_and_investment_zones_structures_and_buildings_allowance
                    ),
                    electric_charge_point_allowance=decimal_str_or_none(
                        sa103f.capital_allowances.electric_charge_point_allowance
                    ),
                    other_capital_allowances=decimal_str_or_none(
                        sa103f.capital_allowances.other_capital_allowances
                    ),
                    balancing_allowances_on_sale_or_cessation=decimal_str_or_none(
                        sa103f.capital_allowances.balancing_allowances_on_sale_or_cessation
                    ),
                    total_capital_allowances=decimal_str_or_none(
                        sa103f.capital_allowances.total_capital_allowances
                    ),
                    total_balancing_charges=decimal_str_or_none(
                        sa103f.capital_allowances.total_balancing_charges
                    ),
                )
                if sa103f.capital_allowances
                else None,
                taxable_profit_or_loss=mtr.Mtr.Sa103F.TaxableProfitOrLoss(
                    own_goods_and_services=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.own_goods_and_services
                    ),
                    additions_to_net_profit_deductions_from_net_loss=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.additions_to_net_profit_deductions_from_net_loss
                    ),
                    non_taxable_business_income=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.non_taxable_business_income
                    ),
                    deductions_from_net_profit_additions_to_net_loss=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.deductions_from_net_profit_additions_to_net_loss
                    ),
                    net_business_profit_loss_for_tax=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.net_business_profit_loss_for_tax
                    ),
                    tax_year_adjustment=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.tax_year_adjustment
                    ),
                    change_of_accounting_practice_adjustment=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.change_of_accounting_practice_adjustment
                    ),
                    averaging_adjustment=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.averaging_adjustment
                    ),
                    adjusted_profit_for_the_year=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.adjusted_profit_for_the_year
                    ),
                    spread_transition_profit_treated_as_arising=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.spread_transition_profit_treated_as_arising
                    ),
                    loss_brought_forward_used_against_spread_transition_profit=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.loss_brought_forward_used_against_spread_transition_profit
                    ),
                    loss_brought_forward=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.loss_brought_forward
                    ),
                    any_other_business_income=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.any_other_business_income
                    ),
                    total_taxable_business_profits=decimal_str_or_none(
                        sa103f.taxable_profit_or_loss.total_taxable_business_profits
                    ),
                )
                if sa103f.taxable_profit_or_loss
                else None,
                losses=mtr.Mtr.Sa103F.Losses(
                    adjusted_loss_for_the_year=decimal_str_or_none(
                        sa103f.losses.adjusted_loss_for_the_year
                    ),
                    loss_of_year_set_against_other_income=decimal_str_or_none(
                        sa103f.losses.loss_of_year_set_against_other_income
                    ),
                    loss_to_carry_back=decimal_str_or_none(
                        sa103f.losses.loss_to_carry_back
                    ),
                    total_loss_to_carry_forward=decimal_str_or_none(
                        sa103f.losses.total_loss_to_carry_forward
                    ),
                )
                if sa103f.losses
                else None,
                tax_taken_off=mtr.Mtr.Sa103F.TaxTakenOff(
                    sub_contractors_tax_deduction=decimal_str_or_none(
                        sa103f.tax_taken_off.sub_contractors_tax_deduction
                    ),
                    other_tax_taken_off_trading_income=decimal_str_or_none(
                        sa103f.tax_taken_off.other_tax_taken_off_trading_income
                    ),
                )
                if sa103f.tax_taken_off
                else None,
                balance_sheet=mtr.Mtr.Sa103F.BalanceSheet(
                    assets=mtr.Mtr.Sa103F.BalanceSheet.Assets(
                        equipment_machinery_vehicles=decimal_str_or_none(
                            sa103f.balance_sheet.assets.equipment_machinery_vehicles
                        ),
                        other_fixed_assets=decimal_str_or_none(
                            sa103f.balance_sheet.assets.other_fixed_assets
                        ),
                        stock_and_work_in_progress=decimal_str_or_none(
                            sa103f.balance_sheet.assets.stock_and_work_in_progress
                        ),
                        trade_debtors=decimal_str_or_none(
                            sa103f.balance_sheet.assets.trade_debtors
                        ),
                        bank_etc_balances=decimal_str_or_none(
                            sa103f.balance_sheet.assets.bank_etc_balances
                        ),
                        cash_in_hand=decimal_str_or_none(
                            sa103f.balance_sheet.assets.cash_in_hand
                        ),
                        other_current_assets=decimal_str_or_none(
                            sa103f.balance_sheet.assets.other_current_assets
                        ),
                        total_business_assets=decimal_str_or_none(
                            sa103f.balance_sheet.assets.total_business_assets
                        ),
                    )
                    if sa103f.balance_sheet.assets
                    else None,
                    liabilities=mtr.Mtr.Sa103F.BalanceSheet.Liabilities(
                        trade_creditors=decimal_str_or_none(
                            sa103f.balance_sheet.liabilities.trade_creditors
                        ),
                        loans_and_overdrafts=decimal_str_or_none(
                            sa103f.balance_sheet.liabilities.loans_and_overdrafts
                        ),
                        other_liabilities=decimal_str_or_none(
                            sa103f.balance_sheet.liabilities.other_liabilities
                        ),
                    )
                    if sa103f.balance_sheet.liabilities
                    else None,
                    net_business_assets=decimal_str_or_none(
                        sa103f.balance_sheet.net_business_assets
                    ),
                    capital_account=mtr.Mtr.Sa103F.BalanceSheet.CapitalAccount(
                        capital_account_balance_at_start=decimal_str_or_none(
                            sa103f.balance_sheet.capital_account.capital_account_balance_at_start
                        ),
                        net_profit_or_loss=decimal_str_or_none(
                            sa103f.balance_sheet.capital_account.net_profit_or_loss
                        ),
                        capital_introduced=decimal_str_or_none(
                            sa103f.balance_sheet.capital_account.capital_introduced
                        ),
                        drawings=decimal_str_or_none(
                            sa103f.balance_sheet.capital_account.drawings
                        ),
                        capital_account_balance_at_end=decimal_str_or_none(
                            sa103f.balance_sheet.capital_account.capital_account_balance_at_end
                        ),
                    )
                    if sa103f.balance_sheet.capital_account
                    else None,
                )
                if sa103f.balance_sheet
                else None,
                nics=mtr.Mtr.Sa103F.Nics(
                    pay_class2_nicvoluntarily=_yes(
                        sa103f.nics.pay_class2_nic_voluntarily
                    ),
                    class2_nicamount=decimal_str_or_none(sa103f.nics.class2_nic_amount),
                    class4_nicexempt=_yes(sa103f.nics.class4_nic_exempt),
                    adjustment_to_class4_nicprofits=decimal_str_or_none(
                        sa103f.nics.adjustment_to_class4_nic_profits
                    ),
                )
                if sa103f.nics
                else None,
                other_information_space=decimal_str_or_none(
                    sa103f.other_information_space
                ),
            )
            for sa103f in data.sa103f
        ]
        if data.sa103f
        else []
    )


def _get_104s(data: d.MTR) -> list[mtr.Mtr.Sa104S]:
    return (
        [
            mtr.Mtr.Sa104S(
                partnership_details=mtr.Mtr.Sa104S.PartnershipDetails(
                    partnership_reference_number=sa104s.partnership_details.partnership_reference_number,
                    partnership_description=sa104s.partnership_details.partnership_description,
                    did_you_join_the_partnership=_yes_no(
                        sa104s.partnership_details.did_you_join_the_partnership
                    ),
                    date_joined_partnership=xml_date_or_none(
                        sa104s.partnership_details.date_joined_partnership
                    ),
                    did_you_leave_the_partnership=_yes_no(
                        sa104s.partnership_details.did_you_leave_the_partnership
                    ),
                    date_left_partnership=xml_date_or_none(
                        sa104s.partnership_details.date_left_partnership
                    ),
                ),
                share_of_partnership_trading_or_professional_profits=mtr.Mtr.Sa104S.ShareOfPartnershipTradingOrProfessionalProfits(
                    share_of_partnership_profit_or_loss=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_profits.share_of_partnership_profit_or_loss
                    ),
                    tax_year_adjustment=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_profits.tax_year_adjustment
                    ),
                    change_of_accounting_practice_adjustment=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_profits.change_of_accounting_practice_adjustment
                    ),
                    averaging_adjustment=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_profits.averaging_adjustment
                    ),
                    foreign_tax_claimed_as_deduction=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_profits.foreign_tax_claimed_as_deduction
                    ),
                    adjusted_profit_for_year=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_profits.adjusted_profit_for_year
                    ),
                    losses_brought_forward=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_profits.losses_brought_forward
                    ),
                    taxable_profits_after_losses=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_profits.taxable_profits_after_losses
                    ),
                    other_business_income=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_profits.other_business_income
                    ),
                    total_taxable_business_profits=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_profits.total_taxable_business_profits
                    ),
                )
                if sa104s.share_of_partnership_trading_or_professional_profits
                else None,
                share_of_partnership_trading_or_professional_losses=mtr.Mtr.Sa104S.ShareOfPartnershipTradingOrProfessionalLosses(
                    adjusted_loss_for_year=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_losses.adjusted_loss_for_year
                    ),
                    loss_set_off_against_other_income=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_losses.loss_set_off_against_other_income
                    ),
                    loss_to_be_carried_back=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_losses.loss_to_be_carried_back
                    ),
                    total_loss_to_carry_forward=decimal_str_or_none(
                        sa104s.share_of_partnership_trading_or_professional_losses.total_loss_to_carry_forward
                    ),
                )
                if sa104s.share_of_partnership_trading_or_professional_losses
                else None,
                nics=mtr.Mtr.Sa104S.Nics(
                    pay_class2_nicvoluntarily=_yes(
                        sa104s.nics.pay_class2_nic_voluntarily
                    ),
                    class2_nicamount=decimal_str_or_none(sa104s.nics.class2_nic_amount),
                    class4_nicexempt=_yes(sa104s.nics.class4_nic_exempt),
                    adjustment_to_class4_nicprofits=decimal_str_or_none(
                        sa104s.nics.adjustment_to_class4_nic_profits
                    ),
                )
                if sa104s.nics
                else None,
                share_of_untaxed_interest_etc=decimal_str_or_none(
                    sa104s.share_of_untaxed_interest_etc
                ),
                share_of_partnerships_tax_paid=mtr.Mtr.Sa104S.ShareOfPartnershipsTaxPaid(
                    share_of_tax_taken_off_by_contractors=decimal_str_or_none(
                        sa104s.share_of_partnerships_tax_paid.share_of_tax_taken_off_by_contractors
                    ),
                    share_of_tax_taken_off_trading_income=decimal_str_or_none(
                        sa104s.share_of_partnerships_tax_paid.share_of_tax_taken_off_trading_income
                    ),
                )
                if sa104s.share_of_partnerships_tax_paid
                else None,
                any_other_information_space=sa104s.any_other_information_space,
            )
            for sa104s in data.sa104s
        ]
        if data.sa104s
        else []
    )


def _get_104f(data: d.MTR) -> list[mtr.Mtr.Sa104F]:
    return (
        [
            mtr.Mtr.Sa104F(
                partnership_details=mtr.Mtr.Sa104F.PartnershipDetails(
                    partnership_reference_number=sa104f.partnership_details.partnership_reference_number,
                    partnership_description=sa104f.partnership_details.partnership_description,
                    did_you_join_the_partnership=_yes_no(
                        sa104f.partnership_details.did_you_join_the_partnership
                    ),
                    date_joined_partnership=xml_date_or_none(
                        sa104f.partnership_details.date_joined_partnership
                    ),
                    did_you_leave_the_partnership=_yes_no(
                        sa104f.partnership_details.did_you_leave_the_partnership
                    ),
                    date_left_partnership=xml_date_or_none(
                        sa104f.partnership_details.date_left_partnership
                    ),
                ),
                share_of_profits=mtr.Mtr.Sa104F.ShareOfProfits(
                    share_of_partnership_profit_or_loss=decimal_str_or_none(
                        sa104f.share_of_profits.share_of_partnership_profit_or_loss
                    ),
                    tax_year_adjustment=decimal_str_or_none(
                        sa104f.share_of_profits.tax_year_adjustment
                    ),
                    change_of_accounting_practice_adjustment=decimal_str_or_none(
                        sa104f.share_of_profits.change_of_accounting_practice_adjustment
                    ),
                    averaging_adjustment=decimal_str_or_none(
                        sa104f.share_of_profits.averaging_adjustment
                    ),
                    foreign_tax_claimed_as_deduction=decimal_str_or_none(
                        sa104f.share_of_profits.foreign_tax_claimed_as_deduction
                    ),
                    adjusted_profit_for_year=decimal_str_or_none(
                        sa104f.share_of_profits.adjusted_profit_for_year
                    ),
                    spread_transition_profit_treated_as_arising=decimal_str_or_none(
                        sa104f.share_of_profits.spread_transition_profit_treated_as_arising
                    ),
                    loss_brought_forward_used_against_spread_transition_profit=decimal_str_or_none(
                        sa104f.share_of_profits.loss_brought_forward_used_against_spread_transition_profit
                    ),
                    losses_brought_forward=decimal_str_or_none(
                        sa104f.share_of_profits.losses_brought_forward
                    ),
                    taxable_profits_after_losses=decimal_str_or_none(
                        sa104f.share_of_profits.taxable_profits_after_losses
                    ),
                    other_business_income=decimal_str_or_none(
                        sa104f.share_of_profits.other_business_income
                    ),
                    total_taxable_business_profits=decimal_str_or_none(
                        sa104f.share_of_profits.total_taxable_business_profits
                    ),
                )
                if sa104f.share_of_profits
                else None,
                share_of_losses=mtr.Mtr.Sa104F.ShareOfLosses(
                    adjusted_loss_for_year=decimal_str_or_none(
                        sa104f.share_of_losses.adjusted_loss_for_year
                    ),
                    loss_set_off_against_other_income=decimal_str_or_none(
                        sa104f.share_of_losses.loss_set_off_against_other_income
                    ),
                    loss_to_be_carried_back=decimal_str_or_none(
                        sa104f.share_of_losses.loss_to_be_carried_back
                    ),
                    total_loss_to_carry_forward=decimal_str_or_none(
                        sa104f.share_of_losses.total_loss_to_carry_forward
                    ),
                )
                if sa104f.share_of_losses
                else None,
                nics=mtr.Mtr.Sa104F.Nics(
                    pay_class2_nicvoluntarily=_yes(
                        sa104f.nics.pay_class2_nic_voluntarily
                    ),
                    class2_nicamount=decimal_str_or_none(sa104f.nics.class2_nic_amount),
                    class4_nicexempt=_yes(sa104f.nics.class4_nic_exempt),
                    adjustment_to_class4_nicprofits=decimal_str_or_none(
                        sa104f.nics.adjustment_to_class4_nic_profits
                    ),
                )
                if sa104f.nics
                else None,
                share_of_untaxed_income=mtr.Mtr.Sa104F.ShareOfUntaxedIncome(
                    savings_income=mtr.Mtr.Sa104F.ShareOfUntaxedIncome.SavingsIncome(
                        ukuntaxed_savings_income_share=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.savings_income.uk_untaxed_savings_income_share
                        ),
                        ukuntaxed_savings_adjustment=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.savings_income.uk_untaxed_savings_adjustment
                        ),
                        adjusted_uksavings_income=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.savings_income.adjusted_uk_savings_income
                        ),
                        foreign_income=mtr.Mtr.Sa104F.ShareOfUntaxedIncome.SavingsIncome.ForeignIncome(
                            foreign_untaxed_savings_income_share=decimal_str_or_none(
                                sa104f.share_of_untaxed_income.savings_income.foreign_income.foreign_untaxed_savings_income_share
                            ),
                            foreign_untaxed_savings_adjustment=decimal_str_or_none(
                                sa104f.share_of_untaxed_income.savings_income.foreign_income.foreign_untaxed_savings_adjustment
                            ),
                            total_foreign_tax_taken_off=decimal_str_or_none(
                                sa104f.share_of_untaxed_income.savings_income.foreign_income.total_foreign_tax_taken_off
                            ),
                        )
                        if sa104f.share_of_untaxed_income.savings_income.foreign_income
                        else None,
                        total_untaxed_savings_income=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.savings_income.total_untaxed_savings_income
                        ),
                    )
                    if sa104f.share_of_untaxed_income.savings_income
                    else None,
                    ukproperty_income=mtr.Mtr.Sa104F.ShareOfUntaxedIncome.UkpropertyIncome(
                        ukproperty_profit_loss_share=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.uk_property_income.uk_property_profit_loss_share
                        ),
                        ukproperty_income_adjustment=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.uk_property_income.uk_property_income_adjustment
                        ),
                        loss_brought_forward=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.uk_property_income.loss_brought_forward
                        ),
                        loss_for_year_set_off_against_other_income=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.uk_property_income.loss_for_year_set_off_against_other_income
                        ),
                        loss_to_be_carried_forward=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.uk_property_income.loss_to_be_carried_forward
                        ),
                    )
                    if sa104f.share_of_untaxed_income.uk_property_income
                    else None,
                    other_untaxed_ukincome=mtr.Mtr.Sa104F.ShareOfUntaxedIncome.OtherUntaxedUkincome(
                        other_untaxed_ukincome_share=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.other_untaxed_uk_income.other_untaxed_uk_income_share
                        ),
                        other_untaxed_ukincome_adjustment=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.other_untaxed_uk_income.other_untaxed_uk_income_adjustment
                        ),
                        loss_brought_forward=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.other_untaxed_uk_income.loss_brought_forward
                        ),
                        taxable_profit=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.other_untaxed_uk_income.taxable_profit
                        ),
                        other_untaxed_ukincome=mtr.Mtr.Sa104F.ShareOfUntaxedIncome.OtherUntaxedUkincome.OtherUntaxedUkincomeInner(
                            share_of_loss_from_other_untaxed_ukincome=decimal_str_or_none(
                                sa104f.share_of_untaxed_income.other_untaxed_uk_income.other_untaxed_uk_income.share_of_loss_from_other_untaxed_uk_income
                            ),
                            adjustment_to_loss=decimal_str_or_none(
                                sa104f.share_of_untaxed_income.other_untaxed_uk_income.other_untaxed_uk_income.adjustment_to_loss
                            ),
                        )
                        if sa104f.share_of_untaxed_income.other_untaxed_uk_income.other_untaxed_uk_income
                        else None,
                        total_loss_to_carry_forward=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.other_untaxed_uk_income.total_loss_to_carry_forward
                        ),
                    )
                    if sa104f.share_of_untaxed_income.other_untaxed_uk_income
                    else None,
                    offshore_funds_income=mtr.Mtr.Sa104F.ShareOfUntaxedIncome.OffshoreFundsIncome(
                        offshore_funds_income_share=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.offshore_funds_income.offshore_funds_income_share
                        ),
                        offshore_funds_income_adjustment=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.offshore_funds_income.offshore_funds_income_adjustment
                        ),
                        foreign_tax_taken_off=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.offshore_funds_income.foreign_tax_taken_off
                        ),
                        taxable_income_after_adjustment_and_foreign_tax=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.offshore_funds_income.taxable_income_after_adjustment_and_foreign_tax
                        ),
                    )
                    if sa104f.share_of_untaxed_income.offshore_funds_income
                    else None,
                    other_untaxed_foreign_income=mtr.Mtr.Sa104F.ShareOfUntaxedIncome.OtherUntaxedForeignIncome(
                        other_untaxed_foreign_income_share=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.other_untaxed_foreign_income.other_untaxed_foreign_income_share
                        ),
                        other_untaxed_foreign_income_adjustment=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.other_untaxed_foreign_income.other_untaxed_foreign_income_adjustment
                        ),
                        total_foreign_tax_taken_off=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.other_untaxed_foreign_income.total_foreign_tax_taken_off
                        ),
                        taxable_profit=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.other_untaxed_foreign_income.adjusted_foreign_income
                        ),
                        foreign_losses=mtr.Mtr.Sa104F.ShareOfUntaxedIncome.OtherUntaxedForeignIncome.ForeignLosses(
                            share_of_loss_from_other_untaxed_foreign_income=decimal_str_or_none(
                                sa104f.share_of_untaxed_income.other_untaxed_foreign_income.foreign_losses.foreign_losses_brought_forward
                            ),
                            adjustment_to_loss=decimal_str_or_none(
                                sa104f.share_of_untaxed_income.other_untaxed_foreign_income.foreign_losses.foreign_losses_for_year_set_off_against_other_income
                            ),
                            total_loss_to_carry_forward=decimal_str_or_none(
                                sa104f.share_of_untaxed_income.other_untaxed_foreign_income.foreign_losses.foreign_losses_to_be_carried_forward
                            ),
                        )
                        if sa104f.share_of_untaxed_income.other_untaxed_foreign_income.foreign_losses
                        else None,
                        residential_finance_costs=decimal_str_or_none(
                            sa104f.share_of_untaxed_income.other_untaxed_foreign_income.adjusted_foreign_income
                        ),
                    )
                    if sa104f.share_of_untaxed_income.other_untaxed_foreign_income
                    else None,
                    total_untaxed_income_share=decimal_str_or_none(
                        sa104f.share_of_untaxed_income.total_untaxed_income_share
                    ),
                )
                if sa104f.share_of_untaxed_income
                else None,
                share_of_partnership_income=mtr.Mtr.Sa104F.ShareOfPartnershipIncome(
                    share_of_dividend_income=mtr.Mtr.Sa104F.ShareOfPartnershipIncome.ShareOfDividendIncome(
                        dividend_income=decimal_str_or_none(
                            sa104f.share_of_partnership_income.share_of_dividend_income.dividend_income
                        ),
                        total_foreign_tax_taken_off=decimal_str_or_none(
                            sa104f.share_of_partnership_income.share_of_dividend_income.total_foreign_tax_taken_off
                        ),
                        total_dividend_income=decimal_str_or_none(
                            sa104f.share_of_partnership_income.share_of_dividend_income.total_dividend_income
                        ),
                    )
                    if sa104f.share_of_partnership_income.share_of_dividend_income
                    else None,
                    share_of_taxed_income_taxable_at20_percent=mtr.Mtr.Sa104F.ShareOfPartnershipIncome.ShareOfTaxedIncomeTaxableAt20Percent(
                        share_of_taxed_income=decimal_str_or_none(
                            sa104f.share_of_partnership_income.share_of_taxed_income_taxable_at_20_percent.share_of_taxed_income
                        ),
                        total_foreign_tax_taken_off=decimal_str_or_none(
                            sa104f.share_of_partnership_income.share_of_taxed_income_taxable_at_20_percent.total_foreign_tax_taken_off
                        ),
                        taxed_income_taxable_at20_percent=decimal_str_or_none(
                            sa104f.share_of_partnership_income.share_of_taxed_income_taxable_at_20_percent.taxed_income_taxable_at_20_percent
                        ),
                    )
                    if sa104f.share_of_partnership_income.share_of_taxed_income_taxable_at_20_percent
                    else None,
                    share_of_other_taxed_income=mtr.Mtr.Sa104F.ShareOfPartnershipIncome.ShareOfOtherTaxedIncome(
                        share_of_taxed_income=decimal_str_or_none(
                            sa104f.share_of_partnership_income.share_of_other_taxed_income.share_of_taxed_income
                        ),
                        total_foreign_tax_taken_off=decimal_str_or_none(
                            sa104f.share_of_partnership_income.share_of_other_taxed_income.total_foreign_tax_taken_off
                        ),
                    )
                    if sa104f.share_of_partnership_income.share_of_other_taxed_income
                    else None,
                    share_of_total_taxed_and_untaxed_income=decimal_str_or_none(
                        sa104f.share_of_partnership_income.share_of_total_taxed_and_untaxed_income
                    ),
                )
                if sa104f.share_of_partnership_income
                else None,
                share_of_partnership_tax_payed=mtr.Mtr.Sa104F.ShareOfPartnershipTaxPayed(
                    share_of_income_tax_taken_off_partnership_income=decimal_str_or_none(
                        sa104f.share_of_partnership_tax_paid.share_of_income_tax_taken_off_partnership_income
                    ),
                    share_of_tax_taken_off_by_contractors=decimal_str_or_none(
                        sa104f.share_of_partnership_tax_paid.share_of_tax_taken_off_by_contractors
                    ),
                )
                if sa104f.share_of_partnership_tax_paid
                else None,
            )
            for sa104f in data.sa104f
        ]
        if data.sa104f
        else []
    )


def _get_105(data: d.MTR) -> mtr.Mtr.Sa105 | None:
    sa105 = data.sa105
    return (
        mtr.Mtr.Sa105(
            ukproperty_details=mtr.Mtr.Sa105.UkpropertyDetails(
                number_of_properties=sa105.uk_property_details.number_of_properties,
                property_income_ceased_in_year=_yes(
                    sa105.uk_property_details.property_income_ceased_in_year
                ),
                income_from_property_let_jointly=_yes(
                    sa105.uk_property_details.income_from_property_let_jointly
                ),
                rent_aroom_relief_claim=_yes(
                    sa105.uk_property_details.rent_a_room_relief_claim
                ),
            )
            if sa105.uk_property_details
            else None,
            property_income_and_expenses=mtr.Mtr.Sa105.PropertyIncomeAndExpenses(
                total_rents_and_other_income_from_property=decimal_str_or_none(
                    sa105.property_income_and_expenses.total_rents_and_other_income_from_property
                ),
                property_income_allowance=decimal_str_or_none(
                    sa105.property_income_and_expenses.property_income_allowance
                ),
                traditional_accounting=_yes(
                    sa105.property_income_and_expenses.traditional_accounting
                ),
                tax_taken_off_any_income=decimal_str_or_none(
                    sa105.property_income_and_expenses.tax_taken_off_any_income
                ),
                premiums_for_grant_of_alease=decimal_str_or_none(
                    sa105.property_income_and_expenses.premiums_for_grant_of_alease
                ),
                reverse_premiums_and_inducements=decimal_str_or_none(
                    sa105.property_income_and_expenses.reverse_premiums_and_inducements
                ),
                rent_rates_insurance_and_ground_rents=decimal_str_or_none(
                    sa105.property_income_and_expenses.rent_rates_insurance_and_ground_rents
                ),
                repairs_and_maintenance=decimal_str_or_none(
                    sa105.property_income_and_expenses.repairs_and_maintenance
                ),
                allowable_interest_and_other_financial_charges=decimal_str_or_none(
                    sa105.property_income_and_expenses.allowable_interest_and_other_financial_charges
                ),
                legal_management_and_professional_fees=decimal_str_or_none(
                    sa105.property_income_and_expenses.legal_management_and_professional_fees
                ),
                costs_of_services_provided=decimal_str_or_none(
                    sa105.property_income_and_expenses.costs_of_services_provided
                ),
                other_property_expenses=decimal_str_or_none(
                    sa105.property_income_and_expenses.other_property_expenses
                ),
            )
            if sa105.property_income_and_expenses
            else None,
            taxable_profit_or_loss=mtr.Mtr.Sa105.TaxableProfitOrLoss(
                private_use_adjustment=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.private_use_adjustment
                ),
                balancing_charges=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.balancing_charges
                ),
                annual_investment_allowance=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.annual_investment_allowance
                ),
                the_structures_and_buildings_allowance=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.the_structures_and_buildings_allowance
                ),
                electric_charge_point_allowance=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.electric_charge_point_allowance
                ),
                freeport_and_investment_zones_structures_and_buildings_allowance=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.freeport_and_investment_zones_structures_and_buildings_allowance
                ),
                zero_emission_car_allowance=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.zero_emission_car_allowance
                ),
                enhanced_capital_allowances=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.enhanced_capital_allowances
                ),
                costs_of_replacing_domestic_items=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.costs_of_replacing_domestic_items
                ),
                rent_aroom_exempt_amount=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.rent_a_room_exempt_amount
                ),
                adjusted_profit_for_the_year=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.adjusted_profit_for_the_year
                ),
                loss_brought_forward=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.loss_brought_forward
                ),
                taxable_profit_for_the_year=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.taxable_profit_for_the_year
                ),
                adjusted_loss_for_the_year=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.adjusted_loss_for_the_year
                ),
                loss_set_off_against_total_income_of_the_year=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.loss_set_off_against_total_income_of_the_year
                ),
                loss_to_carry_forward=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.loss_to_carry_forward
                ),
                residential_finance_costs=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.residential_finance_costs
                ),
                unused_residential_finance_costs_brought_forward=decimal_str_or_none(
                    sa105.taxable_profit_or_loss.unused_residential_finance_costs_brought_forward
                ),
            )
            if sa105.taxable_profit_or_loss
            else None,
        )
        if sa105
        else None
    )


def _get_106(data: d.MTR) -> mtr.Mtr.Sa106 | None:
    sa106 = data.sa106
    return (
        mtr.Mtr.Sa106(
            unremittable_income=_yes(sa106.unremittable_income),
            foreign_tax_credit_relief=decimal_str_or_none(
                sa106.foreign_tax_credit_relief
            ),
            overseas_savings=mtr.Mtr.Sa106.OverseasSavings(
                income_source=[
                    mtr.Mtr.Sa106.OverseasSavings.IncomeSource(
                        country_code=income_source.country_code,
                        income_before_tax=decimal_str_or_none(
                            income_source.income_before_tax
                        ),
                        foreign_tax=decimal_str_or_none(income_source.foreign_tax),
                        special_withholding_tax=decimal_str_or_none(
                            income_source.special_withholding_tax
                        ),
                        claim_to_ftcr=_yes(income_source.claim_to_ftcr),
                        taxable_amount_on_interest_and_other_savings=decimal_str_or_none(
                            income_source.taxable_amount_on_interest_and_other_savings
                        ),
                    )
                    for income_source in sa106.overseas_savings.income_source
                ]
                if sa106.overseas_savings.income_source
                else [],
                totals=mtr.MtrSa106SourceOfForeignIncomeTotals(
                    swtor_uktax=decimal_str_or_none(
                        sa106.overseas_savings.totals.special_withholding_tax
                    ),
                    taxable_amount=decimal_str_or_none(
                        sa106.overseas_savings.totals.taxable_amount
                    ),
                )
                if sa106.overseas_savings.totals
                else None,
            )
            if sa106.overseas_savings
            else None,
            foreign_companies=mtr.Mtr.Sa106.ForeignCompanies(
                income_source=[
                    mtr.Mtr.Sa106.ForeignCompanies.IncomeSource(
                        country_code=income_source.country_code,
                        income_before_tax=decimal_str_or_none(
                            income_source.income_before_tax
                        ),
                        foreign_tax=decimal_str_or_none(income_source.foreign_tax),
                        special_withholding_tax=decimal_str_or_none(
                            income_source.special_withholding_tax
                        ),
                        claim_to_ftcr=_yes(income_source.claim_to_ftcr),
                        taxable_amount_on_interest_and_other_savings=decimal_str_or_none(
                            income_source.taxable_amount
                        ),
                    )
                    for income_source in sa106.foreign_companies.income_source
                ]
                if sa106.foreign_companies.income_source
                else [],
                totals=mtr.MtrSa106SourceOfForeignIncomeTotals(
                    swtor_uktax=decimal_str_or_none(
                        sa106.foreign_companies.totals.special_withholding_tax
                    ),
                    taxable_amount=decimal_str_or_none(
                        sa106.foreign_companies.totals.taxable_amount
                    ),
                )
                if sa106.foreign_companies.totals
                else None,
            )
            if sa106.foreign_companies
            else None,
            remitted_foreign_dividends=mtr.Mtr.Sa106.RemittedForeignDividends(
                income_source=[
                    mtr.Mtr.Sa106.RemittedForeignDividends.IncomeSource(
                        country_code=income_source.country_code,
                        income_before_tax=decimal_str_or_none(
                            income_source.income_before_tax
                        ),
                        foreign_tax=decimal_str_or_none(income_source.foreign_tax),
                        special_withholding_tax=decimal_str_or_none(
                            income_source.special_withholding_tax
                        ),
                        claim_to_ftcr=_yes(income_source.claim_to_ftcr),
                        taxable_amount=decimal_str_or_none(
                            income_source.taxable_amount
                        ),
                    )
                    for income_source in sa106.remitted_foreign_dividends.income_source
                ]
                if sa106.remitted_foreign_dividends.income_source
                else [],
                totals=mtr.MtrSa106SourceOfForeignIncomeTotalsRemitted(
                    swtor_uktax=decimal_str_or_none(
                        sa106.remitted_foreign_dividends.totals.special_withholding_tax
                    ),
                    taxable_amount=decimal_str_or_none(
                        sa106.remitted_foreign_dividends.totals.taxable_amount
                    ),
                )
                if sa106.remitted_foreign_dividends.totals
                else None,
                amount_subject_to_dividend_tax_credit=decimal_str_or_none(
                    sa106.remitted_foreign_dividends.amount_subject_to_dividend_tax_credit
                ),
            )
            if sa106.remitted_foreign_dividends
            else None,
            overseas_pensions=mtr.Mtr.Sa106.OverseasPensions(
                income_source=[
                    mtr.Mtr.Sa106.OverseasPensions.IncomeSource(
                        country_code=income_source.country_code,
                        income_before_tax=decimal_str_or_none(
                            income_source.income_before_tax
                        ),
                        foreign_tax=decimal_str_or_none(income_source.foreign_tax),
                        special_withholding_tax=decimal_str_or_none(
                            income_source.special_withholding_tax
                        ),
                        claim_to_ftcr=_yes(income_source.claim_to_ftcr),
                        taxable_amount_on_interest_and_other_savings=decimal_str_or_none(
                            income_source.taxable_amount
                        ),
                    )
                    for income_source in sa106.overseas_pensions.income_source
                ]
                if sa106.overseas_pensions.income_source
                else [],
                totals=mtr.MtrSa106SourceOfForeignIncomeTotals(
                    swtor_uktax=decimal_str_or_none(
                        sa106.overseas_pensions.totals.special_withholding_tax
                    ),
                    taxable_amount=decimal_str_or_none(
                        sa106.overseas_pensions.totals.taxable_amount
                    ),
                )
                if sa106.overseas_pensions.totals
                else None,
            )
            if sa106.overseas_pensions
            else None,
            overseas_dividend_income=mtr.Mtr.Sa106.OverseasDividendIncome(
                income_source=[
                    mtr.Mtr.Sa106.OverseasDividendIncome.IncomeSource(
                        country_code=income_source.country_code,
                        income_before_tax=decimal_str_or_none(
                            income_source.income_before_tax
                        ),
                        foreign_tax=decimal_str_or_none(income_source.foreign_tax),
                        special_withholding_tax=decimal_str_or_none(
                            income_source.special_withholding_tax
                        ),
                        claim_to_ftcr=_yes(income_source.claim_to_ftcr),
                        taxable_amount_on_interest_and_other_savings=decimal_str_or_none(
                            income_source.taxable_amount
                        ),
                    )
                    for income_source in sa106.overseas_dividend_income.income_source
                ]
                if sa106.overseas_dividend_income.income_source
                else [],
                totals=mtr.MtrSa106SourceOfForeignIncomeTotals(
                    swtor_uktax=decimal_str_or_none(
                        sa106.overseas_dividend_income.totals.special_withholding_tax
                    ),
                    taxable_amount=decimal_str_or_none(
                        sa106.overseas_dividend_income.totals.taxable_amount
                    ),
                )
                if sa106.overseas_dividend_income.totals
                else None,
            )
            if sa106.overseas_dividend_income
            else None,
            overseas_trust_income=mtr.Mtr.Sa106.OverseasTrustIncome(
                income_source=[
                    mtr.Mtr.Sa106.OverseasTrustIncome.IncomeSource(
                        country_code=income_source.country_code,
                        income_before_tax=decimal_str_or_none(
                            income_source.income_before_tax
                        ),
                        foreign_tax=decimal_str_or_none(income_source.foreign_tax),
                        special_withholding_tax=decimal_str_or_none(
                            income_source.special_withholding_tax
                        ),
                        claim_to_ftcr=_yes(income_source.claim_to_ftcr),
                        taxable_amount_on_interest_and_other_savings=decimal_str_or_none(
                            income_source.taxable_amount
                        ),
                    )
                    for income_source in sa106.overseas_trust_income.income_source
                ]
                if sa106.overseas_trust_income.income_source
                else [],
                totals=mtr.MtrSa106SourceOfForeignIncomeTotals(
                    swtor_uktax=decimal_str_or_none(
                        sa106.overseas_trust_income.totals.special_withholding_tax
                    ),
                    taxable_amount=decimal_str_or_none(
                        sa106.overseas_trust_income.totals.taxable_amount
                    ),
                )
                if sa106.overseas_trust_income.totals
                else None,
            )
            if sa106.overseas_trust_income
            else None,
            residential_property_income_or_restricted_finance_costs=decimal_str_or_none(
                sa106.residential_property_income_or_restricted_finance_costs
            ),
            unused_toaaresidential_finance_costs_brought_forward=decimal_str_or_none(
                sa106.unused_toaa_residential_finance_costs_brought_forward
            ),
            overseas_land_and_property_income_details=[
                mtr.Mtr.Sa106.OverseasLandAndPropertyIncomeDetails(
                    total_rents_and_other_property_receipts=decimal_str_or_none(
                        property_detail.total_rents_and_other_property_receipts
                    ),
                    property_income_allowance=decimal_str_or_none(
                        property_detail.property_income_allowance
                    ),
                    traditional_accounting=_yes(property_detail.traditional_accounting),
                    number_of_properties=property_detail.number_of_properties,
                    premiums_paid_for_lease=decimal_str_or_none(
                        property_detail.premiums_paid_for_lease
                    ),
                    allowable_property_expenses=decimal_str_or_none(
                        property_detail.allowable_property_expenses
                    ),
                    net_profit_or_loss=decimal_str_or_none(
                        property_detail.net_profit_or_loss
                    ),
                    private_use_adjustment=decimal_str_or_none(
                        property_detail.private_use_adjustment
                    ),
                    balancing_charges=decimal_str_or_none(
                        property_detail.balancing_charges
                    ),
                    capital_allowances=decimal_str_or_none(
                        property_detail.capital_allowances
                    ),
                    zero_emission_car_allowance=decimal_str_or_none(
                        property_detail.zero_emission_car_allowance
                    ),
                    the_structures_and_buildings_allowance=decimal_str_or_none(
                        property_detail.the_structures_and_buildings_allowance
                    ),
                    electric_charge_point_allowance=decimal_str_or_none(
                        property_detail.electric_charge_point_allowance
                    ),
                    costs_of_replacing_domestic_items=decimal_str_or_none(
                        property_detail.costs_of_replacing_domestic_items
                    ),
                    adjusted_profit_or_loss_for_the_year=decimal_str_or_none(
                        property_detail.adjusted_profit_or_loss_for_the_year
                    ),
                    residential_finance_costs=decimal_str_or_none(
                        property_detail.residential_finance_costs
                    ),
                    unused_residential_finance_costs_brought_forward=decimal_str_or_none(
                        property_detail.unused_residential_finance_costs_brought_forward
                    ),
                    property_abroad_country=property_detail.property_abroad_country,
                    property_abroad_profit_or_loss=decimal_str_or_none(
                        property_detail.property_abroad_profit_or_loss
                    ),
                    property_abroad_foreign_tax=decimal_str_or_none(
                        property_detail.property_abroad_foreign_tax
                    ),
                    property_abroad_uktax_taken_off=decimal_str_or_none(
                        property_detail.property_abroad_uk_tax_taken_off
                    ),
                    property_abroad_claim_to_ftcr=_yes(
                        property_detail.property_abroad_claim_to_ftcr
                    ),
                )
                for property_detail in sa106.overseas_land_and_property_income_details
            ]
            if sa106.overseas_land_and_property_income_details
            else [],
            total_adjusted_profit_or_loss=decimal_str_or_none(
                sa106.total_adjusted_profit_or_loss
            ),
            loss_brought_forward=decimal_str_or_none(sa106.loss_brought_forward),
            total_taxable_profit=decimal_str_or_none(sa106.total_taxable_profit),
            total_foreign_tax_taken_off=decimal_str_or_none(
                sa106.total_foreign_tax_taken_off
            ),
            total_special_withholding_tax=decimal_str_or_none(
                sa106.total_special_withholding_tax
            ),
            total_taxable_amount=decimal_str_or_none(sa106.total_taxable_amount),
            loss_set_off_against_total_income=decimal_str_or_none(
                sa106.loss_set_off_against_total_income
            ),
            loss_to_carry_forward=decimal_str_or_none(sa106.loss_to_carry_forward),
            foreign_tax_paid=[
                mtr.Mtr.Sa106.ForeignTaxPaid(
                    claim_to_ftcrcountry_code=foreign_tax.claim_to_ftcr_country_code,
                    claim_to_ftcrforeign_tax=decimal_str_or_none(
                        foreign_tax.claim_to_ftcr_foreign_tax
                    ),
                    claim_to_ftcrclaim_for_ftcr=_yes(
                        foreign_tax.claim_to_ftcr_claim_for_ftcr
                    ),
                    claim_to_ftcramount_chargable=decimal_str_or_none(
                        foreign_tax.claim_to_ftcr_amount_chargeable
                    ),
                )
                for foreign_tax in sa106.foreign_tax_paid
            ]
            if sa106.foreign_tax_paid
            else [],
            capital_gains=mtr.Mtr.Sa106.CapitalGains(
                chargeable_gains_ukrules=mtr.Mtr.Sa106.CapitalGains.ChargeableGainsUkrules(
                    chargeable_gains=decimal_str_or_none(
                        sa106.capital_gains.chargeable_gains_uk_rules.chargeable_gains
                    ),
                    number_of_days_over_which_gain_accrued=sa106.capital_gains.chargeable_gains_uk_rules.number_of_days_over_which_gain_accrued,
                )
                if sa106.capital_gains.chargeable_gains_uk_rules
                else None,
                chargeable_gains_foreign_rules=mtr.Mtr.Sa106.CapitalGains.ChargeableGainsForeignRules(
                    chargeable_gains=decimal_str_or_none(
                        sa106.capital_gains.chargeable_gains_foreign_rules.chargeable_gains
                    ),
                    number_of_days_over_which_gain_accrued=sa106.capital_gains.chargeable_gains_foreign_rules.number_of_days_over_which_gain_accrued,
                )
                if sa106.capital_gains.chargeable_gains_foreign_rules
                else None,
                foreign_tax_paid=decimal_str_or_none(
                    sa106.capital_gains.foreign_tax_paid
                ),
                foreign_tax_credit_relief_claim=_yes(
                    sa106.capital_gains.foreign_tax_credit_relief_claim
                ),
                total_foreign_tax_credit_relief_on_gains=decimal_str_or_none(
                    sa106.capital_gains.total_foreign_tax_credit_relief_on_gains
                ),
                special_withholding_tax=decimal_str_or_none(
                    sa106.capital_gains.special_withholding_tax
                ),
            )
            if sa106.capital_gains
            else None,
            other_overseas_income_and_gains=mtr.Mtr.Sa106.OtherOverseasIncomeAndGains(
                foreign_life_insurance_gains=decimal_str_or_none(
                    sa106.other_overseas_income_and_gains.foreign_life_insurance_gains
                ),
                number_of_years_since_policy_made=sa106.other_overseas_income_and_gains.number_of_years_since_policy_made,
                tax_treated_as_paid=decimal_str_or_none(
                    sa106.other_overseas_income_and_gains.tax_treated_as_paid
                ),
                omitted_amount_transfer_of_assets_exemption=decimal_str_or_none(
                    sa106.other_overseas_income_and_gains.omitted_amount_transfer_of_assets_exemption
                ),
            )
            if sa106.other_overseas_income_and_gains
            else None,
        )
        if sa106
        else None
    )


def _get_sa107(data: d.MTR) -> mtr.Mtr.Sa107 | None:
    sa107 = data.sa107
    return (
        mtr.Mtr.Sa107(
            income_from_trusts_and_settlements=mtr.Mtr.Sa107.IncomeFromTrustsAndSettlements(
                discretionary_income_payment=mtr.Mtr.Sa107.IncomeFromTrustsAndSettlements.DiscretionaryIncomePayment(
                    discretionary_income_payment_net_amount=decimal_str_or_none(
                        sa107.income_from_trusts_and_settlements.discretionary_income_payment.discretionary_income_payment_net_amount
                    ),
                    payments_from_settlor_interested_trusts=decimal_str_or_none(
                        sa107.income_from_trusts_and_settlements.discretionary_income_payment.payments_from_settlor_interested_trusts
                    ),
                )
                if sa107.income_from_trusts_and_settlements.discretionary_income_payment
                else None,
                nondiscretionary_income_entitlement_from_trusts=mtr.Mtr.Sa107.IncomeFromTrustsAndSettlements.NondiscretionaryIncomeEntitlementFromTrusts(
                    non_discretionary_income_taxed_at_basic_rate=decimal_str_or_none(
                        sa107.income_from_trusts_and_settlements.nondiscretionary_income_entitlement_from_trusts.non_discretionary_income_taxed_at_basic_rate
                    ),
                    non_discretionary_income_taxed_at_lower_rate=decimal_str_or_none(
                        sa107.income_from_trusts_and_settlements.nondiscretionary_income_entitlement_from_trusts.non_discretionary_income_taxed_at_lower_rate
                    ),
                    non_discretionary_income_taxed_at_dividend_rate=decimal_str_or_none(
                        sa107.income_from_trusts_and_settlements.nondiscretionary_income_entitlement_from_trusts.non_discretionary_income_taxed_at_dividend_rate
                    ),
                    income_from_trusts_etc_non_resident_trustees=_yes(
                        sa107.income_from_trusts_and_settlements.nondiscretionary_income_entitlement_from_trusts.income_from_trusts_etc_non_resident_trustees
                    ),
                )
                if sa107.income_from_trusts_and_settlements.nondiscretionary_income_entitlement_from_trusts
                else None,
            )
            if sa107.income_from_trusts_and_settlements
            else None,
            income_chargeable_on_settlors=mtr.Mtr.Sa107.IncomeChargeableOnSettlors(
                net_settlor_income_taxed_at_basic_rate=decimal_str_or_none(
                    sa107.income_chargeable_on_settlors.net_settlor_income_taxed_at_basic_rate
                ),
                net_settlor_income_taxed_at_lower_rate=decimal_str_or_none(
                    sa107.income_chargeable_on_settlors.net_settlor_income_taxed_at_lower_rate
                ),
                net_settlor_income_taxed_at_dividend_rate=decimal_str_or_none(
                    sa107.income_chargeable_on_settlors.net_settlor_income_taxed_at_dividend_rate
                ),
                net_settlor_income_taxed_at_trust_rate=decimal_str_or_none(
                    sa107.income_chargeable_on_settlors.net_settlor_income_taxed_at_trust_rate
                ),
                savings_income_at_trust_rate=decimal_str_or_none(
                    sa107.income_chargeable_on_settlors.savings_income_at_trust_rate
                ),
                net_settlor_income_taxed_at_dividend_trust_rate=decimal_str_or_none(
                    sa107.income_chargeable_on_settlors.net_settlor_income_taxed_at_dividend_trust_rate
                ),
                gross_settlor_income_to_be_taxed_at_basic_rate=decimal_str_or_none(
                    sa107.income_chargeable_on_settlors.gross_settlor_income_to_be_taxed_at_basic_rate
                ),
                gross_settlor_income_to_be_taxed_at_lower_rate=decimal_str_or_none(
                    sa107.income_chargeable_on_settlors.gross_settlor_income_to_be_taxed_at_lower_rate
                ),
                amount_of_uklife_insurance_policy=decimal_str_or_none(
                    sa107.income_chargeable_on_settlors.amount_of_uk_life_insurance_policy
                ),
            )
            if sa107.income_chargeable_on_settlors
            else None,
            income_from_estates=mtr.Mtr.Sa107.IncomeFromEstates(
                ukestates=mtr.Mtr.Sa107.IncomeFromEstates.Ukestates(
                    estate_income_taxed_at_basic_rate=decimal_str_or_none(
                        sa107.income_from_estates.uk_estates.estate_income_taxed_at_basic_rate
                    ),
                    estate_income_taxed_at_lower_rate=decimal_str_or_none(
                        sa107.income_from_estates.uk_estates.estate_income_taxed_at_lower_rate
                    ),
                    estate_income_taxed_at_dividend_rate=decimal_str_or_none(
                        sa107.income_from_estates.uk_estates.estate_income_taxed_at_dividend_rate
                    ),
                    estate_income_already_taxed_at75dividend_rate=decimal_str_or_none(
                        sa107.income_from_estates.uk_estates.estate_income_already_taxed_at_75_dividend_rate
                    ),
                    estate_income_taxed_at_nonrepayable_basic_rate=decimal_str_or_none(
                        sa107.income_from_estates.uk_estates.estate_income_taxed_at_nonrepayable_basic_rate
                    ),
                )
                if sa107.income_from_estates.uk_estates
                else None,
                foreign_estates=mtr.Mtr.Sa107.IncomeFromEstates.ForeignEstates(
                    foreign_estate_income=decimal_str_or_none(
                        sa107.income_from_estates.foreign_estates.foreign_estate_income
                    ),
                    relief_for_uktax_accounted_for=decimal_str_or_none(
                        sa107.income_from_estates.foreign_estates.relief_for_uk_tax_accounted_for
                    ),
                )
                if sa107.income_from_estates.foreign_estates
                else None,
            )
            if sa107.income_from_estates
            else None,
            foreign_tax=decimal_str_or_none(sa107.foreign_tax),
            income_from_residential_property=mtr.Mtr.Sa107.IncomeFromResidentialProperty(
                residential_property_income_or_restricted_finance_costs=decimal_str_or_none(
                    sa107.income_from_residential_property.residential_property_income_or_restricted_finance_costs
                ),
                unused_residential_finance_costs_brought_forward=decimal_str_or_none(
                    sa107.income_from_residential_property.unused_residential_finance_costs_brought_forward
                ),
            )
            if sa107.income_from_residential_property
            else None,
            any_other_information_space=sa107.any_other_information_space,
        )
        if sa107
        else None
    )


def _get_sa108(data: d.MTR) -> mtr.Mtr.Sa108 | None:
    sa108 = data.sa108
    return (
        mtr.Mtr.Sa108(
            residential_property_and_carried_interest=mtr.Mtr.Sa108.ResidentialPropertyAndCarriedInterest(
                number_of_disposals=sa108.residential_property_and_carried_interest.number_of_disposals,
                disposal_proceeds=decimal_str_or_none(
                    sa108.residential_property_and_carried_interest.disposal_proceeds
                ),
                allowable_costs=decimal_str_or_none(
                    sa108.residential_property_and_carried_interest.allowable_costs
                ),
                gains_on_residential_property_in_the_year=decimal_str_or_none(
                    sa108.residential_property_and_carried_interest.gains_on_residential_property_in_the_year
                ),
                losses_in_the_year=decimal_str_or_none(
                    sa108.residential_property_and_carried_interest.losses_in_the_year
                ),
                claim_or_election_made=sa108.residential_property_and_carried_interest.claim_or_election_made,
                gain_or_loss_from_ukproperty_disposal=decimal_str_or_none(
                    sa108.residential_property_and_carried_interest.gain_or_loss_from_uk_property_disposal
                ),
                ukproperty_disposal_tax_already_charged=decimal_str_or_none(
                    sa108.residential_property_and_carried_interest.uk_property_disposal_tax_already_charged
                ),
                gain_or_loss_from_rttreturn=decimal_str_or_none(
                    sa108.residential_property_and_carried_interest.gain_or_loss_from_rtt_return
                ),
                rtttax_already_charged=decimal_str_or_none(
                    sa108.residential_property_and_carried_interest.rtt_tax_already_charged
                ),
                carried_interest_arising_basis=decimal_str_or_none(
                    sa108.residential_property_and_carried_interest.carried_interest_arising_basis
                ),
                carried_interest_accruals_basis=decimal_str_or_none(
                    sa108.residential_property_and_carried_interest.carried_interest_accruals_basis
                ),
                gains_on_carried_interest_in_the_year=decimal_str_or_none(
                    sa108.residential_property_and_carried_interest.gains_on_carried_interest_in_the_year
                ),
            )
            if sa108.residential_property_and_carried_interest
            else None,
            cryptoassets=mtr.Mtr.Sa108.Cryptoassets(
                number_of_disposals=sa108.cryptoassets.number_of_disposals,
                disposal_proceeds=decimal_str_or_none(
                    sa108.cryptoassets.disposal_proceeds
                ),
                allowable_costs=decimal_str_or_none(sa108.cryptoassets.allowable_costs),
                gains_in_the_year=decimal_str_or_none(
                    sa108.cryptoassets.gains_in_the_year
                ),
                losses_in_the_year=decimal_str_or_none(
                    sa108.cryptoassets.losses_in_the_year
                ),
                claim_or_election_made=sa108.cryptoassets.claim_or_election_made,
                gain_from_rttreturn=decimal_str_or_none(
                    sa108.cryptoassets.gain_from_rtt_return
                ),
                rtttax_already_charged=decimal_str_or_none(
                    sa108.cryptoassets.rtt_tax_already_charged
                ),
            )
            if sa108.cryptoassets
            else None,
            other_property_assets_and_gains=mtr.Mtr.Sa108.OtherPropertyAssetsAndGains(
                number_of_disposals=sa108.other_property_assets_and_gains.number_of_disposals,
                disposal_proceeds=decimal_str_or_none(
                    sa108.other_property_assets_and_gains.disposal_proceeds
                ),
                allowable_costs=decimal_str_or_none(
                    sa108.other_property_assets_and_gains.allowable_costs
                ),
                gains_in_the_year=decimal_str_or_none(
                    sa108.other_property_assets_and_gains.gains_in_the_year
                ),
                non_residential_disposals_included_in_box17=decimal_str_or_none(
                    sa108.other_property_assets_and_gains.non_residential_disposals_included_in_box17
                ),
                land_and_property_disposals_where_badris_being_claimed=decimal_str_or_none(
                    sa108.other_property_assets_and_gains.land_and_property_disposals_where_badr_is_being_claimed
                ),
                shares_disposals_where_badris_being_claimed=decimal_str_or_none(
                    sa108.other_property_assets_and_gains.shares_disposals_where_badr_is_being_claimed
                ),
                other_disposals_where_badris_being_claimed=decimal_str_or_none(
                    sa108.other_property_assets_and_gains.other_disposals_where_badr_is_being_claimed
                ),
                losses_in_the_year=decimal_str_or_none(
                    sa108.other_property_assets_and_gains.losses_in_the_year
                ),
                claim_or_election_made=sa108.other_property_assets_and_gains.claim_or_election_made,
                gain_from_rttreturn=decimal_str_or_none(
                    sa108.other_property_assets_and_gains.gain_from_rtt_return
                ),
                rtttax_already_charged=decimal_str_or_none(
                    sa108.other_property_assets_and_gains.rtt_tax_already_charged
                ),
            )
            if sa108.other_property_assets_and_gains
            else None,
            listed_shares_and_securities=mtr.Mtr.Sa108.ListedSharesAndSecurities(
                number_of_disposals=sa108.listed_shares_and_securities.number_of_disposals,
                disposal_proceeds=decimal_str_or_none(
                    sa108.listed_shares_and_securities.disposal_proceeds
                ),
                allowable_costs=decimal_str_or_none(
                    sa108.listed_shares_and_securities.allowable_costs
                ),
                gains_in_the_year=decimal_str_or_none(
                    sa108.listed_shares_and_securities.gains_in_the_year
                ),
                losses_in_the_year=decimal_str_or_none(
                    sa108.listed_shares_and_securities.losses_in_the_year
                ),
                claim_or_election_made=sa108.listed_shares_and_securities.claim_or_election_made,
                gain_from_rttreturn=decimal_str_or_none(
                    sa108.listed_shares_and_securities.gain_from_rtt_return
                ),
                rtttax_already_charged=decimal_str_or_none(
                    sa108.listed_shares_and_securities.rtt_tax_already_charged
                ),
            )
            if sa108.listed_shares_and_securities
            else None,
            unlisted_shares_and_securities=mtr.Mtr.Sa108.UnlistedSharesAndSecurities(
                number_of_disposals=sa108.unlisted_shares_and_securities.number_of_disposals,
                disposal_proceeds=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.disposal_proceeds
                ),
                allowable_costs=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.allowable_costs
                ),
                gains_in_the_year=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.gains_in_the_year
                ),
                losses_in_the_year=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.losses_in_the_year
                ),
                claim_or_election_made=sa108.unlisted_shares_and_securities.claim_or_election_made,
                gain_from_rttreturn=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.gain_from_rtt_return
                ),
                rtttax_already_charged=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.rtt_tax_already_charged
                ),
                gains_exceeding_esslimit=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.gains_exceeding_esslimit
                ),
                gains_invested_under_seed_eis=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.gains_invested_under_seed_eis
                ),
                losses_used_against_return_year_income=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.losses_used_against_return_year_income
                ),
                seisand_eisloss_relief_in_return_year=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.seis_and_eis_loss_relief_in_return_year
                ),
                losses_used_against_previous_return_year_income=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.losses_used_against_previous_return_year_income
                ),
                seisand_eisloss_relief_in_previous_return_year=decimal_str_or_none(
                    sa108.unlisted_shares_and_securities.seis_and_eis_loss_relief_in_previous_return_year
                ),
            )
            if sa108.unlisted_shares_and_securities
            else None,
            losses_and_adjustments=mtr.Mtr.Sa108.LossesAndAdjustments(
                losses_brought_forward_and_used_in_the_return_year=decimal_str_or_none(
                    sa108.losses_and_adjustments.losses_brought_forward_and_used_in_the_return_year
                ),
                income_losses_of_the_return_year_set_against_gains=decimal_str_or_none(
                    sa108.losses_and_adjustments.income_losses_of_the_return_year_set_against_gains
                ),
                losses_to_be_carried_forward=decimal_str_or_none(
                    sa108.losses_and_adjustments.losses_to_be_carried_forward
                ),
                losses_used_against_earlier_return_years_gain=decimal_str_or_none(
                    sa108.losses_and_adjustments.losses_used_against_earlier_return_years_gain
                ),
                gains_qualifying_for_investors_relief=decimal_str_or_none(
                    sa108.losses_and_adjustments.gains_qualifying_for_investors_relief
                ),
                gains_qualifying_for_business_asset_disposal_relief=decimal_str_or_none(
                    sa108.losses_and_adjustments.gains_qualifying_for_business_asset_disposal_relief
                ),
                badrand_erclaimed_to_date=decimal_str_or_none(
                    sa108.losses_and_adjustments.badr_and_er_claimed_to_date
                ),
                adjustment_to_cgt=decimal_str_or_none(
                    sa108.losses_and_adjustments.adjustment_to_cgt
                ),
                non_residentdual_resident_trust_liability=decimal_str_or_none(
                    sa108.losses_and_adjustments.non_resident_dual_resident_trust_liability
                ),
            )
            if sa108.losses_and_adjustments
            else None,
            nrcgton_ukproperty_or_land_and_indirect_disposals=mtr.Mtr.Sa108.NrcgtonUkpropertyOrLandAndIndirectDisposals(
                total_gains_chargeable_for_direct_disposals_for_ukresidential_property=decimal_str_or_none(
                    sa108.non_resident_cgt_uk_property_or_land_and_indirect_disposals.total_gains_chargeable_for_direct_disposals_for_uk_residential_property
                ),
                total_gains_chargeable_for_direct_disposals_for_uknrproperty=decimal_str_or_none(
                    sa108.non_resident_cgt_uk_property_or_land_and_indirect_disposals.total_gains_chargeable_for_direct_disposals_for_uk_nr_property
                ),
                gains_from_indirect_disposals=_yes(
                    sa108.non_resident_cgt_uk_property_or_land_and_indirect_disposals.gains_from_indirect_disposals
                ),
                tax_on_gains_already_charged=decimal_str_or_none(
                    sa108.non_resident_cgt_uk_property_or_land_and_indirect_disposals.tax_on_gains_already_charged
                ),
                total_losses_available_against_nrcgtgains_for_the_year=decimal_str_or_none(
                    sa108.non_resident_cgt_uk_property_or_land_and_indirect_disposals.total_losses_available_against_nrcgt_gains_for_the_year
                ),
            )
            if sa108.non_resident_cgt_uk_property_or_land_and_indirect_disposals
            else None,
            eisand_qahc=mtr.Mtr.Sa108.EisandQahc(
                total_gains_from_eis=decimal_str_or_none(
                    sa108.eis_and_qahc.total_gains_from_eis
                ),
                total_gains_from_qahc=decimal_str_or_none(
                    sa108.eis_and_qahc.total_gains_from_qahc
                ),
                total_losses_from_qahc=decimal_str_or_none(
                    sa108.eis_and_qahc.total_losses_from_qahc
                ),
            )
            if sa108.eis_and_qahc
            else None,
            estimate_or_valuation=_yes(sa108.estimate_or_valuation),
            any_other_information_space=sa108.any_other_information_space,
        )
        if sa108
        else None
    )


def _get_sa109(data: d.MTR) -> mtr.Mtr.Sa109 | None:
    sa109 = data.sa109
    return (
        mtr.Mtr.Sa109(
            residence_status=mtr.Mtr.Sa109.ResidenceStatus(
                not_resident_in_uk=_yes(sa109.residence_status.not_resident_in_uk),
                request_for_split_year_treatment=_yes(
                    sa109.residence_status.request_for_split_year_treatment
                ),
                more_than_one_case_of_split_year_treatment_applies=_yes(
                    sa109.residence_status.more_than_one_case_of_split_year_treatment_applies
                ),
                resident_in_ukfor_previous_year=_yes(
                    sa109.residence_status.resident_in_uk_for_previous_year
                ),
                split_year_treatment_date_from_which_the_ukpart_year_begins_or_ends=xml_date_or_none(
                    sa109.residence_status.split_year_treatment_date_from_which_the_uk_part_year_begins_or_ends
                ),
                meet_the_third_automatic_overseas_test=_yes(
                    sa109.residence_status.meet_the_third_automatic_overseas_test
                ),
                had_agap_between_employments_in_this_tax_year=_yes(
                    sa109.residence_status.had_a_gap_between_employments_in_this_tax_year
                ),
                had_ahome_overseas=_yes(sa109.residence_status.had_a_home_overseas),
            )
            if sa109.residence_status
            else None,
            time_spent_in_uk=mtr.Mtr.Sa109.TimeSpentInUk(
                number_of_days_spent_in_uk=sa109.time_spent_in_uk.number_of_days_spent_in_uk,
                number_of_days_due_to_exceptional_circumstances=sa109.time_spent_in_uk.number_of_days_due_to_exceptional_circumstances,
                number_of_days_in_ukwhile_in_transit=sa109.time_spent_in_uk.number_of_days_in_uk_while_in_transit,
                how_many_ties_to_uk=sa109.time_spent_in_uk.how_many_ties_to_uk,
                number_of_workdays_in_ukfor_employment=sa109.time_spent_in_uk.number_of_workdays_in_uk_for_employment,
                number_of_workdays_spent_overseas=sa109.time_spent_in_uk.number_of_workdays_spent_overseas,
            )
            if sa109.time_spent_in_uk
            else None,
            personal_allowances=mtr.Mtr.Sa109.PersonalAllowances(
                personal_allowances_claim_due_to_dta=_yes(
                    sa109.personal_allowances.personal_allowances_claim_due_to_dta
                ),
                personal_allowances_claim_on_other_basis=_yes(
                    sa109.personal_allowances.personal_allowances_claim_on_other_basis
                ),
                code_for_country_of_nationality_or_residence=sa109.personal_allowances.code_for_country_of_nationality_or_residence,
            )
            if sa109.personal_allowances
            else None,
            residence_in_other_countries=mtr.Mtr.Sa109.ResidenceInOtherCountries(
                code_for_country_of_residence_for_tax_in_year=sa109.residence_in_other_countries.code_for_country_of_residence_for_tax_in_year,
                code_for_country_of_residence_in_previous_year=sa109.residence_in_other_countries.code_for_country_of_residence_in_previous_year,
                amount_of_dtaincome_for_which_partial_relief_is_claimed=decimal_str_or_none(
                    sa109.residence_in_other_countries.amount_of_dta_income_for_which_partial_relief_is_claimed
                ),
                dtarelief_claim_residence_in_another_country=decimal_str_or_none(
                    sa109.residence_in_other_countries.dta_relief_claim_residence_in_another_country
                ),
                dtarelief_claim_other_provisions=decimal_str_or_none(
                    sa109.residence_in_other_countries.dta_relief_claim_other_provisions
                ),
            )
            if sa109.residence_in_other_countries
            else None,
            remittance_basis=mtr.Mtr.Sa109.RemittanceBasis(
                remitted_income_or_gains=_yes(
                    sa109.remittance_basis.remitted_income_or_gains
                ),
                amount_of_relief_claimed_for_investment_in_qualifying_business=decimal_str_or_none(
                    sa109.remittance_basis.investment_in_qualifying_business.amount_of_relief_claimed_for_investment_in_qualifying_business
                ),
                previous_investment_no_longer_qualifies=_yes(
                    sa109.remittance_basis.previous_investment_no_longer_qualifies
                ),
            )
            if sa109.remittance_basis
            else None,
            any_other_information_space=sa109.any_other_information_space,
        )
        if sa109
        else None
    )


def _get_attached_files(data: d.MTR) -> mtr.Mtr.AttachedFiles | None:
    return (
        mtr.Mtr.AttachedFiles(
            attachment=[
                mtr.Mtr.AttachedFiles.Attachment(
                    value=decode_attachment(attachment.content_base64),
                    file_format=_attachment_file_format(attachment.file_format),
                    filename=attachment.file_name,
                    size=attachment.size,
                    description=attachment.description,
                )
                for attachment in data.attached_files.attachment
            ]
        )
        if data.attached_files
        else None
    )
