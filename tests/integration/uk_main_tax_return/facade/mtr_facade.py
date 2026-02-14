from __future__ import (
    annotations,
)  # for forward references in type hints without quotes

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum, unique

try:
    from enum import StrEnum
except ImportError:  # Python < 3.11

    class StrEnum(str, Enum):  # type: ignore[no-redef]
        pass

#
# Public API
#


@dataclass(frozen=True, kw_only=True, slots=True)
class MTR:
    declaration: MTRDeclaration
    sa100: MTRSA100
    sa102: list[MTRSA102] | None = None
    sa102m: list[MTRSA102M] | None = None
    sa103s: list[MTRSA103S] | None = None
    sa103f: list[MTRSA103F] | None = None
    sa104s: list[MTRSA104S] | None = None
    sa104f: list[MTRSA104F] | None = None
    sa105: MTRSA105 | None = None
    sa106: MTRSA106 | None = None
    sa107: MTRSA107 | None = None
    sa108: MTRSA108 | None = None
    sa109: MTRSA109 | None = None
    sa110: MTRSA110 | None = None
    taxpayer_name: str | None = None
    welsh_return: MTRYesType | None = None
    amended_return: MTRYesType | None = None
    attached_files: MTRAttachedFiles | None = None


#
# Helpers
#


@unique
class TaxPayerStatus(StrEnum):
    C = "C"  # Welsh
    S = "S"  # Scottish
    U = "U"  # Rest of the UK


@unique
class MTRYesType(StrEnum):
    YES = "yes"


@unique
class MTRYesNoType(StrEnum):
    YES = "yes"
    NO = "no"


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRAddress:
    line1: str
    line2: str
    line3: str | None = None
    line4: str | None = None
    postcode: str | None = None
    effective_from: date | None = None


class MTRAttachmentFileFormat(StrEnum):
    PDF = "pdf"


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRAttachment:
    content_base64: str
    file_format: MTRAttachmentFileFormat
    file_name: str
    size: int | None = None
    description: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRAttachedFiles:
    attachment: list[MTRAttachment]


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRDeclaration:
    individual_declaration: MTRYesType | None = None
    agent_declaration: MTRYesType | None = None


# SA100 - Main Tax Return
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100:
    personal_details: MTRSA100PersonalDetails
    tax_return: MTRSA100TaxReturn | None = None
    student_loan_repayments: MTRSA100StudentLoanRepayments | None = None
    income: MTRSA100Income | None = None
    tax_reliefs: MTRSA100TaxReliefs | None = None
    high_income_child_benefit_charge: MTRSA100HighIncomeChildBenefitCharge | None = None
    marriage_allowance: MTRSA100MarriageAllowance | None = None
    marriage_allowance_transferred_in: MTRYesType | None = None
    marriage_allowance_transferred_out: MTRYesType | None = None
    finishing_tax_return: MTRSA100FinishingYourTaxReturn | None = None
    chargeable_event_gains: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100PersonalDetails:
    taxpayer_status: TaxPayerStatus
    dob: date | None = None
    new_address: MTRAddress | None = None
    phone_number: str | None = None
    national_insurance_number: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100TaxReturn:
    employment_schedule: MTRYesType | None = None
    number_of_employment_schedules: int | None = None
    minister_of_religion: MTRYesType | None = None
    number_of_minister_of_religion_schedules: int | None = None
    full_self_employment_schedule: MTRYesType | None = None
    number_of_full_self_employment_schedules: int | None = None
    short_self_employment_schedule: MTRYesType | None = None
    number_of_short_self_employment_schedules: int | None = None
    lloyds_underwriter_schedule: MTRYesType | None = None
    full_partnership_schedule: MTRYesType | None = None
    number_of_full_partnership_schedules: int | None = None
    short_partnership_schedule: MTRYesType | None = None
    number_of_short_partnership_schedules: int | None = None
    uk_property_schedule: MTRYesType | None = None
    foreign_schedule: MTRYesType | None = None
    trust_schedule: MTRYesType | None = None
    capital_gains_schedule: MTRYesType | None = None
    capital_gains_computation_attached: MTRYesType | None = None
    resident_remittance_schedule: MTRYesType | None = None
    additional_information_schedule: MTRYesType | None = None


class MTRStudentLoanPlanType(StrEnum):
    PLAN1 = "01"
    PLAN2 = "02"
    PLAN4 = "04"


class MTRPostgraduateLoanPlanType(StrEnum):
    PLAN3 = "03"


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100StudentLoanRepayments:
    income_contingent_student_loan_notification: MTRYesType | None = None
    student_loan_repayment_deducted_amount: Decimal | None = None
    postgraduate_loan_repayment_deducted_amount: Decimal | None = None
    student_loan_plan_type: MTRStudentLoanPlanType | None = None
    postgraduate_loan_plan_type: MTRPostgraduateLoanPlanType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100UKInterestAndDividends:
    taxed_bank_building_society_etc_interest: Decimal | None = None
    untaxed_uk_interest_etc: Decimal | None = None
    untaxed_foreign_interest: Decimal | None = None
    company_dividends: Decimal | None = None
    unit_trust_etc_dividends: Decimal | None = None
    foreign_dividends: Decimal | None = None
    tax_taken_off_foreign_dividends: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100StateBenefits:
    annual_state_pension: Decimal | None = None
    state_pension_lump_sum: Decimal | None = None
    tax_taken_off_pension_lump_sum: Decimal | None = None
    other_pensions_and_retirement_annuities: Decimal | None = None
    tax_taken_off_pensions_and_retirement_annuities: Decimal | None = None
    incapacity_benefit: Decimal | None = None
    tax_taken_off_incapacity_benefit: Decimal | None = None
    jobseekers_allowance: Decimal | None = None
    other_state_pensions_and_benefits: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100OtherTaxableIncomeDetails:
    other_taxable_income: Decimal
    tax_taken_off_other_taxable_income: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100OtherUKIncome:
    other_taxable_income_details: MTRSA100OtherTaxableIncomeDetails | None = None
    allowable_expenses: Decimal | None = None
    deemed_income_or_benefits: Decimal | None = None
    description_of_other_income: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100Income:
    uk_interest_and_dividends: MTRSA100UKInterestAndDividends | None = None
    state_benefits: MTRSA100StateBenefits | None = None
    other_uk_income: MTRSA100OtherUKIncome | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100TaxReliefsPensions:
    payments_to_registered_pension_schemes: Decimal | None = None
    one_off_registered_pension_schemes_payments: Decimal | None = None
    retirement_annuity_contract_payments: Decimal | None = None
    employer_pension_scheme_payments: Decimal | None = None
    non_uk_overseas_pension_scheme_payments: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100TaxReliefsCharitableGiving:
    gift_aid_payments_made_in_year: Decimal | None = None
    one_off_gift_aid_payments: Decimal | None = None
    gift_aid_payments_carried_back_to_previous_year: Decimal | None = None
    gift_aid_payments_brought_back_from_later_year: Decimal | None = None
    shares_gifted_to_charity: Decimal | None = None
    land_and_buildings_gifted_to_charity: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100TaxReliefsBlindPersonsAllowanceDetails:
    registered_blind: MTRYesType | None = None
    surplus_blind_persons_allowance_to_spouse: MTRYesType | None = None
    local_authority_name: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100TaxReliefsBlindPersonsAllowance:
    blind_persons_allowance_details: (
        MTRSA100TaxReliefsBlindPersonsAllowanceDetails | None
    ) = None
    surplus_blind_persons_allowance_from_spouse: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100TaxReliefs:
    pensions: MTRSA100TaxReliefsPensions | None = None
    charitable_giving: MTRSA100TaxReliefsCharitableGiving | None = None
    blind_persons_allowance: MTRSA100TaxReliefsBlindPersonsAllowance | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100HighIncomeChildBenefitCharge:
    amount_received: Decimal | None = None
    number_of_children: int | None = None
    date_stopped_receiving_all_child_benefit_payments: date | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100MarriageAllowance:
    spouse_first_name: str
    spouse_last_name: str
    spouse_nino: str
    spouse_date_of_birth: date
    date_of_marriage_or_civil_partnership: date


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100NotPaidEnough:
    tax_owed_not_to_be_coded_out: MTRYesType | None = None
    non_paye_income_not_to_be_coded_out: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100PaidTooMuchBankAccountDetails:
    bank_or_building_society_name: str
    account_holder_or_nominee_name: str
    branch_sort_code: str
    account_number: str
    building_society_reference_number: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSAAddress:
    line: list[str]
    short_line: str | None = None
    post_code: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100PaidTooMuchNomineeDetails:
    nominee_name_given: MTRYesType
    nominee_address: MTRSAAddress
    nominee_is_tax_adviser: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100PaidTooMuchPaymentDetails:
    bank_account_details: MTRSA100PaidTooMuchBankAccountDetails | None = None
    nominee_details: MTRSA100PaidTooMuchNomineeDetails | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100PaidTooMuch:
    payment_details: MTRSA100PaidTooMuchPaymentDetails | None = None
    no_bank_or_building_society_account: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100TaxAdviser:
    tax_adviser: str | None = None
    tax_adviser_phone_number: str | None = None
    tax_adviser_address: MTRSAAddress | None = None
    tax_advisers_reference: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100SigningYourForm:
    other_information_space: str | None = None
    provisional_figures: MTRYesType | None = None
    capacity_of_person_signing: str | None = None
    name_of_person_signed_for: str | None = None
    name_of_person_signing: str | None = None
    address_of_person_signing: MTRSAAddress | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA100FinishingYourTaxReturn:
    tax_refunded_or_set_off: Decimal | None = None
    not_paid_enough: MTRSA100NotPaidEnough | None = None
    paid_too_much: MTRSA100PaidTooMuch | None = None
    tax_adviser: MTRSA100TaxAdviser | None = None
    signing_your_form: MTRSA100SigningYourForm | None = None


# SA102 - Employment
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA102:
    employment: MTRSA102Employment
    benefits: MTRSA102Benefits | None = None
    expenses: MTRSA102Expenses | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA102Employment:
    pay_from_employment: Decimal | None = None
    payrolled_benefits: Decimal | None = None
    tax_taken_off_pay: Decimal | None = None
    total_class1_nicable_earnings: Decimal | None = None
    tips_and_other_payments: Decimal | None = None
    pension_contribution_payment_from_hmrc: Decimal | None = None
    employer_paye_reference: str
    employers_name: str | None = None
    company_director: MTRYesNoType | None = None
    date_ceased_being_a_director: date | None = None
    close_company: MTRYesNoType | None = None
    close_company_name: str | None = None
    company_registration_number: str | None = None
    close_company_dividend: Decimal | None = None
    percentage_shareholding: int | None = None
    off_payroll_working: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA102Benefits:
    company_cars_and_vans_benefit: Decimal | None = None
    fuel_for_cars_and_vans: Decimal | None = None
    private_medical_dental_insurance: Decimal | None = None
    vouchers_credit_cards_excess_mileage_allowance: Decimal | None = None
    goods_etc_provided_by_employer: Decimal | None = None
    accommodation_provided_by_employer: Decimal | None = None
    other_benefits: Decimal | None = None
    expenses_payments_received: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA102Expenses:
    business_travel_and_subsistence: Decimal | None = None
    fixed_expenses_deductions: Decimal | None = None
    professional_fees_and_subscriptions: Decimal | None = None
    other_expenses_and_capital_allowances: Decimal | None = None


# SA102M - Special employment categories (Ministers of Religion)
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA102M:
    income: MTRSA102MIncome | None = None
    benefits_and_expense_payments_to_you: (
        MTRSA102MBenefitsAndExpensePaymentsToYou | None
    ) = None
    income_benefits_and_expenses_received: Decimal | None = None
    expenses_paid_by_you: MTRSA102MExpensesPaidByYou | None = None
    service_benefit_cap: MTRSA102MServiceBenefitCap | None = None
    other_income: MTRSA102MOtherIncome | None = None
    taxable_income: MTRSA102MTaxableIncome | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA102MIncome:
    nature_of_post: str | None = None
    salary_or_stipend: Decimal | None = None
    payrolled_benefits: Decimal | None = None
    tax_taken_off_salary_stipend: Decimal | None = None
    total_class1_nicable_earnings: Decimal | None = None
    fees_and_offerings: Decimal | None = None
    pension_contribution_payment_from_hmrc: Decimal | None = None
    vicarage_manse_expenses: Decimal | None = None
    personal_expenses_etc_paid: Decimal | None = None
    excess_mileage_allowance_etc: Decimal | None = None
    round_sum_expenses_and_rent_allowances: Decimal | None = None
    tax_taken_off_round_sum_expenses: Decimal | None = None
    other_income_from_post: Decimal | None = None
    tax_taken_off_other_income: Decimal | None = None
    total_income_as_minister_of_religion: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA102MBenefitsAndExpensePaymentsToYou:
    vicarage_services_benefit: Decimal | None = None
    car_provided: Decimal | None = None
    fuel_for_car_provided: Decimal | None = None
    interest_free_loans: Decimal | None = None
    expenses_payments_made: Decimal | None = None
    other_benefits: Decimal | None = None
    total_benefits_and_expenses: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA102MExpensesPaidByYou:
    travelling_expenses_and_capital_allowances: Decimal | None = None
    maintenance_and_repairs_etc: Decimal | None = None
    rent_expenses: Decimal | None = None
    other_expenses: Decimal | None = None
    total_expenses_paid: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA102MServiceBenefitCap:
    gross_income: Decimal | None = None
    backpay_received_after_year_end: Decimal | None = None
    earlier_years_backpay_received_in_year: Decimal | None = None
    pension_scheme_payments: Decimal | None = None
    net_income: Decimal | None = None
    ten_percent_of_net_income: Decimal | None = None
    amount_paid_toward_service_benefit: Decimal | None = None
    payments_made_and_service_benefit_received: Decimal | None = None
    service_benefit_cap: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA102MOtherIncome:
    chaplaincy_and_other_income: Decimal | None = None
    tax_taken_of_other_income: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA102MTaxableIncome:
    taxable_income_minus_expenses: Decimal | None = None
    total_tax_taken_off: Decimal | None = None


# SA103S - Self-employment (short)
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103S:
    business_details: MTRSA103SBusinessDetails
    business_income: MTRSA103SBusinessIncome | None = None
    allowable_business_expenses: MTRSA103SAllowableBusinessExpenses | None = None
    net_profit_or_loss: Decimal | None = None
    capital_allowances: MTRSA103SCapitalAllowances | None = None
    taxable_profits: MTRSA103STaxableProfits | None = None
    profits_losses_nics_and_cis: MTRSA103SProfitsLossesNICsAndCIS | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103SBusinessDetails:
    business_description: str
    business_address_postcode: str | None = None
    change_of_business_details: MTRYesType | None = None
    foster_etc_carer_indicator: MTRYesType | None = None
    did_your_business_start: MTRYesNoType | None = None
    date_business_started: date | None = None
    did_your_business_cease: MTRYesNoType | None = None
    date_business_ceased: date | None = None
    date_business_books_are_made_up_to: date | None = None
    election_to_opt_out_of_cash_basis: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103SBusinessIncome:
    turnover: Decimal | None = None
    other_business_income: Decimal | None = None
    trading_income_allowance: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103SAllowableBusinessExpenses:
    cost_of_goods: Decimal | None = None
    car_van_and_travel_expenses: Decimal | None = None
    wages_salaries_and_staff_costs: Decimal | None = None
    rent_and_other_property_costs: Decimal | None = None
    repairs_and_maintenance_costs: Decimal | None = None
    accountancy_and_legal_fees: Decimal | None = None
    interest_and_finance_charges: Decimal | None = None
    phone_and_other_office_costs: Decimal | None = None
    other_allowable_business_expenses: Decimal | None = None
    total_allowable_expenses: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103SCapitalAllowances:
    annual_investment_allowance: Decimal | None = None
    allowance_for_small_balance_of_unrelieved_expenditure: Decimal | None = None
    zero_emission_car_allowance: Decimal | None = None
    other_capital_allowances: Decimal | None = None
    the_structures_and_buildings_allowance: Decimal | None = None
    freeport_and_investment_zones_structures_and_buildings_allowance: Decimal | None = (
        None
    )
    total_balancing_charges: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103STaxableProfits:
    own_goods_and_services: Decimal | None = None
    net_business_profit_for_tax: Decimal | None = None
    loss_brought_forward: Decimal | None = None
    any_other_business_income: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103SProfitsLossesNICsAndCIS:
    total_taxable_business_profits: Decimal | None = None
    net_business_loss_for_tax: Decimal | None = None
    loss_of_year_set_against_other_income: Decimal | None = None
    loss_to_carry_back: Decimal | None = None
    total_loss_to_carry_forward: Decimal | None = None
    pay_class2_nic_voluntarily: MTRYesType | None = None
    class2_nic_amount: Decimal | None = None
    class4_nic_exempt: MTRYesType | None = None
    sub_contractors_tax_deduction: Decimal | None = None


# SA103F - Self-employment (full)
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103F:
    business_details: MTRSA103FBusinessDetails
    other_information: MTRSA103FOtherInformation | None = None
    business_income: MTRSA103FBusinessIncome | None = None
    business_expenses: MTRSA103FBusinessExpenses | None = None
    net_profit_loss: Decimal | None = None
    capital_allowances: MTRSA103FCapitalAllowances | None = None
    taxable_profit_or_loss: MTRSA103FTaxableProfitOrLoss | None = None
    losses: MTRSA103FLosses | None = None
    tax_taken_off: MTRSA103FTaxTakenOff | None = None
    balance_sheet: MTRSA103FBalanceSheet | None = None
    nics: MTRSA103FNICs | None = None
    other_information_space: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FBusinessDetails:
    business_name: str
    business_description: str
    business_address_first_line: str | None = None
    business_address_postcode: str | None = None
    change_of_business_details: MTRYesType | None = None
    did_your_business_start: MTRYesNoType | None = None
    date_business_started: date | None = None
    did_your_business_cease: MTRYesNoType | None = None
    date_business_ceased: date | None = None
    date_accounting_period_starts: date | None = None
    date_accounting_period_ends: date | None = None
    election_to_opt_out_of_cash_basis: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FOtherInformation:
    special_arrangements_apply: MTRYesType | None = None
    information_provided_last_year: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FBusinessIncome:
    turnover: Decimal | None = None
    other_business_income: Decimal | None = None
    trading_income_allowance: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FTotalExpenses:
    cost_of_goods: Decimal | None = None
    subcontractor_costs: Decimal | None = None
    wages_salaries_and_staff_costs: Decimal | None = None
    car_van_and_travel_expenses: Decimal | None = None
    rent_and_other_property_costs: Decimal | None = None
    repairs_and_maintenance_costs: Decimal | None = None
    phone_and_other_office_costs: Decimal | None = None
    advertising_and_entertainment_costs: Decimal | None = None
    bank_and_loan_interest: Decimal | None = None
    other_finance_charges: Decimal | None = None
    debts_written_off: Decimal | None = None
    accountancy_and_legal_fees: Decimal | None = None
    depreciation_and_loss_profit_on_sale: Decimal | None = None
    other_business_expenses: Decimal | None = None
    total_expenses: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FDisallowableExpenses:
    disallowable_cost_of_goods: Decimal | None = None
    disallowable_subcontractor_costs: Decimal | None = None
    disallowable_staff_costs: Decimal | None = None
    disallowable_car_and_travel_expenses: Decimal | None = None
    disallowable_rent_and_other_property_costs: Decimal | None = None
    disallowable_repairs_and_maintenance_costs: Decimal | None = None
    disallowable_phone_and_other_office_costs: Decimal | None = None
    disallowable_advertising_and_entertainment_costs: Decimal | None = None
    disallowable_bank_and_loan_interest: Decimal | None = None
    disallowable_other_finance_charges: Decimal | None = None
    disallowable_debts_written_off: Decimal | None = None
    disallowable_accountancy_and_legal_fees: Decimal | None = None
    disallowable_depreciation_and_loss_profit_on_sale: Decimal | None = None
    disallowable_other_business_expenses: Decimal | None = None
    total_disallowable_expenses: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FBusinessExpenses:
    total_expenses: MTRSA103FTotalExpenses | None = None
    disallowable_expenses: MTRSA103FDisallowableExpenses | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FCapitalAllowances:
    annual_investment_allowance: Decimal | None = None
    annual_allowances_at_higher_rate: Decimal | None = None
    annual_allowances_at_lower_rate: Decimal | None = None
    zero_emission_goods_vehicle_allowance: Decimal | None = None
    zero_emission_car_allowance: Decimal | None = None
    the_structures_and_buildings_allowance: Decimal | None = None
    freeport_and_investment_zones_structures_and_buildings_allowance: Decimal | None = (
        None
    )
    electric_charge_point_allowance: Decimal | None = None
    other_capital_allowances: Decimal | None = None
    balancing_allowances_on_sale_or_cessation: Decimal | None = None
    total_capital_allowances: Decimal | None = None
    total_balancing_charges: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FTaxableProfitOrLoss:
    own_goods_and_services: Decimal | None = None
    additions_to_net_profit_deductions_from_net_loss: Decimal | None = None
    non_taxable_business_income: Decimal | None = None
    deductions_from_net_profit_additions_to_net_loss: Decimal | None = None
    net_business_profit_loss_for_tax: Decimal | None = None
    tax_year_adjustment: Decimal | None = None
    change_of_accounting_practice_adjustment: Decimal | None = None
    averaging_adjustment: Decimal | None = None
    adjusted_profit_for_the_year: Decimal | None = None
    spread_transition_profit_treated_as_arising: Decimal | None = None
    loss_brought_forward_used_against_spread_transition_profit: Decimal | None = None
    loss_brought_forward: Decimal | None = None
    any_other_business_income: Decimal | None = None
    total_taxable_business_profits: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FLosses:
    adjusted_loss_for_the_year: Decimal | None = None
    loss_of_year_set_against_other_income: Decimal | None = None
    loss_to_carry_back: Decimal | None = None
    total_loss_to_carry_forward: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FTaxTakenOff:
    sub_contractors_tax_deduction: Decimal | None = None
    other_tax_taken_off_trading_income: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FBalanceSheetAssets:
    equipment_machinery_vehicles: Decimal | None = None
    other_fixed_assets: Decimal | None = None
    stock_and_work_in_progress: Decimal | None = None
    trade_debtors: Decimal | None = None
    bank_etc_balances: Decimal | None = None
    cash_in_hand: Decimal | None = None
    other_current_assets: Decimal | None = None
    total_business_assets: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FBalanceSheetLiabilities:
    trade_creditors: Decimal | None = None
    loans_and_overdrafts: Decimal | None = None
    other_liabilities: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FBalanceSheetCapitalAccount:
    capital_account_balance_at_start: Decimal | None = None
    net_profit_or_loss: Decimal | None = None
    capital_introduced: Decimal | None = None
    drawings: Decimal | None = None
    capital_account_balance_at_end: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FBalanceSheet:
    assets: MTRSA103FBalanceSheetAssets | None = None
    liabilities: MTRSA103FBalanceSheetLiabilities | None = None
    net_business_assets: Decimal | None = None
    capital_account: MTRSA103FBalanceSheetCapitalAccount | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA103FNICs:
    pay_class2_nic_voluntarily: MTRYesType | None = None
    class2_nic_amount: Decimal | None = None
    adjustment_to_class4_nic_profits: Decimal | None = None
    class4_nic_exempt: MTRYesType | None = None


# SA104S - Partnership income (short)
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104S:
    partnership_details: MTRSA104SPartnershipDetails
    share_of_partnership_trading_or_professional_profits: (
        MTRSA104SShareOfPartnershipTradingOrProfessionalProfits | None
    ) = None
    share_of_partnership_trading_or_professional_losses: (
        MTRSA104SShareOfPartnershipTradingOrProfessionalLosses | None
    ) = None
    nics: MTRSA104SNICs | None = None
    share_of_untaxed_interest_etc: Decimal | None = None
    share_of_partnerships_tax_paid: MTRSA104SShareOfPartnershipsTaxPaid | None = None
    any_other_information_space: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104SPartnershipDetails:
    partnership_reference_number: str
    partnership_description: str
    did_you_join_the_partnership: MTRYesNoType | None = None
    date_joined_partnership: date | None = None
    did_you_leave_the_partnership: MTRYesNoType | None = None
    date_left_partnership: date | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104SShareOfPartnershipTradingOrProfessionalProfits:
    share_of_partnership_profit_or_loss: Decimal | None = None
    tax_year_adjustment: Decimal | None = None
    change_of_accounting_practice_adjustment: Decimal | None = None
    averaging_adjustment: Decimal | None = None
    foreign_tax_claimed_as_deduction: Decimal | None = None
    adjusted_profit_for_year: Decimal | None = None
    losses_brought_forward: Decimal | None = None
    taxable_profits_after_losses: Decimal | None = None
    other_business_income: Decimal | None = None
    total_taxable_business_profits: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104SShareOfPartnershipTradingOrProfessionalLosses:
    adjusted_loss_for_year: Decimal | None = None
    loss_set_off_against_other_income: Decimal | None = None
    loss_to_be_carried_back: Decimal | None = None
    total_loss_to_carry_forward: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104SNICs:
    pay_class2_nic_voluntarily: MTRYesType | None = None
    class2_nic_amount: Decimal | None = None
    class4_nic_exempt: MTRYesType | None = None
    adjustment_to_class4_nic_profits: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104SShareOfPartnershipsTaxPaid:
    share_of_tax_taken_off_by_contractors: Decimal | None = None
    share_of_tax_taken_off_trading_income: Decimal | None = None


# SA104F - Partnership income (full)
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104F:
    partnership_details: MTRSA104FPartnershipDetails
    share_of_profits: MTRSA104FShareOfProfits | None = None
    share_of_losses: MTRSA104FShareOfLosses | None = None
    nics: MTRSA104FNics | None = None
    share_of_untaxed_income: MTRSA104FShareOfUntaxedIncome | None = None
    share_of_partnership_income: MTRSA104FShareOfPartnershipIncome | None = None
    share_of_partnership_tax_paid: MTRSA104FShareOfPartnershipTaxPaid | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FPartnershipDetails:
    partnership_reference_number: str
    partnership_description: str
    did_you_join_the_partnership: MTRYesNoType | None = None
    date_joined_partnership: date | None = None
    did_you_leave_the_partnership: MTRYesNoType | None = None
    date_left_partnership: date | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfProfits:
    share_of_partnership_profit_or_loss: Decimal | None = None
    tax_year_adjustment: Decimal | None = None
    change_of_accounting_practice_adjustment: Decimal | None = None
    averaging_adjustment: Decimal | None = None
    foreign_tax_claimed_as_deduction: Decimal | None = None
    adjusted_profit_for_year: Decimal | None = None
    spread_transition_profit_treated_as_arising: Decimal | None = None
    loss_brought_forward_used_against_spread_transition_profit: Decimal | None = None
    losses_brought_forward: Decimal | None = None
    taxable_profits_after_losses: Decimal | None = None
    other_business_income: Decimal | None = None
    total_taxable_business_profits: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfLosses:
    adjusted_loss_for_year: Decimal | None = None
    loss_set_off_against_other_income: Decimal | None = None
    loss_to_be_carried_back: Decimal | None = None
    total_loss_to_carry_forward: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FNics:
    pay_class2_nic_voluntarily: MTRYesType | None = None
    class2_nic_amount: Decimal | None = None
    class4_nic_exempt: MTRYesType | None = None
    adjustment_to_class4_nic_profits: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfUntaxedIncomeSavingsIncomeForeignIncome:
    foreign_untaxed_savings_income_share: Decimal | None = None
    foreign_untaxed_savings_adjustment: Decimal | None = None
    total_foreign_tax_taken_off: Decimal | None = None
    adjusted_foreign_savings_income: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfUntaxedIncomeSavingsIncome:
    uk_untaxed_savings_income_share: Decimal | None = None
    uk_untaxed_savings_adjustment: Decimal | None = None
    adjusted_uk_savings_income: Decimal | None = None
    foreign_income: MTRSA104FShareOfUntaxedIncomeSavingsIncomeForeignIncome | None = (
        None
    )
    total_untaxed_savings_income: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfUntaxedIncomeUkPropertyIncome:
    uk_property_profit_loss_share: Decimal | None = None
    uk_property_income_adjustment: Decimal | None = None
    loss_brought_forward: Decimal | None = None
    loss_for_year_set_off_against_other_income: Decimal | None = None
    loss_to_be_carried_forward: Decimal | None = None
    taxable_profits_after_adjustment_and_losses: Decimal | None = None
    residential_finance_costs: Decimal | None = None
    unused_residential_finance_costs_brought_forward: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfUntaxedIncomeOtherUntaxedUkIncomeInner:
    share_of_loss_from_other_untaxed_uk_income: Decimal | None = None
    adjustment_to_loss: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfUntaxedIncomeOtherUntaxedUkIncome:
    other_untaxed_uk_income_share: Decimal | None = None
    other_untaxed_uk_income_adjustment: Decimal | None = None
    loss_brought_forward: Decimal | None = None
    taxable_profit: Decimal | None = None
    other_untaxed_uk_income: (
        MTRSA104FShareOfUntaxedIncomeOtherUntaxedUkIncomeInner | None
    ) = None
    total_loss_to_carry_forward: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfUntaxedIncomeOffshoreFundsIncome:
    offshore_funds_income_share: Decimal | None = None
    offshore_funds_income_adjustment: Decimal | None = None
    foreign_tax_taken_off: Decimal | None = None
    taxable_income_after_adjustment_and_foreign_tax: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfUntaxedIncomeOtherUntaxedForeignIncomeForeignLosses:
    foreign_losses_brought_forward: Decimal | None = None
    foreign_losses_for_year_set_off_against_other_income: Decimal | None = None
    foreign_losses_to_be_carried_forward: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfUntaxedIncomeOtherUntaxedForeignIncome:
    other_untaxed_foreign_income_share: Decimal | None = None
    other_untaxed_foreign_income_adjustment: Decimal | None = None
    total_foreign_tax_taken_off: Decimal | None = None
    adjusted_foreign_income: Decimal | None = None
    foreign_losses: (
        MTRSA104FShareOfUntaxedIncomeOtherUntaxedForeignIncomeForeignLosses | None
    ) = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfUntaxedIncome:
    savings_income: MTRSA104FShareOfUntaxedIncomeSavingsIncome | None = None
    uk_property_income: MTRSA104FShareOfUntaxedIncomeUkPropertyIncome | None = None
    share_of_fhl_profit: Decimal | None = None
    adjustments_to_fhl_profit: Decimal | None = None
    taxable_fhl_profit: Decimal | None = None
    other_untaxed_uk_income: (
        MTRSA104FShareOfUntaxedIncomeOtherUntaxedUkIncome | None
    ) = None
    offshore_funds_income: MTRSA104FShareOfUntaxedIncomeOffshoreFundsIncome | None = (
        None
    )
    other_untaxed_foreign_income: (
        MTRSA104FShareOfUntaxedIncomeOtherUntaxedForeignIncome | None
    ) = None
    total_untaxed_income_share: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfPartnershipIncomeShareOfDividendIncome:
    dividend_income: Decimal | None = None
    total_foreign_tax_taken_off: Decimal | None = None
    total_dividend_income: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfPartnershipIncomeShareOfTaxedIncomeTaxableAt20Percent:
    share_of_taxed_income: Decimal | None = None
    total_foreign_tax_taken_off: Decimal | None = None
    taxed_income_taxable_at_20_percent: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfPartnershipIncomeShareOfOtherTaxedIncome:
    share_of_taxed_income: Decimal | None = None
    total_foreign_tax_taken_off: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfPartnershipIncome:
    share_of_dividend_income: (
        MTRSA104FShareOfPartnershipIncomeShareOfDividendIncome | None
    ) = None
    share_of_taxed_income_taxable_at_20_percent: (
        MTRSA104FShareOfPartnershipIncomeShareOfTaxedIncomeTaxableAt20Percent | None
    ) = None
    share_of_other_taxed_income: (
        MTRSA104FShareOfPartnershipIncomeShareOfOtherTaxedIncome | None
    ) = None
    share_of_total_taxed_and_untaxed_income: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA104FShareOfPartnershipTaxPaid:
    share_of_income_tax_taken_off_partnership_income: Decimal | None = None
    share_of_tax_taken_off_by_contractors: Decimal | None = None
    share_of_tax_taken_off_trading_income: Decimal | None = None
    share_of_total_tax_taken_off: Decimal | None = None


# SA105 - UK property
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA105:
    uk_property_details: MTRSA105UKPropertyDetails | None = None
    furnished_holiday_lettings: list[MTRSA105FurnishedHolidayLettings] | None = None
    property_income_and_expenses: MTRSA105PropertyIncomeAndExpenses | None = None
    taxable_profit_or_loss: MTRSA105TaxableProfitOrLoss | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA105UKPropertyDetails:
    number_of_properties: int | None = None
    property_income_ceased_in_year: MTRYesType | None = None
    income_from_property_let_jointly: MTRYesType | None = None
    rent_a_room_relief_claim: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA105FurnishedHolidayLettings:
    furnished_holiday_lettings_income: Decimal | None = None
    property_income_allowance: Decimal | None = None
    traditional_accounting: MTRYesType | None = None
    furnished_holiday_lettings_expenses: Decimal | None = None
    furnished_holiday_lettings_interest_etc_costs: Decimal | None = None
    furnished_holiday_lettings_management_etc_fees: Decimal | None = None
    furnished_holiday_lettings_other_expenses: Decimal | None = None
    private_use_adjustment: Decimal | None = None
    balancing_charges: Decimal | None = None
    electric_charge_point_allowance: Decimal | None = None
    zero_emission_car_allowance: Decimal | None = None
    capital_allowances: Decimal | None = None
    adjusted_profit_for_the_year: Decimal | None = None
    losses_brought_forward: Decimal | None = None
    taxable_profit_for_year: Decimal | None = None
    loss_for_year: Decimal | None = None
    loss_to_carry_forward: Decimal | None = None
    in_eea: MTRYesType | None = None
    period_of_grace_election: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA105PropertyIncomeAndExpenses:
    total_rents_and_other_income_from_property: Decimal | None = None
    property_income_allowance: Decimal | None = None
    traditional_accounting: MTRYesType | None = None
    tax_taken_off_any_income: Decimal | None = None
    premiums_for_grant_of_alease: Decimal | None = None
    reverse_premiums_and_inducements: Decimal | None = None
    rent_rates_insurance_and_ground_rents: Decimal | None = None
    repairs_and_maintenance: Decimal | None = None
    allowable_interest_and_other_financial_charges: Decimal | None = None
    legal_management_and_professional_fees: Decimal | None = None
    costs_of_services_provided: Decimal | None = None
    other_property_expenses: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA105TaxableProfitOrLoss:
    private_use_adjustment: Decimal | None = None
    balancing_charges: Decimal | None = None
    annual_investment_allowance: Decimal | None = None
    the_structures_and_buildings_allowance: Decimal | None = None
    electric_charge_point_allowance: Decimal | None = None
    freeport_and_investment_zones_structures_and_buildings_allowance: Decimal | None = (
        None
    )
    zero_emission_goods_vehicle_allowance: Decimal | None = None
    zero_emission_car_allowance: Decimal | None = None
    enhanced_capital_allowances: Decimal | None = None
    costs_of_replacing_domestic_items: Decimal | None = None
    rent_a_room_exempt_amount: Decimal | None = None
    adjusted_profit_for_the_year: Decimal | None = None
    loss_brought_forward: Decimal | None = None
    taxable_profit_for_the_year: Decimal | None = None
    adjusted_loss_for_the_year: Decimal | None = None
    loss_set_off_against_total_income_of_the_year: Decimal | None = None
    loss_to_carry_forward: Decimal | None = None
    residential_finance_costs: Decimal | None = None
    unused_residential_finance_costs_brought_forward: Decimal | None = None


# SA106 - Foreign income
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106:
    unremittable_income: MTRYesType | None = None
    foreign_tax_credit_relief: Decimal | None = None
    overseas_savings: MTRSA106OverseasSavings | None = None
    foreign_companies: MTRSA106ForeignCompanies | None = None
    remitted_foreign_savings: MTRSA106RemittedForeignSavings | None = None
    remitted_foreign_dividends: MTRSA106RemittedForeignDividends | None = None
    overseas_pensions: MTRSA106OverseasPensions | None = None
    overseas_dividend_income: MTRSA106OverseasDividendIncome | None = None
    overseas_trust_income: MTRSA106OverseasTrustIncome | None = None
    residential_property_income_or_restricted_finance_costs: Decimal | None = None
    unused_toaa_residential_finance_costs_brought_forward: Decimal | None = None
    overseas_land_and_property_income_details: (
        list[MTRSA106OverseasLandAndPropertyIncomeDetails] | None
    ) = None
    total_adjusted_profit_or_loss: Decimal | None = None
    loss_brought_forward: Decimal | None = None
    total_taxable_profit: Decimal | None = None
    total_foreign_tax_taken_off: Decimal | None = None
    total_special_withholding_tax: Decimal | None = None
    total_taxable_amount: Decimal | None = None
    loss_set_off_against_total_income: Decimal | None = None
    loss_to_carry_forward: Decimal | None = None
    foreign_tax_paid: list[MTRSA106ForeignTaxPaid] | None = None
    capital_gains: MTRSA106CapitalGains | None = None
    other_overseas_income_and_gains: MTRSA106OtherOverseasIncomeAndGains | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106IncomeSource:
    country_code: str
    income_before_tax: Decimal | None = None
    foreign_tax: Decimal | None = None
    special_withholding_tax: Decimal | None = None
    claim_to_ftcr: MTRYesType | None = None
    taxable_amount_on_interest_and_other_savings: Decimal | None = None
    taxable_amount: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106Totals:
    special_withholding_tax: Decimal | None = None
    taxable_amount: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106RemittedTotals:
    special_withholding_tax: Decimal | None = None
    taxable_amount: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106OverseasSavings:
    income_source: list[MTRSA106IncomeSource] | None = None
    totals: MTRSA106Totals | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106ForeignCompanies:
    income_source: list[MTRSA106IncomeSource] | None = None
    totals: MTRSA106Totals | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106RemittedForeignSavings:
    income_source: list[MTRSA106IncomeSource] | None = None
    totals: MTRSA106RemittedTotals | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106RemittedForeignDividends:
    income_source: list[MTRSA106IncomeSource] | None = None
    totals: MTRSA106RemittedTotals | None = None
    amount_subject_to_dividend_tax_credit: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106OverseasPensions:
    income_source: list[MTRSA106IncomeSource] | None = None
    totals: MTRSA106Totals | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106OverseasDividendIncome:
    income_source: list[MTRSA106IncomeSource] | None = None
    totals: MTRSA106Totals | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106OverseasTrustIncome:
    income_source: list[MTRSA106IncomeSource] | None = None
    totals: MTRSA106Totals | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106OverseasLandAndPropertyIncomeDetails:
    total_rents_and_other_property_receipts: Decimal | None = None
    property_income_allowance: Decimal | None = None
    traditional_accounting: MTRYesType | None = None
    number_of_properties: int | None = None
    premiums_paid_for_lease: Decimal | None = None
    allowable_property_expenses: Decimal | None = None
    net_profit_or_loss: Decimal | None = None
    private_use_adjustment: Decimal | None = None
    balancing_charges: Decimal | None = None
    capital_allowances: Decimal | None = None
    zero_emission_car_allowance: Decimal | None = None
    zero_emission_goods_vehicle_allowance: Decimal | None = None
    the_structures_and_buildings_allowance: Decimal | None = None
    electric_charge_point_allowance: Decimal | None = None
    costs_of_replacing_domestic_items: Decimal | None = None
    adjusted_profit_or_loss_for_the_year: Decimal | None = None
    residential_finance_costs: Decimal | None = None
    unused_residential_finance_costs_brought_forward: Decimal | None = None
    property_abroad_country: str | None = None
    property_abroad_profit_or_loss: Decimal | None = None
    property_abroad_foreign_tax: Decimal | None = None
    property_abroad_uk_tax_taken_off: Decimal | None = None
    property_abroad_claim_to_ftcr: MTRYesType | None = None
    property_abroad_total_amount: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106ForeignTaxPaid:
    claim_to_ftcr_country_code: str
    claim_to_ftcr_foreign_tax: Decimal | None = None
    claim_to_ftcr_claim_for_ftcr: MTRYesType | None = None
    claim_to_ftcr_amount_chargeable: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106ChargeableGainsUkRules:
    chargeable_gains: Decimal | None = None
    number_of_days_over_which_gain_accrued: int | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106ChargeableGainsForeignRules:
    chargeable_gains: Decimal | None = None
    number_of_days_over_which_gain_accrued: int | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106CapitalGains:
    chargeable_gains_uk_rules: MTRSA106ChargeableGainsUkRules | None = None
    chargeable_gains_foreign_rules: MTRSA106ChargeableGainsForeignRules | None = None
    foreign_tax_paid: Decimal | None = None
    foreign_tax_credit_relief_claim: MTRYesType | None = None
    total_foreign_tax_credit_relief_on_gains: Decimal | None = None
    special_withholding_tax: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA106OtherOverseasIncomeAndGains:
    offshore_fund_gains_and_non_resident_trust_income: Decimal | None = None
    benefits_from_overseas_trusts_etc: Decimal | None = None
    foreign_life_insurance_gains: Decimal | None = None
    number_of_years_since_policy_made: int | None = None
    tax_treated_as_paid: Decimal | None = None
    omitted_amount_transfer_of_assets_exemption: Decimal | None = None


# SA107 - Trusts
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA107:
    income_from_trusts_and_settlements: (
        MTRSA107IncomeFromTrustsAndSettlements | None
    ) = None
    income_chargeable_on_settlors: MTRSA107IncomeChargeableOnSettlors | None = None
    income_from_estates: MTRSA107IncomeFromEstates | None = None
    foreign_tax: Decimal | None = None
    income_from_residential_property: MTRSA107IncomeFromResidentialProperty | None = (
        None
    )
    any_other_information_space: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA107DiscretionaryIncomePayment:
    discretionary_income_payment_net_amount: Decimal | None = None
    payments_from_settlor_interested_trusts: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA107NondiscretionaryIncomeEntitlementFromTrusts:
    non_discretionary_income_taxed_at_basic_rate: Decimal | None = None
    non_discretionary_income_taxed_at_lower_rate: Decimal | None = None
    non_discretionary_income_taxed_at_dividend_rate: Decimal | None = None
    income_from_trusts_etc_non_resident_trustees: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA107IncomeFromTrustsAndSettlements:
    discretionary_income_payment: MTRSA107DiscretionaryIncomePayment | None = None
    nondiscretionary_income_entitlement_from_trusts: (
        MTRSA107NondiscretionaryIncomeEntitlementFromTrusts | None
    ) = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA107IncomeChargeableOnSettlors:
    net_settlor_income_taxed_at_basic_rate: Decimal | None = None
    net_settlor_income_taxed_at_lower_rate: Decimal | None = None
    net_settlor_income_taxed_at_dividend_rate: Decimal | None = None
    net_settlor_income_taxed_at_trust_rate: Decimal | None = None
    savings_income_at_trust_rate: Decimal | None = None
    net_settlor_income_taxed_at_dividend_trust_rate: Decimal | None = None
    gross_settlor_income_to_be_taxed_at_basic_rate: Decimal | None = None
    gross_settlor_income_to_be_taxed_at_lower_rate: Decimal | None = None
    amount_of_uk_life_insurance_policy: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA107UKEstates:
    estate_income_taxed_at_basic_rate: Decimal | None = None
    estate_income_taxed_at_lower_rate: Decimal | None = None
    estate_income_taxed_at_dividend_rate: Decimal | None = None
    estate_income_already_taxed_at_75_dividend_rate: Decimal | None = None
    estate_income_taxed_at_nonrepayable_basic_rate: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA107ForeignEstates:
    foreign_estate_income: Decimal | None = None
    relief_for_uk_tax_accounted_for: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA107IncomeFromEstates:
    uk_estates: MTRSA107UKEstates | None = None
    foreign_estates: MTRSA107ForeignEstates | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA107IncomeFromResidentialProperty:
    residential_property_income_or_restricted_finance_costs: Decimal | None = None
    unused_residential_finance_costs_brought_forward: Decimal | None = None


# SA108 - Capital gains
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA108:
    residential_property_and_carried_interest: (
        MTRSA108ResidentialPropertyAndCarriedInterest | None
    ) = None
    cryptoassets: MTRSA108Cryptoassets | None = None
    other_property_assets_and_gains: MTRSA108OtherPropertyAssetsAndGains | None = None
    listed_shares_and_securities: MTRSA108ListedSharesAndSecurities | None = None
    unlisted_shares_and_securities: MTRSA108UnlistedSharesAndSecurities | None = None
    losses_and_adjustments: MTRSA108LossesAndAdjustments | None = None
    non_resident_cgt_uk_property_or_land_and_indirect_disposals: (
        MTRSA108NrcgtonUkpropertyOrLandAndIndirectDisposals | None
    ) = None
    eis_and_qahc: MTRSA108EisandQahc | None = None
    estimate_or_valuation: MTRYesType | None = None
    any_other_information_space: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA108ResidentialPropertyAndCarriedInterest:
    number_of_disposals: int | None = None
    disposal_proceeds: Decimal | None = None
    allowable_costs: Decimal | None = None
    gains_on_residential_property_in_the_year: Decimal | None = None
    losses_in_the_year: Decimal | None = None
    claim_or_election_made: str | None = None
    gain_or_loss_from_uk_property_disposal: Decimal | None = None
    uk_property_disposal_tax_already_charged: Decimal | None = None
    gain_or_loss_from_rtt_return: Decimal | None = None
    rtt_tax_already_charged: Decimal | None = None
    carried_interest_arising_basis: Decimal | None = None
    carried_interest_accruals_basis: Decimal | None = None
    gains_on_carried_interest_in_the_year: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA108Cryptoassets:
    number_of_disposals: int | None = None
    disposal_proceeds: Decimal | None = None
    allowable_costs: Decimal | None = None
    gains_in_the_year: Decimal | None = None
    losses_in_the_year: Decimal | None = None
    claim_or_election_made: str | None = None
    gain_from_rtt_return: Decimal | None = None
    rtt_tax_already_charged: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA108OtherPropertyAssetsAndGains:
    number_of_disposals: int | None = None
    disposal_proceeds: Decimal | None = None
    allowable_costs: Decimal | None = None
    gains_in_the_year: Decimal | None = None
    non_residential_disposals_included_in_box17: Decimal | None = None
    land_and_property_disposals_where_badr_is_being_claimed: Decimal | None = None
    shares_disposals_where_badr_is_being_claimed: Decimal | None = None
    other_disposals_where_badr_is_being_claimed: Decimal | None = None
    attributed_gains: Decimal | None = None
    losses_in_the_year: Decimal | None = None
    claim_or_election_made: str | None = None
    gain_from_rtt_return: Decimal | None = None
    rtt_tax_already_charged: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA108ListedSharesAndSecurities:
    number_of_disposals: int | None = None
    disposal_proceeds: Decimal | None = None
    allowable_costs: Decimal | None = None
    gains_in_the_year: Decimal | None = None
    losses_in_the_year: Decimal | None = None
    claim_or_election_made: str | None = None
    gain_from_rtt_return: Decimal | None = None
    rtt_tax_already_charged: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA108UnlistedSharesAndSecurities:
    number_of_disposals: int | None = None
    disposal_proceeds: Decimal | None = None
    allowable_costs: Decimal | None = None
    gains_in_the_year: Decimal | None = None
    losses_in_the_year: Decimal | None = None
    claim_or_election_made: str | None = None
    gain_from_rtt_return: Decimal | None = None
    rtt_tax_already_charged: Decimal | None = None
    gains_exceeding_esslimit: Decimal | None = None
    gains_invested_under_seed_eis: Decimal | None = None
    losses_used_against_return_year_income: Decimal | None = None
    seis_and_eis_loss_relief_in_return_year: Decimal | None = None
    losses_used_against_previous_return_year_income: Decimal | None = None
    seis_and_eis_loss_relief_in_previous_return_year: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA108LossesAndAdjustments:
    losses_brought_forward_and_used_in_the_return_year: Decimal | None = None
    income_losses_of_the_return_year_set_against_gains: Decimal | None = None
    losses_to_be_carried_forward: Decimal | None = None
    losses_used_against_earlier_return_years_gain: Decimal | None = None
    gains_qualifying_for_investors_relief: Decimal | None = None
    gains_qualifying_for_business_asset_disposal_relief: Decimal | None = None
    badr_and_er_claimed_to_date: Decimal | None = None
    adjustment_to_cgt: Decimal | None = None
    non_resident_dual_resident_trust_liability: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA108NrcgtonUkpropertyOrLandAndIndirectDisposals:
    total_gains_chargeable_for_direct_disposals_for_uk_residential_property: (
        Decimal | None
    ) = None
    total_gains_chargeable_for_direct_disposals_for_uk_nr_property: Decimal | None = (
        None
    )
    gains_from_indirect_disposals: MTRYesType | None = None
    tax_on_gains_already_charged: Decimal | None = None
    total_losses_available_against_nrcgt_gains_for_the_year: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA108EisandQahc:
    total_gains_from_eis: Decimal | None = None
    total_gains_from_qahc: Decimal | None = None
    total_losses_from_qahc: Decimal | None = None


# SA109 - Residence
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA109:
    residence_status: MTRSA109ResidenceStatus | None = None
    time_spent_in_uk: MTRSA109TimeSpentInUk | None = None
    personal_allowances: MTRSA109PersonalAllowances | None = None
    residence_in_other_countries: MTRSA109ResidenceInOtherCountries | None = None
    domicile: MTRSA109Domicile | None = None
    remittance_basis: MTRSA109RemittanceBasis | None = None
    any_other_information_space: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA109ResidenceStatus:
    not_resident_in_uk: MTRYesType | None = None
    claim_for_overseas_workday_relief: MTRYesType | None = None
    request_for_split_year_treatment: MTRYesType | None = None
    more_than_one_case_of_split_year_treatment_applies: MTRYesType | None = None
    resident_in_uk_for_previous_year: MTRYesType | None = None
    claim_for_overseas_workday_relief_which_includes_py_amount: MTRYesType | None = None
    split_year_treatment_date_from_which_the_uk_part_year_begins_or_ends: (
        date | None
    ) = None
    meet_the_third_automatic_overseas_test: MTRYesType | None = None
    had_a_gap_between_employments_in_this_tax_year: MTRYesType | None = None
    had_a_home_overseas: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA109TimeSpentInUk:
    number_of_days_spent_in_uk: int | None = None
    number_of_days_due_to_exceptional_circumstances: int | None = None
    number_of_days_in_uk_while_in_transit: int | None = None
    how_many_ties_to_uk: int | None = None
    number_of_workdays_in_uk_for_employment: int | None = None
    number_of_workdays_spent_overseas: int | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA109PersonalAllowances:
    code_for_country_of_nationality_or_residence: list[str]
    personal_allowances_claim_due_to_dta: MTRYesType | None = None
    personal_allowances_claim_on_other_basis: MTRYesType | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA109ResidenceInOtherCountries:
    code_for_country_of_residence_for_tax_in_year: list[str]
    code_for_country_of_residence_in_previous_year: list[str]
    amount_of_dta_income_for_which_partial_relief_is_claimed: Decimal | None = None
    dta_relief_claim_residence_in_another_country: Decimal | None = None
    dta_relief_claim_other_provisions: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA109Domicile:
    domiciled_outside_the_uk_for_tax: MTRYesType | None = None
    condition_a: MTRYesType | None = None
    condition_b: MTRYesType | None = None
    years_uk_resident: int | None = None
    first_year_or_always_domiciled_outside_uk: MTRYesType | None = None
    date_domicile_changed: date | None = None
    born_in_uk_but_non_uk_domicile: MTRYesType | None = None
    date_of_coming_to_live_in_uk: date | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA109RemittanceBasisInvestmentInQualifyingBusiness:
    amount_of_relief_claimed_for_investment_in_qualifying_business: Decimal
    company_registration_number: list[str]


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA109RemittanceBasis:
    remittance_basis_claim: MTRYesType | None = None
    unremitted_income_and_gains_unremitted_income_and_gains_under_2000: (
        MTRYesType | None
    ) = None
    deemed_uk_domicile_and_previously_claimed_remittance_basis: MTRYesType | None = None
    uk_resident_for_12_out_of_14_years: MTRYesType | None = None
    uk_resident_for_7_out_of_9_years_uk_resident: MTRYesType | None = None
    less_than18_years: MTRYesType | None = None
    nominated_income_amount: Decimal | None = None
    nominated_capital_gains_amount: Decimal | None = None
    adjustment_to_payments_on_account: Decimal | None = None
    remitted_income_or_gains: MTRYesType | None = None
    investment_in_qualifying_business: (
        MTRSA109RemittanceBasisInvestmentInQualifyingBusiness | None
    ) = None
    previous_investment_no_longer_qualifies: MTRYesType | None = None
    qahc_income_or_gains: MTRYesType | None = None


# SA110 - Tax Calculation Summary
@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA110:
    self_assessment: MTRSA110SelfAssessment
    underpaid_tax: MTRSA110UnderpaidTax
    payments_on_account: MTRSA110PaymentsOnAccount | None = None
    surplus_allowances: MTRSA110SurplusAllowances | None = None
    adjustments_to_tax_due: MTRSA110AdjustmentsToTaxDue | None = None
    any_other_information_space: str | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA110SelfAssessment:
    total_tax_etc_due: Decimal
    student_loan_repayment_due: Decimal | None = None
    postgraduate_loan_repayment_due: Decimal | None = None
    class4_nics_due: Decimal | None = None
    class2_nics_due: Decimal | None = None
    capital_gains_tax_due: Decimal | None = None
    pension_charges_due: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA110UnderpaidTax:
    underpaid_tax_for_earlier_years_included_in_code: Decimal | None = None
    underpaid_tax_for_year_included_in_future_code: Decimal | None = None
    outstanding_debt_coded_out_amount: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA110PaymentsOnAccount:
    claim_to_reduce_payments_on_account: MTRYesType | None = None
    first_payment_on_account: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA110SurplusAllowances:
    surplus_blind_persons_allowance: Decimal | None = None
    surplus_married_couples_allowance: Decimal | None = None


@dataclass(frozen=True, kw_only=True, slots=True)
class MTRSA110AdjustmentsToTaxDue:
    increase_in_tax_from_adjustment_to_earlier_years: Decimal | None = None
    decrease_in_tax_from_adjustment_to_earlier_years: Decimal | None = None
    next_years_repayment_claimed_now: Decimal | None = None
