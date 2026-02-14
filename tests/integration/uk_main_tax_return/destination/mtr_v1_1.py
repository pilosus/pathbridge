from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1"


class AttachmentFileFormat(Enum):
    PDF = "pdf"


class IrheaderDefaultCurrency(Enum):
    """
    :cvar GBP: Sterling
    """

    GBP = "GBP"


class IrheaderSender(Enum):
    """
    :cvar INDIVIDUAL: Individual
    :cvar COMPANY: Company
    :cvar AGENT: Agent
    :cvar BUREAU: Bureau
    :cvar PARTNERSHIP: Partnership
    :cvar TRUST: Trust
    :cvar EMPLOYER: Employer
    :cvar GOVERNMENT: Government
    :cvar ACTING_IN_CAPACITY: Acting in Capacity
    :cvar OTHER: Other
    """

    INDIVIDUAL = "Individual"
    COMPANY = "Company"
    AGENT = "Agent"
    BUREAU = "Bureau"
    PARTNERSHIP = "Partnership"
    TRUST = "Trust"
    EMPLOYER = "Employer"
    GOVERNMENT = "Government"
    ACTING_IN_CAPACITY = "Acting in Capacity"
    OTHER = "Other"


class IrmarkType(Enum):
    """
    :cvar SAONLY: SAonly
    :cvar GENERIC: generic
    """

    SAONLY = "SAonly"
    GENERIC = "generic"


@dataclass(kw_only=True)
class MtrSa106SourceOfForeignIncomeTotals:
    class Meta:
        name = "MTR_SA106SourceOfForeignIncomeTotals"

    swtor_uktax: None | str = field(
        default=None,
        metadata={
            "name": "SWTOrUKTax",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
            "min_exclusive": "0.00",
            "max_exclusive": "10000000000.00",
            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
        },
    )
    taxable_amount: None | str = field(
        default=None,
        metadata={
            "name": "TaxableAmount",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
            "min_inclusive": "0.00",
            "max_exclusive": "10000000000.00",
            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
        },
    )


@dataclass(kw_only=True)
class MtrSa106SourceOfForeignIncomeTotalsRemitted:
    class Meta:
        name = "MTR_SA106SourceOfForeignIncomeTotalsRemitted"

    swtor_uktax: None | str = field(
        default=None,
        metadata={
            "name": "SWTOrUKTax",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
            "min_exclusive": "0.00",
            "max_exclusive": "10000000000.00",
            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
        },
    )
    taxable_amount: None | str = field(
        default=None,
        metadata={
            "name": "TaxableAmount",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
            "min_inclusive": "0.00",
            "max_exclusive": "10000000000.00",
            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
        },
    )


@dataclass(kw_only=True)
class MtrSaaddressStructure:
    """
    Included since the HMRC core InternationalAddressStructure does not
    provide the correct format.
    """

    class Meta:
        name = "MTR_SAaddressStructure"

    line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
            "min_occurs": 1,
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 28,
            "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
        },
    )
    short_line: None | str = field(
        default=None,
        metadata={
            "name": "ShortLine",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
            "min_length": 1,
            "max_length": 18,
            "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
        },
    )
    post_code: None | str = field(
        default=None,
        metadata={
            "name": "PostCode",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
            "max_length": 8,
            "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
        },
    )


class MtrWorkHomeType(Enum):
    HOME = "home"
    WORK = "work"


class MtrYesNoType(Enum):
    NO = "no"
    YES = "yes"


class MtrYesType(Enum):
    YES = "yes"


class StudentLoanRepaymentsPlanType(Enum):
    """
    :cvar VALUE_01: Plan type 1
    :cvar VALUE_02: Plan type 2
    :cvar VALUE_04: Plan type 4
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_04 = "04"


class StudentLoanRepaymentsPostgraduateLoanPlanType(Enum):
    """
    :cvar VALUE_03: Plan type 3
    """

    VALUE_03 = "03"


class YourPersonalDetailsTaxpayerStatus(Enum):
    """
    :cvar C: Welsh
    :cvar S: Scottish
    :cvar U: Rest of UK
    """

    C = "C"
    S = "S"
    U = "U"


@dataclass(kw_only=True)
class Mtr:
    class Meta:
        name = "MTR"
        namespace = "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1"

    sa100: Mtr.Sa100 = field(
        metadata={
            "name": "SA100",
            "type": "Element",
            "required": True,
        }
    )
    sa101: None | Mtr.Sa101 = field(
        default=None,
        metadata={
            "name": "SA101",
            "type": "Element",
        },
    )
    sa102: list[Mtr.Sa102] = field(
        default_factory=list,
        metadata={
            "name": "SA102",
            "type": "Element",
            "max_occurs": 50,
        },
    )
    sa102_m: list[Mtr.Sa102M] = field(
        default_factory=list,
        metadata={
            "name": "SA102M",
            "type": "Element",
            "max_occurs": 50,
        },
    )
    sa103_f: list[Mtr.Sa103F] = field(
        default_factory=list,
        metadata={
            "name": "SA103F",
            "type": "Element",
            "max_occurs": 50,
        },
    )
    sa103_s: list[Mtr.Sa103S] = field(
        default_factory=list,
        metadata={
            "name": "SA103S",
            "type": "Element",
            "max_occurs": 50,
        },
    )
    sa103_l: None | Mtr.Sa103L = field(
        default=None,
        metadata={
            "name": "SA103L",
            "type": "Element",
        },
    )
    sa104_f: list[Mtr.Sa104F] = field(
        default_factory=list,
        metadata={
            "name": "SA104F",
            "type": "Element",
            "max_occurs": 50,
        },
    )
    sa104_s: list[Mtr.Sa104S] = field(
        default_factory=list,
        metadata={
            "name": "SA104S",
            "type": "Element",
            "max_occurs": 50,
        },
    )
    sa105: None | Mtr.Sa105 = field(
        default=None,
        metadata={
            "name": "SA105",
            "type": "Element",
        },
    )
    sa106: None | Mtr.Sa106 = field(
        default=None,
        metadata={
            "name": "SA106",
            "type": "Element",
        },
    )
    sa107: None | Mtr.Sa107 = field(
        default=None,
        metadata={
            "name": "SA107",
            "type": "Element",
        },
    )
    sa108: None | Mtr.Sa108 = field(
        default=None,
        metadata={
            "name": "SA108",
            "type": "Element",
        },
    )
    sa109: None | Mtr.Sa109 = field(
        default=None,
        metadata={
            "name": "SA109",
            "type": "Element",
        },
    )
    sa110: Mtr.Sa110 = field(
        metadata={
            "name": "SA110",
            "type": "Element",
            "required": True,
        }
    )
    welsh_return: None | MtrYesType = field(
        default=None,
        metadata={
            "name": "WelshReturn",
            "type": "Element",
        },
    )
    taxpayer_name: None | str = field(
        default=None,
        metadata={
            "name": "TaxpayerName",
            "type": "Element",
            "max_length": 56,
            "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
        },
    )
    declaration: Mtr.Declaration = field(
        metadata={
            "name": "Declaration",
            "type": "Element",
            "required": True,
        }
    )
    attached_files: None | Mtr.AttachedFiles = field(
        default=None,
        metadata={
            "name": "AttachedFiles",
            "type": "Element",
        },
    )
    amended_return: None | MtrYesType = field(
        default=None,
        metadata={
            "name": "AmendedReturn",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Sa100:
        your_personal_details: Mtr.Sa100.YourPersonalDetails = field(
            metadata={
                "name": "YourPersonalDetails",
                "type": "Element",
                "required": True,
            }
        )
        your_tax_return: None | Mtr.Sa100.YourTaxReturn = field(
            default=None,
            metadata={
                "name": "YourTaxReturn",
                "type": "Element",
            },
        )
        student_loan_repayments: None | Mtr.Sa100.StudentLoanRepayments = field(
            default=None,
            metadata={
                "name": "StudentLoanRepayments",
                "type": "Element",
            },
        )
        income: None | Mtr.Sa100.Income = field(
            default=None,
            metadata={
                "name": "Income",
                "type": "Element",
            },
        )
        tax_reliefs: None | Mtr.Sa100.TaxReliefs = field(
            default=None,
            metadata={
                "name": "TaxReliefs",
                "type": "Element",
            },
        )
        high_income_child_benefit_charge: (
            None | Mtr.Sa100.HighIncomeChildBenefitCharge
        ) = field(
            default=None,
            metadata={
                "name": "HighIncomeChildBenefitCharge",
                "type": "Element",
            },
        )
        winter_fuel_payment_or_pensions_age_winter_heating_payment_received: (
            None | str
        ) = field(
            default=None,
            metadata={
                "name": "WinterFuelPaymentOrPensionsAgeWinterHeatingPaymentReceived",
                "type": "Element",
                "min_exclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        marriage_allowance: None | Mtr.Sa100.MarriageAllowance = field(
            default=None,
            metadata={
                "name": "MarriageAllowance",
                "type": "Element",
            },
        )
        marriage_allowance_transferred_in: None | MtrYesType = field(
            default=None,
            metadata={
                "name": "MarriageAllowanceTransferredIn",
                "type": "Element",
            },
        )
        marriage_allowance_transferred_out: None | MtrYesType = field(
            default=None,
            metadata={
                "name": "MarriageAllowanceTransferredOut",
                "type": "Element",
            },
        )
        finishing_your_tax_return: None | Mtr.Sa100.FinishingYourTaxReturn = field(
            default=None,
            metadata={
                "name": "FinishingYourTaxReturn",
                "type": "Element",
            },
        )
        chargeable_event_gains: None | str = field(
            default=None,
            metadata={
                "name": "ChargeableEventGains",
                "type": "Element",
                "min_inclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )

        @dataclass(kw_only=True)
        class YourPersonalDetails:
            date_of_birth: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateOfBirth",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            new_address: None | Mtr.Sa100.YourPersonalDetails.NewAddress = field(
                default=None,
                metadata={
                    "name": "NewAddress",
                    "type": "Element",
                },
            )
            telephone_number: None | str = field(
                default=None,
                metadata={
                    "name": "TelephoneNumber",
                    "type": "Element",
                    "max_length": 20,
                    "pattern": r"[0-9 ]{1,20}",
                },
            )
            national_insurance_number: None | str = field(
                default=None,
                metadata={
                    "name": "NationalInsuranceNumber",
                    "type": "Element",
                    "pattern": r"([A-Z]{2}[0-9]{6}[A-Z]?)|([0-9]{2}[A-Z][0-9]{5})",
                },
            )
            taxpayer_status: YourPersonalDetailsTaxpayerStatus = field(
                metadata={
                    "name": "TaxpayerStatus",
                    "type": "Element",
                    "required": True,
                }
            )

            @dataclass(kw_only=True)
            class NewAddress:
                address_line1: str = field(
                    metadata={
                        "name": "AddressLine1",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 28,
                        "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                    }
                )
                address_line2: str = field(
                    metadata={
                        "name": "AddressLine2",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 28,
                        "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                    }
                )
                address_line3: None | str = field(
                    default=None,
                    metadata={
                        "name": "AddressLine3",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 28,
                        "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                    },
                )
                address_line4: None | str = field(
                    default=None,
                    metadata={
                        "name": "AddressLine4",
                        "type": "Element",
                        "max_length": 18,
                        "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                    },
                )
                postcode: None | str = field(
                    default=None,
                    metadata={
                        "name": "Postcode",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 8,
                        "pattern": r"(GIR 0AA)|((([A-Z][0-9][0-9]?)|(([A-Z][A-HJ-Y][0-9][0-9]?)|(([A-Z][0-9][A-Z])|([A-Z][A-HJ-Y][0-9]?[A-Z])))) [0-9][A-Z]{2})",
                    },
                )
                effective_from: XmlDate = field(
                    metadata={
                        "name": "EffectiveFrom",
                        "type": "Element",
                        "required": True,
                        "min_inclusive": XmlDate(1851, 1, 1),
                        "max_inclusive": XmlDate(2040, 1, 1),
                    }
                )

        @dataclass(kw_only=True)
        class YourTaxReturn:
            employment_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "EmploymentSchedule",
                    "type": "Element",
                },
            )
            number_of_employment_schedules: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfEmploymentSchedules",
                    "type": "Element",
                    "min_inclusive": 1,
                    "max_inclusive": 50,
                },
            )
            minister_of_religion_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "MinisterOfReligionSchedule",
                    "type": "Element",
                },
            )
            number_of_minister_of_religion_schedules: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfMinisterOfReligionSchedules",
                    "type": "Element",
                    "min_inclusive": 1,
                    "max_inclusive": 50,
                },
            )
            full_self_employment_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "FullSelfEmploymentSchedule",
                    "type": "Element",
                },
            )
            number_of_full_self_employment_schedules: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfFullSelfEmploymentSchedules",
                    "type": "Element",
                    "min_inclusive": 1,
                    "max_inclusive": 50,
                },
            )
            short_self_employment_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ShortSelfEmploymentSchedule",
                    "type": "Element",
                },
            )
            number_of_short_self_employment_schedules: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfShortSelfEmploymentSchedules",
                    "type": "Element",
                    "min_inclusive": 1,
                    "max_inclusive": 50,
                },
            )
            lloyds_underwriter_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "LloydsUnderwriterSchedule",
                    "type": "Element",
                },
            )
            full_partnership_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "FullPartnershipSchedule",
                    "type": "Element",
                },
            )
            number_of_full_partnership_schedules: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfFullPartnershipSchedules",
                    "type": "Element",
                    "min_inclusive": 1,
                    "max_inclusive": 50,
                },
            )
            short_partnership_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ShortPartnershipSchedule",
                    "type": "Element",
                },
            )
            number_of_short_partnership_schedules: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfShortPartnershipSchedules",
                    "type": "Element",
                    "min_inclusive": 1,
                    "max_inclusive": 50,
                },
            )
            ukproperty_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "UKPropertySchedule",
                    "type": "Element",
                },
            )
            foreign_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ForeignSchedule",
                    "type": "Element",
                },
            )
            trusts_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "TrustsSchedule",
                    "type": "Element",
                },
            )
            capital_gains_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "CapitalGainsSchedule",
                    "type": "Element",
                },
            )
            capital_gains_computation_attached: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "CapitalGainsComputationAttached",
                    "type": "Element",
                },
            )
            residence_figschedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ResidenceFIGschedule",
                    "type": "Element",
                },
            )
            additional_information_schedule: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "AdditionalInformationSchedule",
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class StudentLoanRepayments:
            income_contingent_student_loan_notification: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "IncomeContingentStudentLoanNotification",
                    "type": "Element",
                },
            )
            student_loan_repayment_deducted_amount: None | str = field(
                default=None,
                metadata={
                    "name": "StudentLoanRepaymentDeductedAmount",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            postgraduate_loan_repayment_deducted_amount: None | str = field(
                default=None,
                metadata={
                    "name": "PostgraduateLoanRepaymentDeductedAmount",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            plan_type: None | StudentLoanRepaymentsPlanType = field(
                default=None,
                metadata={
                    "name": "PlanType",
                    "type": "Element",
                },
            )
            postgraduate_loan_plan_type: (
                None | StudentLoanRepaymentsPostgraduateLoanPlanType
            ) = field(
                default=None,
                metadata={
                    "name": "PostgraduateLoanPlanType",
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class Income:
            ukinterest_and_dividends: None | Mtr.Sa100.Income.UkinterestAndDividends = (
                field(
                    default=None,
                    metadata={
                        "name": "UKInterestAndDividends",
                        "type": "Element",
                    },
                )
            )
            state_benefits: None | Mtr.Sa100.Income.StateBenefits = field(
                default=None,
                metadata={
                    "name": "StateBenefits",
                    "type": "Element",
                },
            )
            other_ukincome: None | Mtr.Sa100.Income.OtherUkincome = field(
                default=None,
                metadata={
                    "name": "OtherUKIncome",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class UkinterestAndDividends:
                taxed_bank_building_society_etc_interest: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxedBankBuildingSocietyEtcInterest",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                untaxed_ukinterest_etc: None | str = field(
                    default=None,
                    metadata={
                        "name": "UntaxedUKinterestEtc",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                untaxed_foreign_interest: None | str = field(
                    default=None,
                    metadata={
                        "name": "UntaxedForeignInterest",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                company_dividends: None | str = field(
                    default=None,
                    metadata={
                        "name": "CompanyDividends",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                unit_trust_etc_dividends: None | str = field(
                    default=None,
                    metadata={
                        "name": "UnitTrustEtcDividends",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_dividends: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignDividends",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                tax_taken_off_foreign_dividends: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxTakenOffForeignDividends",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class StateBenefits:
                annual_state_pension: None | str = field(
                    default=None,
                    metadata={
                        "name": "AnnualStatePension",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                state_pension_lump_sum: None | str = field(
                    default=None,
                    metadata={
                        "name": "StatePensionLumpSum",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                tax_taken_off_pension_lump_sum: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxTakenOffPensionLumpSum",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                other_pensions_and_retirement_annuities: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherPensionsAndRetirementAnnuities",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                tax_taken_off_pensions_and_retirement_annuities: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxTakenOffPensionsAndRetirementAnnuities",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                incapacity_benefit: None | str = field(
                    default=None,
                    metadata={
                        "name": "IncapacityBenefit",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                tax_taken_off_incapacity_benefit: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxTakenOffIncapacityBenefit",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                jobseekers_allowance: None | str = field(
                    default=None,
                    metadata={
                        "name": "JobseekersAllowance",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                other_state_pensions_and_benefits: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherStatePensionsAndBenefits",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class OtherUkincome:
                other_taxable_income_details: (
                    None | Mtr.Sa100.Income.OtherUkincome.OtherTaxableIncomeDetails
                ) = field(
                    default=None,
                    metadata={
                        "name": "OtherTaxableIncomeDetails",
                        "type": "Element",
                    },
                )
                allowable_expenses: None | str = field(
                    default=None,
                    metadata={
                        "name": "AllowableExpenses",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                deemed_income_or_benefits: None | str = field(
                    default=None,
                    metadata={
                        "name": "DeemedIncomeOrBenefits",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                description_of_other_income: None | str = field(
                    default=None,
                    metadata={
                        "name": "DescriptionOfOtherIncome",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 240,
                        "pattern": r".*[^\s]+.*",
                    },
                )

                @dataclass(kw_only=True)
                class OtherTaxableIncomeDetails:
                    other_taxable_income: str = field(
                        metadata={
                            "name": "OtherTaxableIncome",
                            "type": "Element",
                            "required": True,
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        }
                    )
                    tax_taken_off_other_taxable_income: None | str = field(
                        default=None,
                        metadata={
                            "name": "TaxTakenOffOtherTaxableIncome",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )

        @dataclass(kw_only=True)
        class TaxReliefs:
            pensions: None | Mtr.Sa100.TaxReliefs.Pensions = field(
                default=None,
                metadata={
                    "name": "Pensions",
                    "type": "Element",
                },
            )
            charitable_giving: None | Mtr.Sa100.TaxReliefs.CharitableGiving = field(
                default=None,
                metadata={
                    "name": "CharitableGiving",
                    "type": "Element",
                },
            )
            blind_persons_allowance: (
                None | Mtr.Sa100.TaxReliefs.BlindPersonsAllowance
            ) = field(
                default=None,
                metadata={
                    "name": "BlindPersonsAllowance",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Pensions:
                payments_to_registered_pension_schemes: None | str = field(
                    default=None,
                    metadata={
                        "name": "PaymentsToRegisteredPensionSchemes",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                one_off_registered_pension_schemes_payments: None | str = field(
                    default=None,
                    metadata={
                        "name": "OneOffRegisteredPensionSchemesPayments",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                retirement_annuity_contract_payments: None | str = field(
                    default=None,
                    metadata={
                        "name": "RetirementAnnuityContractPayments",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                employer_pension_scheme_payments: None | str = field(
                    default=None,
                    metadata={
                        "name": "EmployerPensionSchemePayments",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                non_ukoverseas_pension_scheme_payments: None | str = field(
                    default=None,
                    metadata={
                        "name": "NonUKOverseasPensionSchemePayments",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class CharitableGiving:
                gift_aid_payments_made_in_year: None | str = field(
                    default=None,
                    metadata={
                        "name": "GiftAidPaymentsMadeInYear",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                one_off_gift_aid_payments: None | str = field(
                    default=None,
                    metadata={
                        "name": "OneOffGiftAidPayments",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                gift_aid_payments_carried_back_to_previous_year: None | str = field(
                    default=None,
                    metadata={
                        "name": "GiftAidPaymentsCarriedBackToPreviousYear",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                gift_aid_payments_brought_back_from_later_year: None | str = field(
                    default=None,
                    metadata={
                        "name": "GiftAidPaymentsBroughtBackFromLaterYear",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                shares_gifted_to_charity: None | str = field(
                    default=None,
                    metadata={
                        "name": "SharesGiftedToCharity",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                land_and_buildings_gifted_to_charity: None | str = field(
                    default=None,
                    metadata={
                        "name": "LandAndBuildingsGiftedToCharity",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class BlindPersonsAllowance:
                blind_persons_allowance_details: (
                    None
                    | Mtr.Sa100.TaxReliefs.BlindPersonsAllowance.BlindPersonsAllowanceDetails
                ) = field(
                    default=None,
                    metadata={
                        "name": "BlindPersonsAllowanceDetails",
                        "type": "Element",
                    },
                )
                surplus_blind_persons_allowance_from_spouse: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "SurplusBlindPersonsAllowanceFromSpouse",
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class BlindPersonsAllowanceDetails:
                    registered_blind: None | MtrYesType = field(
                        default=None,
                        metadata={
                            "name": "RegisteredBlind",
                            "type": "Element",
                        },
                    )
                    surplus_blind_persons_allowance_to_spouse: None | MtrYesType = (
                        field(
                            default=None,
                            metadata={
                                "name": "SurplusBlindPersonsAllowanceToSpouse",
                                "type": "Element",
                            },
                        )
                    )
                    local_authority_name: None | str = field(
                        default=None,
                        metadata={
                            "name": "LocalAuthorityName",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 28,
                            "pattern": r".*[^\s]+.*",
                        },
                    )

        @dataclass(kw_only=True)
        class HighIncomeChildBenefitCharge:
            amount_received: None | str = field(
                default=None,
                metadata={
                    "name": "AmountReceived",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            number_of_children: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfChildren",
                    "type": "Element",
                    "max_inclusive": 99,
                },
            )
            date_stopped_receiving_all_child_benefit_payments: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateStoppedReceivingAllChildBenefitPayments",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )

        @dataclass(kw_only=True)
        class MarriageAllowance:
            spouse_first_name: str = field(
                metadata={
                    "name": "SpouseFirstName",
                    "type": "Element",
                    "required": True,
                    "max_length": 35,
                    "pattern": r".*[^\s]+.*",
                }
            )
            spouse_last_name: str = field(
                metadata={
                    "name": "SpouseLastName",
                    "type": "Element",
                    "required": True,
                    "max_length": 35,
                    "pattern": r".*[^\s]+.*",
                }
            )
            spouse_nino: str = field(
                metadata={
                    "name": "SpouseNINO",
                    "type": "Element",
                    "required": True,
                    "pattern": r"([A-Z]{2}[0-9]{6}[A-Z]?)|([0-9]{2}[A-Z][0-9]{5})",
                }
            )
            spouse_date_of_birth: XmlDate = field(
                metadata={
                    "name": "SpouseDateOfBirth",
                    "type": "Element",
                    "required": True,
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                }
            )
            date_of_marriage_or_civil_partnership: XmlDate = field(
                metadata={
                    "name": "DateOfMarriageOrCivilPartnership",
                    "type": "Element",
                    "required": True,
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                }
            )

        @dataclass(kw_only=True)
        class FinishingYourTaxReturn:
            tax_refunded_or_set_off: None | str = field(
                default=None,
                metadata={
                    "name": "TaxRefundedOrSetOff",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            not_paid_enough: None | Mtr.Sa100.FinishingYourTaxReturn.NotPaidEnough = (
                field(
                    default=None,
                    metadata={
                        "name": "NotPaidEnough",
                        "type": "Element",
                    },
                )
            )
            paid_too_much: None | Mtr.Sa100.FinishingYourTaxReturn.PaidTooMuch = field(
                default=None,
                metadata={
                    "name": "PaidTooMuch",
                    "type": "Element",
                },
            )
            tax_adviser: None | Mtr.Sa100.FinishingYourTaxReturn.TaxAdviser = field(
                default=None,
                metadata={
                    "name": "TaxAdviser",
                    "type": "Element",
                },
            )
            signing_your_form: (
                None | Mtr.Sa100.FinishingYourTaxReturn.SigningYourForm
            ) = field(
                default=None,
                metadata={
                    "name": "SigningYourForm",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class NotPaidEnough:
                tax_owed_not_to_be_coded_out: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "TaxOwedNotToBeCodedOut",
                        "type": "Element",
                    },
                )
                non_payeincome_not_to_be_coded_out: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "NonPAYEIncomeNotToBeCodedOut",
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class PaidTooMuch:
                payment_details: (
                    None | Mtr.Sa100.FinishingYourTaxReturn.PaidTooMuch.PaymentDetails
                ) = field(
                    default=None,
                    metadata={
                        "name": "PaymentDetails",
                        "type": "Element",
                    },
                )
                no_bank_or_building_society_account: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "NoBankOrBuildingSocietyAccount",
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class PaymentDetails:
                    bank_account_details: (
                        None
                        | Mtr.Sa100.FinishingYourTaxReturn.PaidTooMuch.PaymentDetails.BankAccountDetails
                    ) = field(
                        default=None,
                        metadata={
                            "name": "BankAccountDetails",
                            "type": "Element",
                        },
                    )
                    nominee_details: (
                        None
                        | Mtr.Sa100.FinishingYourTaxReturn.PaidTooMuch.PaymentDetails.NomineeDetails
                    ) = field(
                        default=None,
                        metadata={
                            "name": "NomineeDetails",
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class BankAccountDetails:
                        bank_or_building_society_name: str = field(
                            metadata={
                                "name": "BankOrBuildingSocietyName",
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 28,
                                "pattern": r".*[^\s]+.*",
                            }
                        )
                        account_holder_or_nominee_name: str = field(
                            metadata={
                                "name": "AccountHolderOrNomineeName",
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 28,
                                "pattern": r".*[^\s]+.*",
                            }
                        )
                        branch_sort_code: str = field(
                            metadata={
                                "name": "BranchSortCode",
                                "type": "Element",
                                "required": True,
                                "length": 6,
                                "pattern": r"[0-9]{6}",
                            }
                        )
                        account_number: str = field(
                            metadata={
                                "name": "AccountNumber",
                                "type": "Element",
                                "required": True,
                                "length": 8,
                                "pattern": r"[0-9]{8}",
                            }
                        )
                        building_society_reference_number: None | str = field(
                            default=None,
                            metadata={
                                "name": "BuildingSocietyReferenceNumber",
                                "type": "Element",
                                "min_length": 1,
                                "pattern": r"[A-Z0-9\-/]{1,18}",
                            },
                        )

                    @dataclass(kw_only=True)
                    class NomineeDetails:
                        nominee_name_given: MtrYesType = field(
                            metadata={
                                "name": "NomineeNameGiven",
                                "type": "Element",
                                "required": True,
                            }
                        )
                        nominee_is_tax_adviser: None | MtrYesType = field(
                            default=None,
                            metadata={
                                "name": "NomineeIsTaxAdviser",
                                "type": "Element",
                            },
                        )
                        nominee_address: MtrSaaddressStructure = field(
                            metadata={
                                "name": "NomineeAddress",
                                "type": "Element",
                                "required": True,
                            }
                        )

            @dataclass(kw_only=True)
            class TaxAdviser:
                tax_adviser: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxAdviser",
                        "type": "Element",
                        "max_length": 56,
                        "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                    },
                )
                tax_adviser_phone_number: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxAdviserPhoneNumber",
                        "type": "Element",
                        "max_length": 20,
                        "pattern": r"[0-9 ]{1,20}",
                    },
                )
                tax_adviser_address: None | MtrSaaddressStructure = field(
                    default=None,
                    metadata={
                        "name": "TaxAdviserAddress",
                        "type": "Element",
                    },
                )
                tax_advisers_reference: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxAdvisersReference",
                        "type": "Element",
                        "max_length": 20,
                        "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                    },
                )

            @dataclass(kw_only=True)
            class SigningYourForm:
                other_information_space: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherInformationSpace",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 20480,
                        "pattern": r".*[^\s]+.*",
                    },
                )
                provisional_figures: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "ProvisionalFigures",
                        "type": "Element",
                    },
                )
                capacity_of_person_signing: None | str = field(
                    default=None,
                    metadata={
                        "name": "CapacityOfPersonSigning",
                        "type": "Element",
                        "max_length": 28,
                        "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                    },
                )
                name_of_person_signed_for: None | str = field(
                    default=None,
                    metadata={
                        "name": "NameOfPersonSignedFor",
                        "type": "Element",
                        "max_length": 28,
                        "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                    },
                )
                name_of_person_signing: None | str = field(
                    default=None,
                    metadata={
                        "name": "NameOfPersonSigning",
                        "type": "Element",
                        "max_length": 28,
                        "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                    },
                )
                address_of_person_signing: None | MtrSaaddressStructure = field(
                    default=None,
                    metadata={
                        "name": "AddressOfPersonSigning",
                        "type": "Element",
                    },
                )

    @dataclass(kw_only=True)
    class Sa101:
        gilt_edge_securities_interest: None | Mtr.Sa101.GiltEdgeSecuritiesInterest = (
            field(
                default=None,
                metadata={
                    "name": "GiltEdgeSecuritiesInterest",
                    "type": "Element",
                },
            )
        )
        life_insurance_gains: None | Mtr.Sa101.LifeInsuranceGains = field(
            default=None,
            metadata={
                "name": "LifeInsuranceGains",
                "type": "Element",
            },
        )
        stock_distributions_and_loans_written_off: (
            None | Mtr.Sa101.StockDistributionsAndLoansWrittenOff
        ) = field(
            default=None,
            metadata={
                "name": "StockDistributionsAndLoansWrittenOff",
                "type": "Element",
            },
        )
        business_taxed_income: None | Mtr.Sa101.BusinessTaxedIncome = field(
            default=None,
            metadata={
                "name": "BusinessTaxedIncome",
                "type": "Element",
            },
        )
        shares_employment_compensations_and_deductions: (
            None | Mtr.Sa101.SharesEmploymentCompensationsAndDeductions
        ) = field(
            default=None,
            metadata={
                "name": "SharesEmploymentCompensationsAndDeductions",
                "type": "Element",
            },
        )
        other_tax_reliefs: None | Mtr.Sa101.OtherTaxReliefs = field(
            default=None,
            metadata={
                "name": "OtherTaxReliefs",
                "type": "Element",
            },
        )
        age_related_married_couples_allowance: (
            None | Mtr.Sa101.AgeRelatedMarriedCouplesAllowance
        ) = field(
            default=None,
            metadata={
                "name": "AgeRelatedMarriedCouplesAllowance",
                "type": "Element",
            },
        )
        other_information: None | Mtr.Sa101.OtherInformation = field(
            default=None,
            metadata={
                "name": "OtherInformation",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class GiltEdgeSecuritiesInterest:
            net_gilt_interest: None | str = field(
                default=None,
                metadata={
                    "name": "NetGiltInterest",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            tax_taken_off_gilt_interest: None | str = field(
                default=None,
                metadata={
                    "name": "TaxTakenOffGiltInterest",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gross_gilt_interest: None | str = field(
                default=None,
                metadata={
                    "name": "GrossGiltInterest",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class LifeInsuranceGains:
            life_insurance_gains_tax_treated_as_paid: (
                None | Mtr.Sa101.LifeInsuranceGains.LifeInsuranceGainsTaxTreatedAsPaid
            ) = field(
                default=None,
                metadata={
                    "name": "LifeInsuranceGainsTaxTreatedAsPaid",
                    "type": "Element",
                },
            )
            life_insurance_gains_no_tax_treated_as_paid: (
                None | Mtr.Sa101.LifeInsuranceGains.LifeInsuranceGainsNoTaxTreatedAsPaid
            ) = field(
                default=None,
                metadata={
                    "name": "LifeInsuranceGainsNoTaxTreatedAsPaid",
                    "type": "Element",
                },
            )
            life_insurance_gains_from_voided_isas: (
                None | Mtr.Sa101.LifeInsuranceGains.LifeInsuranceGainsFromVoidedIsas
            ) = field(
                default=None,
                metadata={
                    "name": "LifeInsuranceGainsFromVoidedISAs",
                    "type": "Element",
                },
            )
            tax_taken_off_gains_from_voided_isas: None | str = field(
                default=None,
                metadata={
                    "name": "TaxTakenOffGainsFromVoidedISAs",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            deficiency_relief: None | str = field(
                default=None,
                metadata={
                    "name": "DeficiencyRelief",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

            @dataclass(kw_only=True)
            class LifeInsuranceGainsTaxTreatedAsPaid:
                amount_of_gain: None | str = field(
                    default=None,
                    metadata={
                        "name": "AmountOfGain",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                number_of_years: None | int = field(
                    default=None,
                    metadata={
                        "name": "NumberOfYears",
                        "type": "Element",
                        "min_inclusive": 1,
                        "max_inclusive": 99,
                    },
                )

            @dataclass(kw_only=True)
            class LifeInsuranceGainsNoTaxTreatedAsPaid:
                amount_of_gain: None | str = field(
                    default=None,
                    metadata={
                        "name": "AmountOfGain",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                number_of_years: None | int = field(
                    default=None,
                    metadata={
                        "name": "NumberOfYears",
                        "type": "Element",
                        "min_inclusive": 1,
                        "max_inclusive": 99,
                    },
                )

            @dataclass(kw_only=True)
            class LifeInsuranceGainsFromVoidedIsas:
                amount_of_gain: None | str = field(
                    default=None,
                    metadata={
                        "name": "AmountOfGain",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                number_of_years: None | int = field(
                    default=None,
                    metadata={
                        "name": "NumberOfYears",
                        "type": "Element",
                        "min_inclusive": 1,
                        "max_inclusive": 99,
                    },
                )

        @dataclass(kw_only=True)
        class StockDistributionsAndLoansWrittenOff:
            stock_dividends: None | str = field(
                default=None,
                metadata={
                    "name": "StockDividends",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            bonus_issues_of_securities_and_redeemable_shares: None | str = field(
                default=None,
                metadata={
                    "name": "BonusIssuesOfSecuritiesAndRedeemableShares",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            close_company_loans_written_off_or_released: None | str = field(
                default=None,
                metadata={
                    "name": "CloseCompanyLoansWrittenOffOrReleased",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class BusinessTaxedIncome:
            post_cessation_or_other_business_receipts: str = field(
                metadata={
                    "name": "PostCessationOrOtherBusinessReceipts",
                    "type": "Element",
                    "required": True,
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                }
            )
            tax_year_income_to_be_taxed: str = field(
                metadata={
                    "name": "TaxYearIncomeToBeTaxed",
                    "type": "Element",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}",
                }
            )

        @dataclass(kw_only=True)
        class SharesEmploymentCompensationsAndDeductions:
            share_schemes_taxable_amount: None | str = field(
                default=None,
                metadata={
                    "name": "ShareSchemesTaxableAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            lump_sums: (
                None | Mtr.Sa101.SharesEmploymentCompensationsAndDeductions.LumpSums
            ) = field(
                default=None,
                metadata={
                    "name": "LumpSums",
                    "type": "Element",
                },
            )
            tax_taken_off_lump_sums_left_blank: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "TaxTakenOffLumpSumsLeftBlank",
                    "type": "Element",
                },
            )
            retirement_and_other_exemptions: None | str = field(
                default=None,
                metadata={
                    "name": "RetirementAndOtherExemptions",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            compensation_and_lump_sum_exemption: None | str = field(
                default=None,
                metadata={
                    "name": "CompensationAndLumpSumExemption",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            disability_and_foreign_service_deduction: None | str = field(
                default=None,
                metadata={
                    "name": "DisabilityAndForeignServiceDeduction",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            seafarers_earnings_deduction: None | str = field(
                default=None,
                metadata={
                    "name": "SeafarersEarningsDeduction",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            non_uktaxable_foreign_earnings: None | str = field(
                default=None,
                metadata={
                    "name": "NonUKTaxableForeignEarnings",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            foreign_tax_no_foreign_tax_credit_relief_claim: None | str = field(
                default=None,
                metadata={
                    "name": "ForeignTaxNoForeignTaxCreditReliefClaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            overseas_pension_exempt_employer_contributions: None | str = field(
                default=None,
                metadata={
                    "name": "OverseasPensionExemptEmployerContributions",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            ukpatent_royalty_payments_made: None | str = field(
                default=None,
                metadata={
                    "name": "UKpatentRoyaltyPaymentsMade",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

            @dataclass(kw_only=True)
            class LumpSums:
                lump_sum_salaries_and_other_payments: None | str = field(
                    default=None,
                    metadata={
                        "name": "LumpSumSalariesAndOtherPayments",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                lump_sums_or_benefits_from_retirement_schemes: None | str = field(
                    default=None,
                    metadata={
                        "name": "LumpSumsOrBenefitsFromRetirementSchemes",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                redundancy_and_other_compensation_payments: None | str = field(
                    default=None,
                    metadata={
                        "name": "RedundancyAndOtherCompensationPayments",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                tax_taken_off: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxTakenOff",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class OtherTaxReliefs:
            venture_capital_trust_share_subscriptions: None | str = field(
                default=None,
                metadata={
                    "name": "VentureCapitalTrustShareSubscriptions",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            enterprise_investment_scheme_share_subscriptions: None | str = field(
                default=None,
                metadata={
                    "name": "EnterpriseInvestmentSchemeShareSubscriptions",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            community_investment_trust_relief: None | str = field(
                default=None,
                metadata={
                    "name": "CommunityInvestmentTrustRelief",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            annuities_and_annual_payments: None | str = field(
                default=None,
                metadata={
                    "name": "AnnuitiesAndAnnualPayments",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            qualifying_loan_interest: None | str = field(
                default=None,
                metadata={
                    "name": "QualifyingLoanInterest",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            post_cessation_and_other_losses: None | str = field(
                default=None,
                metadata={
                    "name": "PostCessationAndOtherLosses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            preincorporation_losses: None | str = field(
                default=None,
                metadata={
                    "name": "PreincorporationLosses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            maintenance_or_alimony_payments: None | str = field(
                default=None,
                metadata={
                    "name": "MaintenanceOrAlimonyPayments",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            trade_union_etc_death_benefit_payments: None | str = field(
                default=None,
                metadata={
                    "name": "TradeUnionEtcDeathBenefitPayments",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            bonus_security_redemption_distribution_relief: None | str = field(
                default=None,
                metadata={
                    "name": "BonusSecurityRedemptionDistributionRelief",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            seed_enterprise_investment_scheme_amount: None | str = field(
                default=None,
                metadata={
                    "name": "SeedEnterpriseInvestmentSchemeAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            nondeductible_loan_interest: None | str = field(
                default=None,
                metadata={
                    "name": "NondeductibleLoanInterest",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class AgeRelatedMarriedCouplesAllowance:
            higher_earner: (
                None | Mtr.Sa101.AgeRelatedMarriedCouplesAllowance.HigherEarner
            ) = field(
                default=None,
                metadata={
                    "name": "HigherEarner",
                    "type": "Element",
                },
            )
            lower_earner: (
                None | Mtr.Sa101.AgeRelatedMarriedCouplesAllowance.LowerEarner
            ) = field(
                default=None,
                metadata={
                    "name": "LowerEarner",
                    "type": "Element",
                },
            )
            date_of_marriage_or_civil_partnership: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateOfMarriageOrCivilPartnership",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            surplus_allowance_from_spouse: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "SurplusAllowanceFromSpouse",
                    "type": "Element",
                },
            )
            surplus_allowance_to_spouse: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "SurplusAllowanceToSpouse",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class HigherEarner:
                spouses_name: str = field(
                    metadata={
                        "name": "SpousesName",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 28,
                        "pattern": r".*[^\s]+.*",
                    }
                )
                spouses_date_of_birth: None | XmlDate = field(
                    default=None,
                    metadata={
                        "name": "SpousesDateOfBirth",
                        "type": "Element",
                        "min_inclusive": XmlDate(1851, 1, 1),
                        "max_inclusive": XmlDate(2040, 1, 1),
                    },
                )
                half_minimum_allowance_transfer_to_other: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "HalfMinimumAllowanceTransferToOther",
                        "type": "Element",
                    },
                )
                all_minimum_allowance_transfer_to_other: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "AllMinimumAllowanceTransferToOther",
                        "type": "Element",
                    },
                )
                previous_spouses_date_of_birth: None | XmlDate = field(
                    default=None,
                    metadata={
                        "name": "PreviousSpousesDateOfBirth",
                        "type": "Element",
                        "min_inclusive": XmlDate(1851, 1, 1),
                        "max_inclusive": XmlDate(2040, 1, 1),
                    },
                )

            @dataclass(kw_only=True)
            class LowerEarner:
                half_minimum_allowance_transfer_to_you: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "HalfMinimumAllowanceTransferToYou",
                        "type": "Element",
                    },
                )
                all_minimum_allowance_transfer_to_you: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "AllMinimumAllowanceTransferToYou",
                        "type": "Element",
                    },
                )
                spouses_name: str = field(
                    metadata={
                        "name": "SpousesName",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 28,
                        "pattern": r".*[^\s]+.*",
                    }
                )

        @dataclass(kw_only=True)
        class OtherInformation:
            income_tax_losses: None | Mtr.Sa101.OtherInformation.IncomeTaxLosses = (
                field(
                    default=None,
                    metadata={
                        "name": "IncomeTaxLosses",
                        "type": "Element",
                    },
                )
            )
            amount_of_payroll_giving: None | str = field(
                default=None,
                metadata={
                    "name": "AmountOfPayrollGiving",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            pension_tax_and_lump_sums: (
                None | Mtr.Sa101.OtherInformation.PensionTaxAndLumpSums
            ) = field(
                default=None,
                metadata={
                    "name": "PensionTaxAndLumpSums",
                    "type": "Element",
                },
            )
            tax_avoidance_schemes: list[
                Mtr.Sa101.OtherInformation.TaxAvoidanceSchemes
            ] = field(
                default_factory=list,
                metadata={
                    "name": "TaxAvoidanceSchemes",
                    "type": "Element",
                    "max_occurs": 3,
                },
            )

            @dataclass(kw_only=True)
            class IncomeTaxLosses:
                earlier_years_income_tax_losses: None | str = field(
                    default=None,
                    metadata={
                        "name": "EarlierYearsIncomeTaxLosses",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                unused_income_tax_losses_carried_forward: None | str = field(
                    default=None,
                    metadata={
                        "name": "UnusedIncomeTaxLossesCarriedForward",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                next_years_trading_and_capital_losses_relief: None | str = field(
                    default=None,
                    metadata={
                        "name": "NextYearsTradingAndCapitalLossesRelief",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                next_years_uncapped_loss_relief: None | str = field(
                    default=None,
                    metadata={
                        "name": "NextYearsUncappedLossRelief",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                year_for_which_relief_claimed: None | str = field(
                    default=None,
                    metadata={
                        "name": "YearForWhichReliefClaimed",
                        "type": "Element",
                        "pattern": r"[0-9]{4}-[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class PensionTaxAndLumpSums:
                amount_saved_exceeding_annual_allowance: None | str = field(
                    default=None,
                    metadata={
                        "name": "AmountSavedExceedingAnnualAllowance",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                annual_allowance_tax_paid_by_pension_scheme: None | str = field(
                    default=None,
                    metadata={
                        "name": "AnnualAllowanceTaxPaidByPensionScheme",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                pension_benefit_transferred_subject_to_otc: None | str = field(
                    default=None,
                    metadata={
                        "name": "PensionBenefitTransferredSubjectToOTC",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                tax_paid_by_pension_scheme_on_otc: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxPaidByPensionSchemeOnOTC",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                pension_scheme_tax_ref: None | str = field(
                    default=None,
                    metadata={
                        "name": "PensionSchemeTaxRef",
                        "type": "Element",
                        "max_length": 10,
                        "pattern": r"[A-Za-z0-9]{1,10}",
                    },
                )
                unauthorised_payment_not_subject_to_surcharge: None | str = field(
                    default=None,
                    metadata={
                        "name": "UnauthorisedPaymentNotSubjectToSurcharge",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                unauthorised_payment_subject_to_surcharge: None | str = field(
                    default=None,
                    metadata={
                        "name": "UnauthorisedPaymentSubjectToSurcharge",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax_paid_on_unauthorised_payment: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTaxPaidOnUnauthorisedPayment",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                overseas_pension_contribution_short_service_refund: None | str = field(
                    default=None,
                    metadata={
                        "name": "OverseasPensionContributionShortServiceRefund",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax_paid: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTaxPaid",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class TaxAvoidanceSchemes:
                tax_avoidance_scheme_reference_number: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxAvoidanceSchemeReferenceNumber",
                        "type": "Element",
                        "pattern": r"[0-9]{8}",
                    },
                )
                expected_advantage_tax_year: None | str = field(
                    default=None,
                    metadata={
                        "name": "ExpectedAdvantageTaxYear",
                        "type": "Element",
                        "pattern": r"[0-9]{4}-[0-9]{2}",
                    },
                )

    @dataclass(kw_only=True)
    class Sa102:
        employment: Mtr.Sa102.Employment = field(
            metadata={
                "name": "Employment",
                "type": "Element",
                "required": True,
            }
        )
        benefits: None | Mtr.Sa102.Benefits = field(
            default=None,
            metadata={
                "name": "Benefits",
                "type": "Element",
            },
        )
        expenses: None | Mtr.Sa102.Expenses = field(
            default=None,
            metadata={
                "name": "Expenses",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class Employment:
            pay_from_employment: None | str = field(
                default=None,
                metadata={
                    "name": "PayFromEmployment",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            payrolled_benefits: None | str = field(
                default=None,
                metadata={
                    "name": "PayrolledBenefits",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            tax_taken_off_pay: None | str = field(
                default=None,
                metadata={
                    "name": "TaxTakenOffPay",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_class1_nicable_earnings: None | str = field(
                default=None,
                metadata={
                    "name": "TotalClass1NICableEarnings",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            tips_and_other_payments: None | str = field(
                default=None,
                metadata={
                    "name": "TipsAndOtherPayments",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            employer_payereference: str = field(
                metadata={
                    "name": "EmployerPAYEReference",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 17,
                    "pattern": r".*[^\s]+.*",
                }
            )
            employers_name: None | str = field(
                default=None,
                metadata={
                    "name": "EmployersName",
                    "type": "Element",
                    "max_length": 28,
                    "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                },
            )
            company_director: MtrYesNoType = field(
                metadata={
                    "name": "CompanyDirector",
                    "type": "Element",
                    "required": True,
                }
            )
            date_ceased_being_adirector: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateCeasedBeingADirector",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            close_company: None | MtrYesNoType = field(
                default=None,
                metadata={
                    "name": "CloseCompany",
                    "type": "Element",
                },
            )
            close_company_name: None | str = field(
                default=None,
                metadata={
                    "name": "CloseCompanyName",
                    "type": "Element",
                    "min_length": 5,
                    "max_length": 160,
                    "pattern": r".*[^\s]+.*",
                },
            )
            company_registration_no: None | str = field(
                default=None,
                metadata={
                    "name": "CompanyRegistrationNo",
                    "type": "Element",
                    "min_length": 8,
                    "max_length": 8,
                    "pattern": r"([A-Z]{2}|[0-9]{2})[0-9]{6}",
                },
            )
            close_company_dividend: None | str = field(
                default=None,
                metadata={
                    "name": "CloseCompanyDividend",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            percentage_shareholding: None | int = field(
                default=None,
                metadata={
                    "name": "PercentageShareholding",
                    "type": "Element",
                    "min_inclusive": 0,
                    "max_inclusive": 100,
                },
            )
            off_payroll_working: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "OffPayrollWorking",
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class Benefits:
            company_cars_and_vans_benefit: None | str = field(
                default=None,
                metadata={
                    "name": "CompanyCarsAndVansBenefit",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            fuel_for_cars_and_vans: None | str = field(
                default=None,
                metadata={
                    "name": "FuelForCarsAndVans",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            private_medical_dental_insurance: None | str = field(
                default=None,
                metadata={
                    "name": "PrivateMedicalDentalInsurance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            vouchers_credit_cards_excess_mileage_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "VouchersCreditCardsExcessMileageAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            goods_etc_provided_by_employer: None | str = field(
                default=None,
                metadata={
                    "name": "GoodsEtcProvidedByEmployer",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            accommodation_provided_by_employer: None | str = field(
                default=None,
                metadata={
                    "name": "AccommodationProvidedByEmployer",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_benefits: None | str = field(
                default=None,
                metadata={
                    "name": "OtherBenefits",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            expenses_payments_received: None | str = field(
                default=None,
                metadata={
                    "name": "ExpensesPaymentsReceived",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class Expenses:
            business_travel_and_subsistence: None | str = field(
                default=None,
                metadata={
                    "name": "BusinessTravelAndSubsistence",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            fixed_expenses_deductions: None | str = field(
                default=None,
                metadata={
                    "name": "FixedExpensesDeductions",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            professional_fees_and_subscriptions: None | str = field(
                default=None,
                metadata={
                    "name": "ProfessionalFeesAndSubscriptions",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_expenses_and_capital_allowances: None | str = field(
                default=None,
                metadata={
                    "name": "OtherExpensesAndCapitalAllowances",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Sa102M:
        income: None | Mtr.Sa102M.Income = field(
            default=None,
            metadata={
                "name": "Income",
                "type": "Element",
            },
        )
        benefits_and_expense_payments_to_you: (
            None | Mtr.Sa102M.BenefitsAndExpensePaymentsToYou
        ) = field(
            default=None,
            metadata={
                "name": "BenefitsAndExpensePaymentsToYou",
                "type": "Element",
            },
        )
        income_benefits_and_expenses_received: None | str = field(
            default=None,
            metadata={
                "name": "IncomeBenefitsAndExpensesReceived",
                "type": "Element",
                "min_inclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        expenses_paid_by_you: None | Mtr.Sa102M.ExpensesPaidByYou = field(
            default=None,
            metadata={
                "name": "ExpensesPaidByYou",
                "type": "Element",
            },
        )
        service_benefit_cap: None | Mtr.Sa102M.ServiceBenefitCap = field(
            default=None,
            metadata={
                "name": "ServiceBenefitCap",
                "type": "Element",
            },
        )
        other_income: None | Mtr.Sa102M.OtherIncome = field(
            default=None,
            metadata={
                "name": "OtherIncome",
                "type": "Element",
            },
        )
        taxable_income: None | Mtr.Sa102M.TaxableIncome = field(
            default=None,
            metadata={
                "name": "TaxableIncome",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class Income:
            nature_of_post: None | str = field(
                default=None,
                metadata={
                    "name": "NatureOfPost",
                    "type": "Element",
                    "max_length": 28,
                    "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                },
            )
            salary_or_stipend: None | str = field(
                default=None,
                metadata={
                    "name": "SalaryOrStipend",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            payrolled_benefits: None | str = field(
                default=None,
                metadata={
                    "name": "PayrolledBenefits",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            tax_taken_off_salary_stipend: None | str = field(
                default=None,
                metadata={
                    "name": "TaxTakenOffSalaryStipend",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_class1_nicable_earnings: None | str = field(
                default=None,
                metadata={
                    "name": "TotalClass1NICableEarnings",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            fees_and_offerings: None | str = field(
                default=None,
                metadata={
                    "name": "FeesAndOfferings",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            vicarage_manse_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "VicarageManseExpenses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            personal_expenses_etc_paid: None | str = field(
                default=None,
                metadata={
                    "name": "PersonalExpensesEtcPaid",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            excess_mileage_allowance_etc: None | str = field(
                default=None,
                metadata={
                    "name": "ExcessMileageAllowanceEtc",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            round_sum_expenses_and_rent_allowances: None | str = field(
                default=None,
                metadata={
                    "name": "RoundSumExpensesAndRentAllowances",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            tax_taken_off_round_sum_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "TaxTakenOffRoundSumExpenses",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_income_from_post: None | str = field(
                default=None,
                metadata={
                    "name": "OtherIncomeFromPost",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            tax_taken_off_other_income: None | str = field(
                default=None,
                metadata={
                    "name": "TaxTakenOffOtherIncome",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_income_as_minister_of_religion: None | str = field(
                default=None,
                metadata={
                    "name": "TotalIncomeAsMinisterOfReligion",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class BenefitsAndExpensePaymentsToYou:
            vicarage_services_benefit: None | str = field(
                default=None,
                metadata={
                    "name": "VicarageServicesBenefit",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            car_provided: None | str = field(
                default=None,
                metadata={
                    "name": "CarProvided",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            fuel_for_car_provided: None | str = field(
                default=None,
                metadata={
                    "name": "FuelForCarProvided",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            interest_free_loans: None | str = field(
                default=None,
                metadata={
                    "name": "InterestFreeLoans",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            expenses_payments_made: None | str = field(
                default=None,
                metadata={
                    "name": "ExpensesPaymentsMade",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_benefits: None | str = field(
                default=None,
                metadata={
                    "name": "OtherBenefits",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_benefits_and_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "TotalBenefitsAndExpenses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class ExpensesPaidByYou:
            travelling_expenses_and_capital_allowances: None | str = field(
                default=None,
                metadata={
                    "name": "TravellingExpensesAndCapitalAllowances",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            maintenance_and_repairs_etc: None | str = field(
                default=None,
                metadata={
                    "name": "MaintenanceAndRepairsEtc",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            rent_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "RentExpenses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            secretarial_assistance: None | str = field(
                default=None,
                metadata={
                    "name": "SecretarialAssistance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "OtherExpenses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_expenses_paid: None | str = field(
                default=None,
                metadata={
                    "name": "TotalExpensesPaid",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class ServiceBenefitCap:
            gross_income: None | str = field(
                default=None,
                metadata={
                    "name": "GrossIncome",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            backpay_received_after_year_end: None | str = field(
                default=None,
                metadata={
                    "name": "BackpayReceivedAfterYearEnd",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            earlier_years_backpay_received_in_year: None | str = field(
                default=None,
                metadata={
                    "name": "EarlierYearsBackpayReceivedInYear",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            pension_scheme_payments: None | str = field(
                default=None,
                metadata={
                    "name": "PensionSchemePayments",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            net_income: None | str = field(
                default=None,
                metadata={
                    "name": "NetIncome",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            ten_percent_of_net_income: None | str = field(
                default=None,
                metadata={
                    "name": "TenPercentOfNetIncome",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            amount_paid_toward_service_benefit: None | str = field(
                default=None,
                metadata={
                    "name": "AmountPaidTowardServiceBenefit",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            payments_made_and_service_benefit_received: None | str = field(
                default=None,
                metadata={
                    "name": "PaymentsMadeAndServiceBenefitReceived",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            service_benefit_cap: None | str = field(
                default=None,
                metadata={
                    "name": "ServiceBenefitCap",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class OtherIncome:
            chaplaincy_and_other_income: None | str = field(
                default=None,
                metadata={
                    "name": "ChaplaincyAndOtherIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            tax_taken_of_other_income: None | str = field(
                default=None,
                metadata={
                    "name": "TaxTakenOfOtherIncome",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class TaxableIncome:
            taxable_income_minus_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "TaxableIncomeMinusExpenses",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_tax_taken_off: None | str = field(
                default=None,
                metadata={
                    "name": "TotalTaxTakenOff",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Sa103F:
        business_details: Mtr.Sa103F.BusinessDetails = field(
            metadata={
                "name": "BusinessDetails",
                "type": "Element",
                "required": True,
            }
        )
        other_information: None | Mtr.Sa103F.OtherInformation = field(
            default=None,
            metadata={
                "name": "OtherInformation",
                "type": "Element",
            },
        )
        business_income: None | Mtr.Sa103F.BusinessIncome = field(
            default=None,
            metadata={
                "name": "BusinessIncome",
                "type": "Element",
            },
        )
        business_expenses: None | Mtr.Sa103F.BusinessExpenses = field(
            default=None,
            metadata={
                "name": "BusinessExpenses",
                "type": "Element",
            },
        )
        net_profit_loss: None | str = field(
            default=None,
            metadata={
                "name": "NetProfitLoss",
                "type": "Element",
                "min_exclusive": "-10000000000.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        capital_allowances: None | Mtr.Sa103F.CapitalAllowances = field(
            default=None,
            metadata={
                "name": "CapitalAllowances",
                "type": "Element",
            },
        )
        taxable_profit_or_loss: None | Mtr.Sa103F.TaxableProfitOrLoss = field(
            default=None,
            metadata={
                "name": "TaxableProfitOrLoss",
                "type": "Element",
            },
        )
        losses: None | Mtr.Sa103F.Losses = field(
            default=None,
            metadata={
                "name": "Losses",
                "type": "Element",
            },
        )
        tax_taken_off: None | Mtr.Sa103F.TaxTakenOff = field(
            default=None,
            metadata={
                "name": "TaxTakenOff",
                "type": "Element",
            },
        )
        balance_sheet: None | Mtr.Sa103F.BalanceSheet = field(
            default=None,
            metadata={
                "name": "BalanceSheet",
                "type": "Element",
            },
        )
        nics: None | Mtr.Sa103F.Nics = field(
            default=None,
            metadata={
                "name": "NICs",
                "type": "Element",
            },
        )
        other_information_space: None | str = field(
            default=None,
            metadata={
                "name": "OtherInformationSpace",
                "type": "Element",
                "min_length": 1,
                "max_length": 20480,
                "pattern": r".*[^\s]+.*",
            },
        )

        @dataclass(kw_only=True)
        class BusinessDetails:
            business_name: str = field(
                metadata={
                    "name": "BusinessName",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 28,
                    "pattern": r".*[^\s]+.*",
                }
            )
            business_description: str = field(
                metadata={
                    "name": "BusinessDescription",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 42,
                    "pattern": r".*[^\s]+.*",
                }
            )
            business_address_first_line: None | str = field(
                default=None,
                metadata={
                    "name": "BusinessAddressFirstLine",
                    "type": "Element",
                    "max_length": 28,
                    "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                },
            )
            business_address_postcode: None | str = field(
                default=None,
                metadata={
                    "name": "BusinessAddressPostcode",
                    "type": "Element",
                    "max_length": 8,
                    "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                },
            )
            change_of_business_details: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ChangeOfBusinessDetails",
                    "type": "Element",
                },
            )
            did_your_business_start: MtrYesNoType = field(
                metadata={
                    "name": "DidYourBusinessStart",
                    "type": "Element",
                    "required": True,
                }
            )
            date_business_started: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateBusinessStarted",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            did_your_business_cease: MtrYesNoType = field(
                metadata={
                    "name": "DidYourBusinessCease",
                    "type": "Element",
                    "required": True,
                }
            )
            date_business_ceased: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateBusinessCeased",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            date_accounting_period_starts: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateAccountingPeriodStarts",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            date_accounting_period_ends: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateAccountingPeriodEnds",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            election_to_opt_out_of_cash_basis: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ElectionToOptOutOfCashBasis",
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class OtherInformation:
            special_arrangements_apply: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "SpecialArrangementsApply",
                    "type": "Element",
                },
            )
            information_provided_last_year: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "InformationProvidedLastYear",
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class BusinessIncome:
            turnover: None | str = field(
                default=None,
                metadata={
                    "name": "Turnover",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_business_income: None | str = field(
                default=None,
                metadata={
                    "name": "OtherBusinessIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            trading_income_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "TradingIncomeAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "max_inclusive": "1000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class BusinessExpenses:
            total_expenses: None | Mtr.Sa103F.BusinessExpenses.TotalExpenses = field(
                default=None,
                metadata={
                    "name": "TotalExpenses",
                    "type": "Element",
                },
            )
            disallowable_expenses: (
                None | Mtr.Sa103F.BusinessExpenses.DisallowableExpenses
            ) = field(
                default=None,
                metadata={
                    "name": "DisallowableExpenses",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class TotalExpenses:
                cost_of_goods: None | str = field(
                    default=None,
                    metadata={
                        "name": "CostOfGoods",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                subcontractor_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "SubcontractorCosts",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                wages_salaries_and_staff_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "WagesSalariesAndStaffCosts",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                car_van_and_travel_expenses: None | str = field(
                    default=None,
                    metadata={
                        "name": "CarVanAndTravelExpenses",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                rent_and_other_property_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "RentAndOtherPropertyCosts",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                repairs_and_maintenance_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "RepairsAndMaintenanceCosts",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                phone_and_other_office_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "PhoneAndOtherOfficeCosts",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                advertising_and_entertainment_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "AdvertisingAndEntertainmentCosts",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                bank_and_loan_interest: None | str = field(
                    default=None,
                    metadata={
                        "name": "BankAndLoanInterest",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                other_finance_charges: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherFinanceCharges",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                debts_written_off: None | str = field(
                    default=None,
                    metadata={
                        "name": "DebtsWrittenOff",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                accountancy_and_legal_fees: None | str = field(
                    default=None,
                    metadata={
                        "name": "AccountancyAndLegalFees",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                depreciation_and_loss_profit_on_sale: None | str = field(
                    default=None,
                    metadata={
                        "name": "DepreciationAndLossProfitOnSale",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                other_business_expenses: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherBusinessExpenses",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                total_expenses: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalExpenses",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class DisallowableExpenses:
                disallowable_cost_of_goods: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableCostOfGoods",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                disallowable_subcontractor_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableSubcontractorCosts",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                disallowable_staff_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableStaffCosts",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                disallowable_car_and_travel_expenses: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableCarAndTravelExpenses",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                disallowable_rent_and_other_property_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableRentAndOtherPropertyCosts",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                disallowable_repairs_and_maintenance_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableRepairsAndMaintenanceCosts",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                disallowable_phone_and_other_office_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowablePhoneAndOtherOfficeCosts",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                disallowable_advertising_and_entertainment_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableAdvertisingAndEntertainmentCosts",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                disallowable_bank_and_loan_interest: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableBankAndLoanInterest",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                disallowable_other_finance_charges: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableOtherFinanceCharges",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                disallowable_debts_written_off: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableDebtsWrittenOff",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                disallowable_accountancy_and_legal_fees: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableAccountancyAndLegalFees",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                disallowable_depreciation_and_loss_profit_on_sale: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableDepreciationAndLossProfitOnSale",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                disallowable_other_business_expenses: None | str = field(
                    default=None,
                    metadata={
                        "name": "DisallowableOtherBusinessExpenses",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                total_disallowable_expenses: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalDisallowableExpenses",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class CapitalAllowances:
            annual_investment_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "AnnualInvestmentAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            annual_allowances_at_higher_rate: None | str = field(
                default=None,
                metadata={
                    "name": "AnnualAllowancesAtHigherRate",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            annual_allowances_at_lower_rate: None | str = field(
                default=None,
                metadata={
                    "name": "AnnualAllowancesAtLowerRate",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            zero_emission_goods_vehicle_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "ZeroEmissionGoodsVehicleAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            zero_emission_car_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "ZeroEmissionCarAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            the_structures_and_buildings_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "TheStructuresAndBuildingsAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            freeport_and_investment_zones_structures_and_buildings_allowance: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "FreeportAndInvestmentZonesStructuresAndBuildingsAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            electric_charge_point_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "ElectricChargePointAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_capital_allowances: None | str = field(
                default=None,
                metadata={
                    "name": "OtherCapitalAllowances",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            balancing_allowances_on_sale_or_cessation: None | str = field(
                default=None,
                metadata={
                    "name": "BalancingAllowancesOnSaleOrCessation",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_capital_allowances: None | str = field(
                default=None,
                metadata={
                    "name": "TotalCapitalAllowances",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_balancing_charges: None | str = field(
                default=None,
                metadata={
                    "name": "TotalBalancingCharges",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class TaxableProfitOrLoss:
            own_goods_and_services: None | str = field(
                default=None,
                metadata={
                    "name": "OwnGoodsAndServices",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            additions_to_net_profit_deductions_from_net_loss: None | str = field(
                default=None,
                metadata={
                    "name": "AdditionsToNetProfitDeductionsFromNetLoss",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            non_taxable_business_income: None | str = field(
                default=None,
                metadata={
                    "name": "NonTaxableBusinessIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            deductions_from_net_profit_additions_to_net_loss: None | str = field(
                default=None,
                metadata={
                    "name": "DeductionsFromNetProfitAdditionsToNetLoss",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            net_business_profit_loss_for_tax: None | str = field(
                default=None,
                metadata={
                    "name": "NetBusinessProfitLossForTax",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            tax_year_adjustment: None | str = field(
                default=None,
                metadata={
                    "name": "TaxYearAdjustment",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                },
            )
            change_of_accounting_practice_adjustment: None | str = field(
                default=None,
                metadata={
                    "name": "ChangeOfAccountingPracticeAdjustment",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            averaging_adjustment: None | str = field(
                default=None,
                metadata={
                    "name": "AveragingAdjustment",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                },
            )
            adjusted_profit_for_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustedProfitForTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            spread_transition_profit_treated_as_arising: None | str = field(
                default=None,
                metadata={
                    "name": "SpreadTransitionProfitTreatedAsArising",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_brought_forward_used_against_spread_transition_profit: None | str = (
                field(
                    default=None,
                    metadata={
                        "name": "LossBroughtForwardUsedAgainstSpreadTransitionProfit",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
            )
            loss_brought_forward: None | str = field(
                default=None,
                metadata={
                    "name": "LossBroughtForward",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            any_other_business_income: None | str = field(
                default=None,
                metadata={
                    "name": "AnyOtherBusinessIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_taxable_business_profits: None | str = field(
                default=None,
                metadata={
                    "name": "TotalTaxableBusinessProfits",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_taxable_business_profits_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "TotalTaxableBusinessProfitsFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class Losses:
            adjusted_loss_for_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustedLossForTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            adjusted_loss_for_the_year_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustedLossForTheYearFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_of_year_set_against_other_income: None | str = field(
                default=None,
                metadata={
                    "name": "LossOfYearSetAgainstOtherIncome",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_to_carry_back: None | str = field(
                default=None,
                metadata={
                    "name": "LossToCarryBack",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_loss_to_carry_forward: None | str = field(
                default=None,
                metadata={
                    "name": "TotalLossToCarryForward",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class TaxTakenOff:
            sub_contractors_tax_deduction: None | str = field(
                default=None,
                metadata={
                    "name": "SubContractorsTaxDeduction",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_tax_taken_off_trading_income: None | str = field(
                default=None,
                metadata={
                    "name": "OtherTaxTakenOffTradingIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class BalanceSheet:
            assets: None | Mtr.Sa103F.BalanceSheet.Assets = field(
                default=None,
                metadata={
                    "name": "Assets",
                    "type": "Element",
                },
            )
            liabilities: None | Mtr.Sa103F.BalanceSheet.Liabilities = field(
                default=None,
                metadata={
                    "name": "Liabilities",
                    "type": "Element",
                },
            )
            net_business_assets: None | str = field(
                default=None,
                metadata={
                    "name": "NetBusinessAssets",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            capital_account: None | Mtr.Sa103F.BalanceSheet.CapitalAccount = field(
                default=None,
                metadata={
                    "name": "CapitalAccount",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Assets:
                equipment_machinery_vehicles: None | str = field(
                    default=None,
                    metadata={
                        "name": "EquipmentMachineryVehicles",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                other_fixed_assets: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherFixedAssets",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                stock_and_work_in_progress: None | str = field(
                    default=None,
                    metadata={
                        "name": "StockAndWorkInProgress",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                trade_debtors: None | str = field(
                    default=None,
                    metadata={
                        "name": "TradeDebtors",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                bank_etc_balances: None | str = field(
                    default=None,
                    metadata={
                        "name": "BankEtcBalances",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                cash_in_hand: None | str = field(
                    default=None,
                    metadata={
                        "name": "CashInHand",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                other_current_assets: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherCurrentAssets",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                total_business_assets: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalBusinessAssets",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class Liabilities:
                trade_creditors: None | str = field(
                    default=None,
                    metadata={
                        "name": "TradeCreditors",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                loans_and_overdrafts: None | str = field(
                    default=None,
                    metadata={
                        "name": "LoansAndOverdrafts",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                other_liabilities: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherLiabilities",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class CapitalAccount:
                capital_account_balance_at_start: None | str = field(
                    default=None,
                    metadata={
                        "name": "CapitalAccountBalanceAtStart",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )
                net_profit_or_loss: None | str = field(
                    default=None,
                    metadata={
                        "name": "NetProfitOrLoss",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                capital_introduced: None | str = field(
                    default=None,
                    metadata={
                        "name": "CapitalIntroduced",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                drawings: None | str = field(
                    default=None,
                    metadata={
                        "name": "Drawings",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                capital_account_balance_at_end: None | str = field(
                    default=None,
                    metadata={
                        "name": "CapitalAccountBalanceAtEnd",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class Nics:
            pay_class2_nicvoluntarily: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "PayClass2NICvoluntarily",
                    "type": "Element",
                },
            )
            class2_nicamount: None | str = field(
                default=None,
                metadata={
                    "name": "Class2NICamount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            class4_nicexempt: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "Class4NICexempt",
                    "type": "Element",
                },
            )
            adjustment_to_class4_nicprofits: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustmentToClass4NICProfits",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Sa103S:
        business_details: Mtr.Sa103S.BusinessDetails = field(
            metadata={
                "name": "BusinessDetails",
                "type": "Element",
                "required": True,
            }
        )
        business_income: None | Mtr.Sa103S.BusinessIncome = field(
            default=None,
            metadata={
                "name": "BusinessIncome",
                "type": "Element",
            },
        )
        allowable_business_expenses: None | Mtr.Sa103S.AllowableBusinessExpenses = (
            field(
                default=None,
                metadata={
                    "name": "AllowableBusinessExpenses",
                    "type": "Element",
                },
            )
        )
        net_profit_or_loss: None | str = field(
            default=None,
            metadata={
                "name": "NetProfitOrLoss",
                "type": "Element",
                "min_exclusive": "-10000000000.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        capital_allowances: None | Mtr.Sa103S.CapitalAllowances = field(
            default=None,
            metadata={
                "name": "CapitalAllowances",
                "type": "Element",
            },
        )
        taxable_profits: None | Mtr.Sa103S.TaxableProfits = field(
            default=None,
            metadata={
                "name": "TaxableProfits",
                "type": "Element",
            },
        )
        profits_losses_nics_and_cis: None | Mtr.Sa103S.ProfitsLossesNicsAndCis = field(
            default=None,
            metadata={
                "name": "ProfitsLossesNICsAndCIS",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class BusinessDetails:
            business_description: str = field(
                metadata={
                    "name": "BusinessDescription",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 42,
                    "pattern": r".*[^\s]+.*",
                }
            )
            business_address_postcode: None | str = field(
                default=None,
                metadata={
                    "name": "BusinessAddressPostcode",
                    "type": "Element",
                    "max_length": 8,
                    "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./@£]*",
                },
            )
            change_of_business_details: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ChangeOfBusinessDetails",
                    "type": "Element",
                },
            )
            foster_etc_carer_indicator: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "FosterEtcCarerIndicator",
                    "type": "Element",
                },
            )
            did_your_business_start: MtrYesNoType = field(
                metadata={
                    "name": "DidYourBusinessStart",
                    "type": "Element",
                    "required": True,
                }
            )
            date_business_started: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateBusinessStarted",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            did_your_business_cease: MtrYesNoType = field(
                metadata={
                    "name": "DidYourBusinessCease",
                    "type": "Element",
                    "required": True,
                }
            )
            date_business_ceased: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateBusinessCeased",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            date_business_books_are_made_up_to: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateBusinessBooksAreMadeUpTo",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            election_to_opt_out_of_cash_basis: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ElectionToOptOutOfCashBasis",
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class BusinessIncome:
            turnover: None | str = field(
                default=None,
                metadata={
                    "name": "Turnover",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_business_income: None | str = field(
                default=None,
                metadata={
                    "name": "OtherBusinessIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            trading_income_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "TradingIncomeAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "max_inclusive": "1000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class AllowableBusinessExpenses:
            cost_of_goods: None | str = field(
                default=None,
                metadata={
                    "name": "CostOfGoods",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                },
            )
            car_van_and_travel_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "CarVanAndTravelExpenses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            wages_salaries_and_staff_costs: None | str = field(
                default=None,
                metadata={
                    "name": "WagesSalariesAndStaffCosts",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            rent_and_other_property_costs: None | str = field(
                default=None,
                metadata={
                    "name": "RentAndOtherPropertyCosts",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                },
            )
            repairs_and_maintenance_costs: None | str = field(
                default=None,
                metadata={
                    "name": "RepairsAndMaintenanceCosts",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                },
            )
            accountancy_and_legal_fees: None | str = field(
                default=None,
                metadata={
                    "name": "AccountancyAndLegalFees",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                },
            )
            interest_and_finance_charges: None | str = field(
                default=None,
                metadata={
                    "name": "InterestAndFinanceCharges",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                },
            )
            phone_and_other_office_costs: None | str = field(
                default=None,
                metadata={
                    "name": "PhoneAndOtherOfficeCosts",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_allowable_business_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "OtherAllowableBusinessExpenses",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                },
            )
            total_allowable_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "TotalAllowableExpenses",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class CapitalAllowances:
            annual_investment_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "AnnualInvestmentAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            allowance_for_small_balance_of_unrelieved_expenditure: None | str = field(
                default=None,
                metadata={
                    "name": "AllowanceForSmallBalanceOfUnrelievedExpenditure",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            zero_emission_car_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "ZeroEmissionCarAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_capital_allowances: None | str = field(
                default=None,
                metadata={
                    "name": "OtherCapitalAllowances",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            the_structures_and_buildings_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "TheStructuresAndBuildingsAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            freeport_and_investment_zones_structures_and_buildings_allowance: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "FreeportAndInvestmentZonesStructuresAndBuildingsAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_balancing_charges: None | str = field(
                default=None,
                metadata={
                    "name": "TotalBalancingCharges",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class TaxableProfits:
            own_goods_and_services: None | str = field(
                default=None,
                metadata={
                    "name": "OwnGoodsAndServices",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            net_business_profit_for_tax: None | str = field(
                default=None,
                metadata={
                    "name": "NetBusinessProfitForTax",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_brought_forward: None | str = field(
                default=None,
                metadata={
                    "name": "LossBroughtForward",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            any_other_business_income: None | str = field(
                default=None,
                metadata={
                    "name": "AnyOtherBusinessIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class ProfitsLossesNicsAndCis:
            total_taxable_business_profits: None | str = field(
                default=None,
                metadata={
                    "name": "TotalTaxableBusinessProfits",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            net_business_loss_for_tax: None | str = field(
                default=None,
                metadata={
                    "name": "NetBusinessLossForTax",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_of_year_set_against_other_income: None | str = field(
                default=None,
                metadata={
                    "name": "LossOfYearSetAgainstOtherIncome",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_to_carry_back: None | str = field(
                default=None,
                metadata={
                    "name": "LossToCarryBack",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_loss_to_carry_forward: None | str = field(
                default=None,
                metadata={
                    "name": "TotalLossToCarryForward",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            pay_class2_nicvoluntarily: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "PayClass2NICvoluntarily",
                    "type": "Element",
                },
            )
            class2_nicamount: None | str = field(
                default=None,
                metadata={
                    "name": "Class2NICamount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            class4_nicexempt: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "Class4NICexempt",
                    "type": "Element",
                },
            )
            sub_contractors_tax_deduction: None | str = field(
                default=None,
                metadata={
                    "name": "SubContractorsTaxDeduction",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Sa103L:
        ukincome: None | Mtr.Sa103L.Ukincome = field(
            default=None,
            metadata={
                "name": "UKIncome",
                "type": "Element",
            },
        )
        foreign_income: None | Mtr.Sa103L.ForeignIncome = field(
            default=None,
            metadata={
                "name": "ForeignIncome",
                "type": "Element",
            },
        )
        other_receipts: None | Mtr.Sa103L.OtherReceipts = field(
            default=None,
            metadata={
                "name": "OtherReceipts",
                "type": "Element",
            },
        )
        total_lloyds_income: None | str = field(
            default=None,
            metadata={
                "name": "TotalLloydsIncome",
                "type": "Element",
                "min_exclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        repayment_of_foreign_tax_tax_credit_relief: None | str = field(
            default=None,
            metadata={
                "name": "RepaymentOfForeignTaxTaxCreditRelief",
                "type": "Element",
                "min_exclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        losses_and_expenses: None | Mtr.Sa103L.LossesAndExpenses = field(
            default=None,
            metadata={
                "name": "LossesAndExpenses",
                "type": "Element",
            },
        )
        profit_amount: None | str = field(
            default=None,
            metadata={
                "name": "ProfitAmount",
                "type": "Element",
                "min_inclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        loss_amount: None | str = field(
            default=None,
            metadata={
                "name": "LossAmount",
                "type": "Element",
                "min_inclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        foreign_tax: None | Mtr.Sa103L.ForeignTax = field(
            default=None,
            metadata={
                "name": "ForeignTax",
                "type": "Element",
            },
        )
        taxable_profits: None | Mtr.Sa103L.TaxableProfits = field(
            default=None,
            metadata={
                "name": "TaxableProfits",
                "type": "Element",
            },
        )
        allowable_losses: None | Mtr.Sa103L.AllowableLosses = field(
            default=None,
            metadata={
                "name": "AllowableLosses",
                "type": "Element",
            },
        )
        losses_reconciliation: None | Mtr.Sa103L.LossesReconciliation = field(
            default=None,
            metadata={
                "name": "LossesReconciliation",
                "type": "Element",
            },
        )
        nics: None | Mtr.Sa103L.Nics = field(
            default=None,
            metadata={
                "name": "NICs",
                "type": "Element",
            },
        )
        any_other_information_space: None | str = field(
            default=None,
            metadata={
                "name": "AnyOtherInformationSpace",
                "type": "Element",
                "min_length": 1,
                "max_length": 20480,
                "pattern": r".*[^\s]+.*",
            },
        )

        @dataclass(kw_only=True)
        class Ukincome:
            ukinterest: None | Mtr.Sa103L.Ukincome.Ukinterest = field(
                default=None,
                metadata={
                    "name": "UKInterest",
                    "type": "Element",
                },
            )
            ukdividends: None | Mtr.Sa103L.Ukincome.Ukdividends = field(
                default=None,
                metadata={
                    "name": "UKDividends",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Ukinterest:
                bank_etc_and_gilt_untaxed_interest: None | str = field(
                    default=None,
                    metadata={
                        "name": "BankEtcAndGiltUntaxedInterest",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                accrued_income_scheme_aggregate_amount: None | str = field(
                    default=None,
                    metadata={
                        "name": "AccruedIncomeSchemeAggregateAmount",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                taxed_unit_trust_etc_interest: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxedUnitTrustEtcInterest",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                tax_taken_off: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxTakenOff",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                total_ukinterest_and_tax_taken_off: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalUKInterestAndTaxTakenOff",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class Ukdividends:
                stock_dividends_amount_received: None | str = field(
                    default=None,
                    metadata={
                        "name": "StockDividendsAmountReceived",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                bonus_issues_of_securities_and_redeemable_shares: None | str = field(
                    default=None,
                    metadata={
                        "name": "BonusIssuesOfSecuritiesAndRedeemableShares",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                other_distributions_amount_received: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherDistributionsAmountReceived",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                total_ukdividends_and_distributions: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalUKDividendsAndDistributions",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class ForeignIncome:
            interest: None | Mtr.Sa103L.ForeignIncome.Interest = field(
                default=None,
                metadata={
                    "name": "Interest",
                    "type": "Element",
                },
            )
            dividends: None | Mtr.Sa103L.ForeignIncome.Dividends = field(
                default=None,
                metadata={
                    "name": "Dividends",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Interest:
                foreign_interest_etc_amount: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignInterestEtcAmount",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax_deducted: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTaxDeducted",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                uktax_deducted: None | str = field(
                    default=None,
                    metadata={
                        "name": "UKTaxDeducted",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class Dividends:
                non_ukdividends_amount: None | str = field(
                    default=None,
                    metadata={
                        "name": "NonUKDividendsAmount",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax_deducted: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTaxDeducted",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                uktax_deducted: None | str = field(
                    default=None,
                    metadata={
                        "name": "UKTaxDeducted",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                total_non_ukincome: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalNonUKIncome",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class OtherReceipts:
            aggregate_syndicate_profits: None | str = field(
                default=None,
                metadata={
                    "name": "AggregateSyndicateProfits",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            special_reserve_fund_net_withdrawal_release: None | str = field(
                default=None,
                metadata={
                    "name": "SpecialReserveFundNetWithdrawalRelease",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            stop_loss_recoveries: None | str = field(
                default=None,
                metadata={
                    "name": "StopLossRecoveries",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            compensation_receipts: None | str = field(
                default=None,
                metadata={
                    "name": "CompensationReceipts",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            repayment_of_foreign_tax_deduction: None | str = field(
                default=None,
                metadata={
                    "name": "RepaymentOfForeignTaxDeduction",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_nonsyndicate_income: None | str = field(
                default=None,
                metadata={
                    "name": "OtherNonsyndicateIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_other_lloyds_receipts: None | str = field(
                default=None,
                metadata={
                    "name": "TotalOtherLloydsReceipts",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class LossesAndExpenses:
            aggregate_syndicate_losses: None | str = field(
                default=None,
                metadata={
                    "name": "AggregateSyndicateLosses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            special_reserve_fund_net_transfer: None | str = field(
                default=None,
                metadata={
                    "name": "SpecialReserveFundNetTransfer",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            stop_loss_premiums_paid: None | str = field(
                default=None,
                metadata={
                    "name": "StopLossPremiumsPaid",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            personal_quota_share_and_exeat_premiums: None | str = field(
                default=None,
                metadata={
                    "name": "PersonalQuotaShareAndExeatPremiums",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            estate_protection_plan_premiums: None | str = field(
                default=None,
                metadata={
                    "name": "EstateProtectionPlanPremiums",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            underwriting_loan_interest: None | str = field(
                default=None,
                metadata={
                    "name": "UnderwritingLoanInterest",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            lloyds_members_association_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "LloydsMembersAssociationExpenses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            members_agent_profit_commission_and_salaries: None | str = field(
                default=None,
                metadata={
                    "name": "MembersAgentProfitCommissionAndSalaries",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            bank_guaranteeletters_of_credit_fees: None | str = field(
                default=None,
                metadata={
                    "name": "BankGuaranteelettersOfCreditFees",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            accountancy_fees: None | str = field(
                default=None,
                metadata={
                    "name": "AccountancyFees",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_lloyds_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "OtherLloydsExpenses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_losses_and_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "TotalLossesAndExpenses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class ForeignTax:
            foreign_tax_on_personal_fund_income: None | str = field(
                default=None,
                metadata={
                    "name": "ForeignTaxOnPersonalFundIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            usincome_tax_paid: None | str = field(
                default=None,
                metadata={
                    "name": "USIncomeTaxPaid",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            canadian_tax_paid: None | str = field(
                default=None,
                metadata={
                    "name": "CanadianTaxPaid",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            syndicate_foreign_tax: None | str = field(
                default=None,
                metadata={
                    "name": "SyndicateForeignTax",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            additional_payments_of_foreign_tax: None | str = field(
                default=None,
                metadata={
                    "name": "AdditionalPaymentsOfForeignTax",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_foreign_tax: None | str = field(
                default=None,
                metadata={
                    "name": "TotalForeignTax",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class TaxableProfits:
            profit_amount: None | str = field(
                default=None,
                metadata={
                    "name": "ProfitAmount",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            foreign_tax_claimed_as_deduction: None | str = field(
                default=None,
                metadata={
                    "name": "ForeignTaxClaimedAsDeduction",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            unused_losses_brought_forward: None | str = field(
                default=None,
                metadata={
                    "name": "UnusedLossesBroughtForward",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_taxable_profits: None | str = field(
                default=None,
                metadata={
                    "name": "TotalTaxableProfits",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class AllowableLosses:
            loss_amount: None | str = field(
                default=None,
                metadata={
                    "name": "LossAmount",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            foreign_tax_claimed_as_deduction: None | str = field(
                default=None,
                metadata={
                    "name": "ForeignTaxClaimedAsDeduction",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_for_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "LossForTheYear",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_offset_against_other_income: None | str = field(
                default=None,
                metadata={
                    "name": "LossOffsetAgainstOtherIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_carried_back: None | str = field(
                default=None,
                metadata={
                    "name": "LossCarriedBack",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            unused_losses_to_carry_forward: None | str = field(
                default=None,
                metadata={
                    "name": "UnusedLossesToCarryForward",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class LossesReconciliation:
            losses_brought_forward: None | str = field(
                default=None,
                metadata={
                    "name": "LossesBroughtForward",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            losses_used_against_profits_of_year: None | str = field(
                default=None,
                metadata={
                    "name": "LossesUsedAgainstProfitsOfYear",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                },
            )
            unused_loss_from_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "UnusedLossFromTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_loss_to_carry_forward: None | str = field(
                default=None,
                metadata={
                    "name": "TotalLossToCarryForward",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class Nics:
            pay_class2_nicvoluntarily: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "PayClass2NICvoluntarily",
                    "type": "Element",
                },
            )
            class2_nicamount: None | str = field(
                default=None,
                metadata={
                    "name": "Class2NICamount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            class4_nicexempt: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "Class4NICexempt",
                    "type": "Element",
                },
            )
            adjustment_to_class4_nicprofits: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustmentToClass4NICProfits",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Sa104F:
        partnership_details: Mtr.Sa104F.PartnershipDetails = field(
            metadata={
                "name": "PartnershipDetails",
                "type": "Element",
                "required": True,
            }
        )
        share_of_profits: None | Mtr.Sa104F.ShareOfProfits = field(
            default=None,
            metadata={
                "name": "ShareOfProfits",
                "type": "Element",
            },
        )
        share_of_losses: None | Mtr.Sa104F.ShareOfLosses = field(
            default=None,
            metadata={
                "name": "ShareOfLosses",
                "type": "Element",
            },
        )
        nics: None | Mtr.Sa104F.Nics = field(
            default=None,
            metadata={
                "name": "NICs",
                "type": "Element",
            },
        )
        share_of_untaxed_income: None | Mtr.Sa104F.ShareOfUntaxedIncome = field(
            default=None,
            metadata={
                "name": "ShareOfUntaxedIncome",
                "type": "Element",
            },
        )
        share_of_partnership_income: None | Mtr.Sa104F.ShareOfPartnershipIncome = field(
            default=None,
            metadata={
                "name": "ShareOfPartnershipIncome",
                "type": "Element",
            },
        )
        share_of_partnership_tax_payed: None | Mtr.Sa104F.ShareOfPartnershipTaxPayed = (
            field(
                default=None,
                metadata={
                    "name": "ShareOfPartnershipTaxPayed",
                    "type": "Element",
                },
            )
        )

        @dataclass(kw_only=True)
        class PartnershipDetails:
            partnership_reference_number: str = field(
                metadata={
                    "name": "PartnershipReferenceNumber",
                    "type": "Element",
                    "required": True,
                    "length": 10,
                    "pattern": r"[0-9]{10}",
                }
            )
            partnership_description: str = field(
                metadata={
                    "name": "PartnershipDescription",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 28,
                    "pattern": r".*[^\s]+.*",
                }
            )
            did_you_join_the_partnership: MtrYesNoType = field(
                metadata={
                    "name": "DidYouJoinThePartnership",
                    "type": "Element",
                    "required": True,
                }
            )
            date_joined_partnership: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateJoinedPartnership",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            did_you_leave_the_partnership: MtrYesNoType = field(
                metadata={
                    "name": "DidYouLeaveThePartnership",
                    "type": "Element",
                    "required": True,
                }
            )
            date_left_partnership: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateLeftPartnership",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )

        @dataclass(kw_only=True)
        class ShareOfProfits:
            share_of_partnership_profit_or_loss: None | str = field(
                default=None,
                metadata={
                    "name": "ShareOfPartnershipProfitOrLoss",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            tax_year_adjustment: None | str = field(
                default=None,
                metadata={
                    "name": "TaxYearAdjustment",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            change_of_accounting_practice_adjustment: None | str = field(
                default=None,
                metadata={
                    "name": "ChangeOfAccountingPracticeAdjustment",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                },
            )
            averaging_adjustment: None | str = field(
                default=None,
                metadata={
                    "name": "AveragingAdjustment",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            foreign_tax_claimed_as_deduction: None | str = field(
                default=None,
                metadata={
                    "name": "ForeignTaxClaimedAsDeduction",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            adjusted_profit_for_year: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustedProfitForYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            spread_transition_profit_treated_as_arising: None | str = field(
                default=None,
                metadata={
                    "name": "SpreadTransitionProfitTreatedAsArising",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_brought_forward_used_against_spread_transition_profit: None | str = (
                field(
                    default=None,
                    metadata={
                        "name": "LossBroughtForwardUsedAgainstSpreadTransitionProfit",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
            )
            losses_brought_forward: None | str = field(
                default=None,
                metadata={
                    "name": "LossesBroughtForward",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            taxable_profits_after_losses: None | str = field(
                default=None,
                metadata={
                    "name": "TaxableProfitsAfterLosses",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_business_income: None | str = field(
                default=None,
                metadata={
                    "name": "OtherBusinessIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_taxable_business_profits: None | str = field(
                default=None,
                metadata={
                    "name": "TotalTaxableBusinessProfits",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_taxable_business_profits_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "TotalTaxableBusinessProfitsFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class ShareOfLosses:
            adjusted_loss_for_year: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustedLossForYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            adjusted_loss_for_year_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustedLossForYearFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_set_off_against_other_income: None | str = field(
                default=None,
                metadata={
                    "name": "LossSetOffAgainstOtherIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_to_be_carried_back: None | str = field(
                default=None,
                metadata={
                    "name": "LossToBeCarriedBack",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_loss_to_carry_forward: None | str = field(
                default=None,
                metadata={
                    "name": "TotalLossToCarryForward",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class Nics:
            pay_class2_nicvoluntarily: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "PayClass2NICvoluntarily",
                    "type": "Element",
                },
            )
            class2_nicamount: None | str = field(
                default=None,
                metadata={
                    "name": "Class2NICamount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            class4_nicexempt: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "Class4NICexempt",
                    "type": "Element",
                },
            )
            adjustment_to_class4_nicprofits: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustmentToClass4NICProfits",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class ShareOfUntaxedIncome:
            savings_income: None | Mtr.Sa104F.ShareOfUntaxedIncome.SavingsIncome = (
                field(
                    default=None,
                    metadata={
                        "name": "SavingsIncome",
                        "type": "Element",
                    },
                )
            )
            ukproperty_income: (
                None | Mtr.Sa104F.ShareOfUntaxedIncome.UkpropertyIncome
            ) = field(
                default=None,
                metadata={
                    "name": "UKPropertyIncome",
                    "type": "Element",
                },
            )
            other_untaxed_ukincome: (
                None | Mtr.Sa104F.ShareOfUntaxedIncome.OtherUntaxedUkincome
            ) = field(
                default=None,
                metadata={
                    "name": "OtherUntaxedUKIncome",
                    "type": "Element",
                },
            )
            offshore_funds_income: (
                None | Mtr.Sa104F.ShareOfUntaxedIncome.OffshoreFundsIncome
            ) = field(
                default=None,
                metadata={
                    "name": "OffshoreFundsIncome",
                    "type": "Element",
                },
            )
            other_untaxed_foreign_income: (
                None | Mtr.Sa104F.ShareOfUntaxedIncome.OtherUntaxedForeignIncome
            ) = field(
                default=None,
                metadata={
                    "name": "OtherUntaxedForeignIncome",
                    "type": "Element",
                },
            )
            total_untaxed_income_share: None | str = field(
                default=None,
                metadata={
                    "name": "TotalUntaxedIncomeShare",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

            @dataclass(kw_only=True)
            class SavingsIncome:
                ukuntaxed_savings_income_share: None | str = field(
                    default=None,
                    metadata={
                        "name": "UKUntaxedSavingsIncomeShare",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                ukuntaxed_savings_adjustment: None | str = field(
                    default=None,
                    metadata={
                        "name": "UKUntaxedSavingsAdjustment",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                adjusted_uksavings_income: None | str = field(
                    default=None,
                    metadata={
                        "name": "AdjustedUKSavingsIncome",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_income: (
                    None | Mtr.Sa104F.ShareOfUntaxedIncome.SavingsIncome.ForeignIncome
                ) = field(
                    default=None,
                    metadata={
                        "name": "ForeignIncome",
                        "type": "Element",
                    },
                )
                total_untaxed_savings_income: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalUntaxedSavingsIncome",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                total_untaxed_savings_income_figclaim: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalUntaxedSavingsIncomeFIGclaim",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

                @dataclass(kw_only=True)
                class ForeignIncome:
                    foreign_untaxed_savings_income_share: None | str = field(
                        default=None,
                        metadata={
                            "name": "ForeignUntaxedSavingsIncomeShare",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    foreign_untaxed_savings_adjustment: None | str = field(
                        default=None,
                        metadata={
                            "name": "ForeignUntaxedSavingsAdjustment",
                            "type": "Element",
                            "min_exclusive": "-10000000000.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    total_foreign_tax_taken_off: None | str = field(
                        default=None,
                        metadata={
                            "name": "TotalForeignTaxTakenOff",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    adjusted_foreign_savings_income: None | str = field(
                        default=None,
                        metadata={
                            "name": "AdjustedForeignSavingsIncome",
                            "type": "Element",
                            "min_exclusive": "-10000000000.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )

            @dataclass(kw_only=True)
            class UkpropertyIncome:
                ukproperty_profit_loss_share: None | str = field(
                    default=None,
                    metadata={
                        "name": "UKPropertyProfitLossShare",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                ukproperty_income_adjustment: None | str = field(
                    default=None,
                    metadata={
                        "name": "UKPropertyIncomeAdjustment",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                loss_brought_forward: None | str = field(
                    default=None,
                    metadata={
                        "name": "LossBroughtForward",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                loss_for_year_set_off_against_other_income: None | str = field(
                    default=None,
                    metadata={
                        "name": "LossForYearSetOffAgainstOtherIncome",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                loss_to_be_carried_forward: None | str = field(
                    default=None,
                    metadata={
                        "name": "LossToBeCarriedForward",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                taxable_profits_after_adjustment_and_losses: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableProfitsAfterAdjustmentAndLosses",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                residential_finance_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "ResidentialFinanceCosts",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                unused_residential_finance_costs_brought_forward: None | str = field(
                    default=None,
                    metadata={
                        "name": "UnusedResidentialFinanceCostsBroughtForward",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class OtherUntaxedUkincome:
                other_untaxed_ukincome_share: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherUntaxedUKIncomeShare",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                other_untaxed_ukincome_adjustment: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherUntaxedUKIncomeAdjustment",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                loss_brought_forward: None | str = field(
                    default=None,
                    metadata={
                        "name": "LossBroughtForward",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                taxable_profit: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableProfit",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                other_untaxed_ukincome: (
                    None
                    | Mtr.Sa104F.ShareOfUntaxedIncome.OtherUntaxedUkincome.OtherUntaxedUkincomeInner
                ) = field(
                    default=None,
                    metadata={
                        "name": "OtherUntaxedUKIncome",
                        "type": "Element",
                    },
                )
                total_loss_to_carry_forward: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalLossToCarryForward",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

                @dataclass(kw_only=True)
                class OtherUntaxedUkincomeInner:
                    share_of_loss_from_other_untaxed_ukincome: None | str = field(
                        default=None,
                        metadata={
                            "name": "ShareOfLossFromOtherUntaxedUKIncome",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    adjustment_to_loss: None | str = field(
                        default=None,
                        metadata={
                            "name": "AdjustmentToLoss",
                            "type": "Element",
                            "min_exclusive": "-10000000000.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )

            @dataclass(kw_only=True)
            class OffshoreFundsIncome:
                offshore_funds_income_share: None | str = field(
                    default=None,
                    metadata={
                        "name": "OffshoreFundsIncomeShare",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                offshore_funds_income_adjustment: None | str = field(
                    default=None,
                    metadata={
                        "name": "OffshoreFundsIncomeAdjustment",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax_taken_off: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTaxTakenOff",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                taxable_income_after_adjustment_and_foreign_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableIncomeAfterAdjustmentAndForeignTax",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                offshore_fund_taxable_income_figclaim: None | str = field(
                    default=None,
                    metadata={
                        "name": "OffshoreFundTaxableIncomeFIGclaim",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class OtherUntaxedForeignIncome:
                other_untaxed_foreign_income_share: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherUntaxedForeignIncomeShare",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                other_untaxed_foreign_income_adjustment: None | str = field(
                    default=None,
                    metadata={
                        "name": "OtherUntaxedForeignIncomeAdjustment",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                loss_brought_forward: None | str = field(
                    default=None,
                    metadata={
                        "name": "LossBroughtForward",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                total_foreign_tax_taken_off: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalForeignTaxTakenOff",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                taxable_profit: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableProfit",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                taxable_profit_figclaim: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableProfitFIGclaim",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_losses: (
                    None
                    | Mtr.Sa104F.ShareOfUntaxedIncome.OtherUntaxedForeignIncome.ForeignLosses
                ) = field(
                    default=None,
                    metadata={
                        "name": "ForeignLosses",
                        "type": "Element",
                    },
                )
                residential_finance_costs: None | str = field(
                    default=None,
                    metadata={
                        "name": "ResidentialFinanceCosts",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                unused_residential_finance_costs_brought_forward: None | str = field(
                    default=None,
                    metadata={
                        "name": "UnusedResidentialFinanceCostsBroughtForward",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

                @dataclass(kw_only=True)
                class ForeignLosses:
                    share_of_loss_from_other_untaxed_foreign_income: None | str = field(
                        default=None,
                        metadata={
                            "name": "ShareOfLossFromOtherUntaxedForeignIncome",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    adjustment_to_loss: None | str = field(
                        default=None,
                        metadata={
                            "name": "AdjustmentToLoss",
                            "type": "Element",
                            "min_exclusive": "-10000000000.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    total_loss_to_carry_forward: None | str = field(
                        default=None,
                        metadata={
                            "name": "TotalLossToCarryForward",
                            "type": "Element",
                            "min_inclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )

        @dataclass(kw_only=True)
        class ShareOfPartnershipIncome:
            share_of_dividend_income: (
                None | Mtr.Sa104F.ShareOfPartnershipIncome.ShareOfDividendIncome
            ) = field(
                default=None,
                metadata={
                    "name": "ShareOfDividendIncome",
                    "type": "Element",
                },
            )
            share_of_taxed_income_taxable_at20_percent: (
                None
                | Mtr.Sa104F.ShareOfPartnershipIncome.ShareOfTaxedIncomeTaxableAt20Percent
            ) = field(
                default=None,
                metadata={
                    "name": "ShareOfTaxedIncomeTaxableAt20Percent",
                    "type": "Element",
                },
            )
            share_of_other_taxed_income: (
                None | Mtr.Sa104F.ShareOfPartnershipIncome.ShareOfOtherTaxedIncome
            ) = field(
                default=None,
                metadata={
                    "name": "ShareOfOtherTaxedIncome",
                    "type": "Element",
                },
            )
            share_of_total_taxed_and_untaxed_income: None | str = field(
                default=None,
                metadata={
                    "name": "ShareOfTotalTaxedAndUntaxedIncome",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_taxed_and_untaxed_income_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "TotalTaxedAndUntaxedIncomeFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

            @dataclass(kw_only=True)
            class ShareOfDividendIncome:
                dividend_income: None | str = field(
                    default=None,
                    metadata={
                        "name": "DividendIncome",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                total_foreign_tax_taken_off: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalForeignTaxTakenOff",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                total_dividend_income: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalDividendIncome",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                total_dividend_income_figclaim: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalDividendIncomeFIGclaim",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class ShareOfTaxedIncomeTaxableAt20Percent:
                share_of_taxed_income: None | str = field(
                    default=None,
                    metadata={
                        "name": "ShareOfTaxedIncome",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                total_foreign_tax_taken_off: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalForeignTaxTakenOff",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                taxed_income_taxable_at20_percent: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxedIncomeTaxableAt20Percent",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class ShareOfOtherTaxedIncome:
                share_of_taxed_income: None | str = field(
                    default=None,
                    metadata={
                        "name": "ShareOfTaxedIncome",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                total_foreign_tax_taken_off: None | str = field(
                    default=None,
                    metadata={
                        "name": "TotalForeignTaxTakenOff",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                share_of_other_taxed_income_figclaim: None | str = field(
                    default=None,
                    metadata={
                        "name": "ShareOfOtherTaxedIncomeFIGclaim",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class ShareOfPartnershipTaxPayed:
            share_of_income_tax_taken_off_partnership_income: None | str = field(
                default=None,
                metadata={
                    "name": "ShareOfIncomeTaxTakenOffPartnershipIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            share_of_tax_taken_off_by_contractors: None | str = field(
                default=None,
                metadata={
                    "name": "ShareOfTaxTakenOffByContractors",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            share_of_tax_taken_off_trading_income: None | str = field(
                default=None,
                metadata={
                    "name": "ShareOfTaxTakenOffTradingIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            share_of_total_tax_taken_off: None | str = field(
                default=None,
                metadata={
                    "name": "ShareOfTotalTaxTakenOff",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Sa104S:
        partnership_details: Mtr.Sa104S.PartnershipDetails = field(
            metadata={
                "name": "PartnershipDetails",
                "type": "Element",
                "required": True,
            }
        )
        share_of_partnership_trading_or_professional_profits: (
            None | Mtr.Sa104S.ShareOfPartnershipTradingOrProfessionalProfits
        ) = field(
            default=None,
            metadata={
                "name": "ShareOfPartnershipTradingOrProfessionalProfits",
                "type": "Element",
            },
        )
        share_of_partnership_trading_or_professional_losses: (
            None | Mtr.Sa104S.ShareOfPartnershipTradingOrProfessionalLosses
        ) = field(
            default=None,
            metadata={
                "name": "ShareOfPartnershipTradingOrProfessionalLosses",
                "type": "Element",
            },
        )
        nics: None | Mtr.Sa104S.Nics = field(
            default=None,
            metadata={
                "name": "NICs",
                "type": "Element",
            },
        )
        share_of_untaxed_interest_etc: None | str = field(
            default=None,
            metadata={
                "name": "ShareOfUntaxedInterestEtc",
                "type": "Element",
                "min_exclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        share_of_partnerships_tax_paid: None | Mtr.Sa104S.ShareOfPartnershipsTaxPaid = (
            field(
                default=None,
                metadata={
                    "name": "ShareOfPartnershipsTaxPaid",
                    "type": "Element",
                },
            )
        )
        any_other_information_space: None | str = field(
            default=None,
            metadata={
                "name": "AnyOtherInformationSpace",
                "type": "Element",
                "min_length": 1,
                "max_length": 20480,
                "pattern": r".*[^\s]+.*",
            },
        )

        @dataclass(kw_only=True)
        class PartnershipDetails:
            partnership_reference_number: str = field(
                metadata={
                    "name": "PartnershipReferenceNumber",
                    "type": "Element",
                    "required": True,
                    "length": 10,
                    "pattern": r"[0-9]{10}",
                }
            )
            partnership_description: str = field(
                metadata={
                    "name": "PartnershipDescription",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 28,
                    "pattern": r".*[^\s]+.*",
                }
            )
            did_you_join_the_partnership: MtrYesNoType = field(
                metadata={
                    "name": "DidYouJoinThePartnership",
                    "type": "Element",
                    "required": True,
                }
            )
            date_joined_partnership: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateJoinedPartnership",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            did_you_leave_the_partnership: MtrYesNoType = field(
                metadata={
                    "name": "DidYouLeaveThePartnership",
                    "type": "Element",
                    "required": True,
                }
            )
            date_left_partnership: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateLeftPartnership",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )

        @dataclass(kw_only=True)
        class ShareOfPartnershipTradingOrProfessionalProfits:
            share_of_partnership_profit_or_loss: None | str = field(
                default=None,
                metadata={
                    "name": "ShareOfPartnershipProfitOrLoss",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            tax_year_adjustment: None | str = field(
                default=None,
                metadata={
                    "name": "TaxYearAdjustment",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            change_of_accounting_practice_adjustment: None | str = field(
                default=None,
                metadata={
                    "name": "ChangeOfAccountingPracticeAdjustment",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                },
            )
            averaging_adjustment: None | str = field(
                default=None,
                metadata={
                    "name": "AveragingAdjustment",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            foreign_tax_claimed_as_deduction: None | str = field(
                default=None,
                metadata={
                    "name": "ForeignTaxClaimedAsDeduction",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            adjusted_profit_for_year: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustedProfitForYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            losses_brought_forward: None | str = field(
                default=None,
                metadata={
                    "name": "LossesBroughtForward",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            taxable_profits_after_losses: None | str = field(
                default=None,
                metadata={
                    "name": "TaxableProfitsAfterLosses",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_business_income: None | str = field(
                default=None,
                metadata={
                    "name": "OtherBusinessIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_taxable_business_profits: None | str = field(
                default=None,
                metadata={
                    "name": "TotalTaxableBusinessProfits",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class ShareOfPartnershipTradingOrProfessionalLosses:
            adjusted_loss_for_year: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustedLossForYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_set_off_against_other_income: None | str = field(
                default=None,
                metadata={
                    "name": "LossSetOffAgainstOtherIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_to_be_carried_back: None | str = field(
                default=None,
                metadata={
                    "name": "LossToBeCarriedBack",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_loss_to_carry_forward: None | str = field(
                default=None,
                metadata={
                    "name": "TotalLossToCarryForward",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class Nics:
            pay_class2_nicvoluntarily: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "PayClass2NICvoluntarily",
                    "type": "Element",
                },
            )
            class2_nicamount: None | str = field(
                default=None,
                metadata={
                    "name": "Class2NICamount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            class4_nicexempt: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "Class4NICexempt",
                    "type": "Element",
                },
            )
            adjustment_to_class4_nicprofits: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustmentToClass4NICProfits",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class ShareOfPartnershipsTaxPaid:
            share_of_tax_taken_off_by_contractors: None | str = field(
                default=None,
                metadata={
                    "name": "ShareOfTaxTakenOffByContractors",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            share_of_tax_taken_off_trading_income: None | str = field(
                default=None,
                metadata={
                    "name": "ShareOfTaxTakenOffTradingIncome",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Sa105:
        ukproperty_details: None | Mtr.Sa105.UkpropertyDetails = field(
            default=None,
            metadata={
                "name": "UKPropertyDetails",
                "type": "Element",
            },
        )
        property_income_and_expenses: None | Mtr.Sa105.PropertyIncomeAndExpenses = (
            field(
                default=None,
                metadata={
                    "name": "PropertyIncomeAndExpenses",
                    "type": "Element",
                },
            )
        )
        taxable_profit_or_loss: None | Mtr.Sa105.TaxableProfitOrLoss = field(
            default=None,
            metadata={
                "name": "TaxableProfitOrLoss",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class UkpropertyDetails:
            number_of_properties: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfProperties",
                    "type": "Element",
                    "max_inclusive": 99,
                },
            )
            property_income_ceased_in_year: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "PropertyIncomeCeasedInYear",
                    "type": "Element",
                },
            )
            income_from_property_let_jointly: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "IncomeFromPropertyLetJointly",
                    "type": "Element",
                },
            )
            rent_aroom_relief_claim: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "RentARoomReliefClaim",
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class PropertyIncomeAndExpenses:
            total_rents_and_other_income_from_property: None | str = field(
                default=None,
                metadata={
                    "name": "TotalRentsAndOtherIncomeFromProperty",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            property_income_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "PropertyIncomeAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "max_inclusive": "1000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            traditional_accounting: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "TraditionalAccounting",
                    "type": "Element",
                },
            )
            tax_taken_off_any_income: None | str = field(
                default=None,
                metadata={
                    "name": "TaxTakenOffAnyIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            premiums_for_grant_of_alease: None | str = field(
                default=None,
                metadata={
                    "name": "PremiumsForGrantOfALease",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            reverse_premiums_and_inducements: None | str = field(
                default=None,
                metadata={
                    "name": "ReversePremiumsAndInducements",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            rent_rates_insurance_and_ground_rents: None | str = field(
                default=None,
                metadata={
                    "name": "RentRatesInsuranceAndGroundRents",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            repairs_and_maintenance: None | str = field(
                default=None,
                metadata={
                    "name": "RepairsAndMaintenance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            allowable_interest_and_other_financial_charges: None | str = field(
                default=None,
                metadata={
                    "name": "AllowableInterestAndOtherFinancialCharges",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            legal_management_and_professional_fees: None | str = field(
                default=None,
                metadata={
                    "name": "LegalManagementAndProfessionalFees",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            costs_of_services_provided: None | str = field(
                default=None,
                metadata={
                    "name": "CostsOfServicesProvided",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_property_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "OtherPropertyExpenses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class TaxableProfitOrLoss:
            private_use_adjustment: None | str = field(
                default=None,
                metadata={
                    "name": "PrivateUseAdjustment",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            balancing_charges: None | str = field(
                default=None,
                metadata={
                    "name": "BalancingCharges",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            annual_investment_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "AnnualInvestmentAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            the_structures_and_buildings_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "TheStructuresAndBuildingsAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            electric_charge_point_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "ElectricChargePointAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            freeport_and_investment_zones_structures_and_buildings_allowance: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "FreeportAndInvestmentZonesStructuresAndBuildingsAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            zero_emission_car_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "ZeroEmissionCarAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            enhanced_capital_allowances: None | str = field(
                default=None,
                metadata={
                    "name": "EnhancedCapitalAllowances",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            costs_of_replacing_domestic_items: None | str = field(
                default=None,
                metadata={
                    "name": "CostsOfReplacingDomesticItems",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            rent_aroom_exempt_amount: None | str = field(
                default=None,
                metadata={
                    "name": "RentARoomExemptAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            adjusted_profit_for_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustedProfitForTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_brought_forward: None | str = field(
                default=None,
                metadata={
                    "name": "LossBroughtForward",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            taxable_profit_for_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "TaxableProfitForTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            adjusted_loss_for_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustedLossForTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_set_off_against_total_income_of_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "LossSetOffAgainstTotalIncomeOfTheYear",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            loss_to_carry_forward: None | str = field(
                default=None,
                metadata={
                    "name": "LossToCarryForward",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            residential_finance_costs: None | str = field(
                default=None,
                metadata={
                    "name": "ResidentialFinanceCosts",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            unused_residential_finance_costs_brought_forward: None | str = field(
                default=None,
                metadata={
                    "name": "UnusedResidentialFinanceCostsBroughtForward",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Sa106:
        unremittable_income: None | MtrYesType = field(
            default=None,
            metadata={
                "name": "UnremittableIncome",
                "type": "Element",
            },
        )
        foreign_tax_credit_relief: None | str = field(
            default=None,
            metadata={
                "name": "ForeignTaxCreditRelief",
                "type": "Element",
                "min_exclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        overseas_savings: None | Mtr.Sa106.OverseasSavings = field(
            default=None,
            metadata={
                "name": "OverseasSavings",
                "type": "Element",
            },
        )
        foreign_companies: None | Mtr.Sa106.ForeignCompanies = field(
            default=None,
            metadata={
                "name": "ForeignCompanies",
                "type": "Element",
            },
        )
        remitted_foreign_income: None | Mtr.Sa106.RemittedForeignIncome = field(
            default=None,
            metadata={
                "name": "RemittedForeignIncome",
                "type": "Element",
            },
        )
        remitted_foreign_dividends: None | Mtr.Sa106.RemittedForeignDividends = field(
            default=None,
            metadata={
                "name": "RemittedForeignDividends",
                "type": "Element",
            },
        )
        overseas_pensions: None | Mtr.Sa106.OverseasPensions = field(
            default=None,
            metadata={
                "name": "OverseasPensions",
                "type": "Element",
            },
        )
        overseas_dividend_income: None | Mtr.Sa106.OverseasDividendIncome = field(
            default=None,
            metadata={
                "name": "OverseasDividendIncome",
                "type": "Element",
            },
        )
        overseas_trust_income: None | Mtr.Sa106.OverseasTrustIncome = field(
            default=None,
            metadata={
                "name": "OverseasTrustIncome",
                "type": "Element",
            },
        )
        residential_property_income_or_restricted_finance_costs: None | str = field(
            default=None,
            metadata={
                "name": "ResidentialPropertyIncomeOrRestrictedFinanceCosts",
                "type": "Element",
                "min_inclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        unused_toaaresidential_finance_costs_brought_forward: None | str = field(
            default=None,
            metadata={
                "name": "UnusedTOAAresidentialFinanceCostsBroughtForward",
                "type": "Element",
                "min_inclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        overseas_land_and_property_income_details: list[
            Mtr.Sa106.OverseasLandAndPropertyIncomeDetails
        ] = field(
            default_factory=list,
            metadata={
                "name": "OverseasLandAndPropertyIncomeDetails",
                "type": "Element",
                "max_occurs": 6,
            },
        )
        total_adjusted_profit_or_loss: None | str = field(
            default=None,
            metadata={
                "name": "TotalAdjustedProfitOrLoss",
                "type": "Element",
                "min_exclusive": "-10000000000.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        loss_brought_forward: None | str = field(
            default=None,
            metadata={
                "name": "LossBroughtForward",
                "type": "Element",
                "min_exclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        total_taxable_profit: None | str = field(
            default=None,
            metadata={
                "name": "TotalTaxableProfit",
                "type": "Element",
                "min_inclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        total_foreign_tax_taken_off: None | str = field(
            default=None,
            metadata={
                "name": "TotalForeignTaxTakenOff",
                "type": "Element",
                "min_exclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        total_special_withholding_tax: None | str = field(
            default=None,
            metadata={
                "name": "TotalSpecialWithholdingTax",
                "type": "Element",
                "min_exclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        total_taxable_amount: None | str = field(
            default=None,
            metadata={
                "name": "TotalTaxableAmount",
                "type": "Element",
                "min_inclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        property_abroad_total_claimed_figregime: None | str = field(
            default=None,
            metadata={
                "name": "PropertyAbroadTotalClaimedFIGregime",
                "type": "Element",
                "min_exclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        loss_set_off_against_total_income: None | str = field(
            default=None,
            metadata={
                "name": "LossSetOffAgainstTotalIncome",
                "type": "Element",
                "min_exclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        loss_to_carry_forward: None | str = field(
            default=None,
            metadata={
                "name": "LossToCarryForward",
                "type": "Element",
                "min_inclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        foreign_tax_paid: list[Mtr.Sa106.ForeignTaxPaid] = field(
            default_factory=list,
            metadata={
                "name": "ForeignTaxPaid",
                "type": "Element",
                "max_occurs": 20,
            },
        )
        capital_gains: None | Mtr.Sa106.CapitalGains = field(
            default=None,
            metadata={
                "name": "CapitalGains",
                "type": "Element",
            },
        )
        other_overseas_income_and_gains: (
            None | Mtr.Sa106.OtherOverseasIncomeAndGains
        ) = field(
            default=None,
            metadata={
                "name": "OtherOverseasIncomeAndGains",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class OverseasSavings:
            income_source: list[Mtr.Sa106.OverseasSavings.IncomeSource] = field(
                default_factory=list,
                metadata={
                    "name": "IncomeSource",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                },
            )
            totals: None | MtrSa106SourceOfForeignIncomeTotals = field(
                default=None,
                metadata={
                    "name": "Totals",
                    "type": "Element",
                },
            )
            interest_total_claimed_figregime: None | str = field(
                default=None,
                metadata={
                    "name": "InterestTotalClaimedFIGregime",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

            @dataclass(kw_only=True)
            class IncomeSource:
                country_code: str = field(
                    metadata={
                        "name": "CountryCode",
                        "type": "Element",
                        "required": True,
                        "pattern": r"[A-Z]{3}",
                    }
                )
                income_before_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "IncomeBeforeTax",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                special_withholding_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "SpecialWithholdingTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                claim_to_ftcr: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "ClaimToFTCR",
                        "type": "Element",
                    },
                )
                taxable_amount_on_interest_and_other_savings: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableAmountOnInterestAndOtherSavings",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class ForeignCompanies:
            income_source: list[Mtr.Sa106.ForeignCompanies.IncomeSource] = field(
                default_factory=list,
                metadata={
                    "name": "IncomeSource",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                },
            )
            totals: None | MtrSa106SourceOfForeignIncomeTotals = field(
                default=None,
                metadata={
                    "name": "Totals",
                    "type": "Element",
                },
            )
            dividends_total_claimed_figregime: None | str = field(
                default=None,
                metadata={
                    "name": "DividendsTotalClaimedFIGregime",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

            @dataclass(kw_only=True)
            class IncomeSource:
                country_code: str = field(
                    metadata={
                        "name": "CountryCode",
                        "type": "Element",
                        "required": True,
                        "pattern": r"[A-Z]{3}",
                    }
                )
                income_before_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "IncomeBeforeTax",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                special_withholding_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "SpecialWithholdingTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                claim_to_ftcr: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "ClaimToFTCR",
                        "type": "Element",
                    },
                )
                taxable_amount_on_interest_and_other_savings: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableAmountOnInterestAndOtherSavings",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class RemittedForeignIncome:
            income_source: list[Mtr.Sa106.RemittedForeignIncome.IncomeSource] = field(
                default_factory=list,
                metadata={
                    "name": "IncomeSource",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                },
            )
            totals: None | MtrSa106SourceOfForeignIncomeTotalsRemitted = field(
                default=None,
                metadata={
                    "name": "Totals",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class IncomeSource:
                country_code: str = field(
                    metadata={
                        "name": "CountryCode",
                        "type": "Element",
                        "required": True,
                        "pattern": r"[A-Z]{3}",
                    }
                )
                income_before_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "IncomeBeforeTax",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                special_withholding_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "SpecialWithholdingTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                claim_to_ftcr: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "ClaimToFTCR",
                        "type": "Element",
                    },
                )
                taxable_amount: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableAmount",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class RemittedForeignDividends:
            income_source: list[Mtr.Sa106.RemittedForeignDividends.IncomeSource] = (
                field(
                    default_factory=list,
                    metadata={
                        "name": "IncomeSource",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 20,
                    },
                )
            )
            totals: None | MtrSa106SourceOfForeignIncomeTotalsRemitted = field(
                default=None,
                metadata={
                    "name": "Totals",
                    "type": "Element",
                },
            )
            amount_subject_to_dividend_tax_credit: None | str = field(
                default=None,
                metadata={
                    "name": "AmountSubjectToDividendTaxCredit",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

            @dataclass(kw_only=True)
            class IncomeSource:
                country_code: str = field(
                    metadata={
                        "name": "CountryCode",
                        "type": "Element",
                        "required": True,
                        "pattern": r"[A-Z]{3}",
                    }
                )
                income_before_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "IncomeBeforeTax",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                special_withholding_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "SpecialWithholdingTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                claim_to_ftcr: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "ClaimToFTCR",
                        "type": "Element",
                    },
                )
                taxable_amount: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableAmount",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class OverseasPensions:
            income_source: list[Mtr.Sa106.OverseasPensions.IncomeSource] = field(
                default_factory=list,
                metadata={
                    "name": "IncomeSource",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                },
            )
            totals: None | MtrSa106SourceOfForeignIncomeTotals = field(
                default=None,
                metadata={
                    "name": "Totals",
                    "type": "Element",
                },
            )
            pensions_total_claimed_figregime: None | str = field(
                default=None,
                metadata={
                    "name": "PensionsTotalClaimedFIGregime",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

            @dataclass(kw_only=True)
            class IncomeSource:
                country_code: str = field(
                    metadata={
                        "name": "CountryCode",
                        "type": "Element",
                        "required": True,
                        "pattern": r"[A-Z]{3}",
                    }
                )
                income_before_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "IncomeBeforeTax",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                special_withholding_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "SpecialWithholdingTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                claim_to_ftcr: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "ClaimToFTCR",
                        "type": "Element",
                    },
                )
                taxable_amount_on_interest_and_other_savings: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableAmountOnInterestAndOtherSavings",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class OverseasDividendIncome:
            income_source: list[Mtr.Sa106.OverseasDividendIncome.IncomeSource] = field(
                default_factory=list,
                metadata={
                    "name": "IncomeSource",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 10,
                },
            )
            totals: None | MtrSa106SourceOfForeignIncomeTotals = field(
                default=None,
                metadata={
                    "name": "Totals",
                    "type": "Element",
                },
            )
            dividend_from_overseas_trust_etc_total_claimed_figregime: None | str = (
                field(
                    default=None,
                    metadata={
                        "name": "DividendFromOverseasTrustEtcTotalClaimedFIGregime",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
            )

            @dataclass(kw_only=True)
            class IncomeSource:
                country_code: str = field(
                    metadata={
                        "name": "CountryCode",
                        "type": "Element",
                        "required": True,
                        "pattern": r"[A-Z]{3}",
                    }
                )
                income_before_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "IncomeBeforeTax",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                special_withholding_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "SpecialWithholdingTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                claim_to_ftcr: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "ClaimToFTCR",
                        "type": "Element",
                    },
                )
                taxable_amount_on_interest_and_other_savings: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableAmountOnInterestAndOtherSavings",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class OverseasTrustIncome:
            income_source: list[Mtr.Sa106.OverseasTrustIncome.IncomeSource] = field(
                default_factory=list,
                metadata={
                    "name": "IncomeSource",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 10,
                },
            )
            totals: None | MtrSa106SourceOfForeignIncomeTotals = field(
                default=None,
                metadata={
                    "name": "Totals",
                    "type": "Element",
                },
            )
            overseas_trusts_etc_other_income_total_claimed_figregime: None | str = (
                field(
                    default=None,
                    metadata={
                        "name": "OverseasTrustsEtcOtherIncomeTotalClaimedFIGregime",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
            )

            @dataclass(kw_only=True)
            class IncomeSource:
                country_code: str = field(
                    metadata={
                        "name": "CountryCode",
                        "type": "Element",
                        "required": True,
                        "pattern": r"[A-Z]{3}",
                    }
                )
                income_before_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "IncomeBeforeTax",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                special_withholding_tax: None | str = field(
                    default=None,
                    metadata={
                        "name": "SpecialWithholdingTax",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                claim_to_ftcr: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "ClaimToFTCR",
                        "type": "Element",
                    },
                )
                taxable_amount_on_interest_and_other_savings: None | str = field(
                    default=None,
                    metadata={
                        "name": "TaxableAmountOnInterestAndOtherSavings",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class OverseasLandAndPropertyIncomeDetails:
            total_rents_and_other_property_receipts: None | str = field(
                default=None,
                metadata={
                    "name": "TotalRentsAndOtherPropertyReceipts",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            property_income_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "PropertyIncomeAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "max_inclusive": "1000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            traditional_accounting: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "TraditionalAccounting",
                    "type": "Element",
                },
            )
            number_of_properties: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfProperties",
                    "type": "Element",
                    "min_inclusive": 1,
                    "max_inclusive": 99,
                },
            )
            premiums_paid_for_lease: None | str = field(
                default=None,
                metadata={
                    "name": "PremiumsPaidForLease",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            allowable_property_expenses: None | str = field(
                default=None,
                metadata={
                    "name": "AllowablePropertyExpenses",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            net_profit_or_loss: None | str = field(
                default=None,
                metadata={
                    "name": "NetProfitOrLoss",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            private_use_adjustment: None | str = field(
                default=None,
                metadata={
                    "name": "PrivateUseAdjustment",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            balancing_charges: None | str = field(
                default=None,
                metadata={
                    "name": "BalancingCharges",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            capital_allowances: None | str = field(
                default=None,
                metadata={
                    "name": "CapitalAllowances",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            zero_emission_car_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "ZeroEmissionCarAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            the_structures_and_buildings_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "TheStructuresAndBuildingsAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            electric_charge_point_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "ElectricChargePointAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            costs_of_replacing_domestic_items: None | str = field(
                default=None,
                metadata={
                    "name": "CostsOfReplacingDomesticItems",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            adjusted_profit_or_loss_for_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustedProfitOrLossForTheYear",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            residential_finance_costs: None | str = field(
                default=None,
                metadata={
                    "name": "ResidentialFinanceCosts",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            unused_residential_finance_costs_brought_forward: None | str = field(
                default=None,
                metadata={
                    "name": "UnusedResidentialFinanceCostsBroughtForward",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            property_abroad_country: None | str = field(
                default=None,
                metadata={
                    "name": "PropertyAbroadCountry",
                    "type": "Element",
                    "pattern": r"[A-Z]{3}",
                },
            )
            property_abroad_profit_or_loss: None | str = field(
                default=None,
                metadata={
                    "name": "PropertyAbroadProfitOrLoss",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            property_abroad_foreign_tax: None | str = field(
                default=None,
                metadata={
                    "name": "PropertyAbroadForeignTax",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            property_abroad_uktax_taken_off: None | str = field(
                default=None,
                metadata={
                    "name": "PropertyAbroadUKtaxTakenOff",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            property_abroad_claim_to_ftcr: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "PropertyAbroadClaimToFTCR",
                    "type": "Element",
                },
            )
            property_abroad_total_amount: None | str = field(
                default=None,
                metadata={
                    "name": "PropertyAbroadTotalAmount",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class ForeignTaxPaid:
            claim_to_ftcrcountry_code: None | str = field(
                default=None,
                metadata={
                    "name": "ClaimToFTCRCountryCode",
                    "type": "Element",
                    "pattern": r"[A-Z]{3}",
                },
            )
            claim_to_ftcrforeign_tax: None | str = field(
                default=None,
                metadata={
                    "name": "ClaimToFTCRForeignTax",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            claim_to_ftcrclaim_for_ftcr: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ClaimToFTCRClaimForFTCR",
                    "type": "Element",
                },
            )
            claim_to_ftcramount_chargable: None | str = field(
                default=None,
                metadata={
                    "name": "ClaimToFTCRAmountChargable",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class CapitalGains:
            chargeable_gains_ukrules: (
                None | Mtr.Sa106.CapitalGains.ChargeableGainsUkrules
            ) = field(
                default=None,
                metadata={
                    "name": "ChargeableGainsUKRules",
                    "type": "Element",
                },
            )
            chargeable_gains_foreign_rules: (
                None | Mtr.Sa106.CapitalGains.ChargeableGainsForeignRules
            ) = field(
                default=None,
                metadata={
                    "name": "ChargeableGainsForeignRules",
                    "type": "Element",
                },
            )
            foreign_tax_paid: None | str = field(
                default=None,
                metadata={
                    "name": "ForeignTaxPaid",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            foreign_tax_credit_relief_claim: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ForeignTaxCreditReliefClaim",
                    "type": "Element",
                },
            )
            total_foreign_tax_credit_relief_on_gains: None | str = field(
                default=None,
                metadata={
                    "name": "TotalForeignTaxCreditReliefOnGains",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            special_withholding_tax: None | str = field(
                default=None,
                metadata={
                    "name": "SpecialWithholdingTax",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

            @dataclass(kw_only=True)
            class ChargeableGainsUkrules:
                chargeable_gains: None | str = field(
                    default=None,
                    metadata={
                        "name": "ChargeableGains",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                number_of_days_over_which_gain_accrued: None | int = field(
                    default=None,
                    metadata={
                        "name": "NumberOfDaysOverWhichGainAccrued",
                        "type": "Element",
                        "min_inclusive": 1,
                        "max_inclusive": 99999,
                    },
                )

            @dataclass(kw_only=True)
            class ChargeableGainsForeignRules:
                chargeable_gains: None | str = field(
                    default=None,
                    metadata={
                        "name": "ChargeableGains",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                number_of_days_over_which_gain_accrued: None | int = field(
                    default=None,
                    metadata={
                        "name": "NumberOfDaysOverWhichGainAccrued",
                        "type": "Element",
                        "min_inclusive": 1,
                        "max_inclusive": 99999,
                    },
                )

        @dataclass(kw_only=True)
        class OtherOverseasIncomeAndGains:
            foreign_life_insurance_gains: None | str = field(
                default=None,
                metadata={
                    "name": "ForeignLifeInsuranceGains",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            number_of_years_since_policy_made: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfYearsSincePolicyMade",
                    "type": "Element",
                    "min_inclusive": 1,
                    "max_inclusive": 99,
                },
            )
            tax_treated_as_paid: None | str = field(
                default=None,
                metadata={
                    "name": "TaxTreatedAsPaid",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            omitted_amount_transfer_of_assets_exemption: None | str = field(
                default=None,
                metadata={
                    "name": "OmittedAmountTransferOfAssetsExemption",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            non_savings_income_nrsitrusts: (
                None | Mtr.Sa106.OtherOverseasIncomeAndGains.NonSavingsIncomeNrsitrusts
            ) = field(
                default=None,
                metadata={
                    "name": "NonSavingsIncomeNRSItrusts",
                    "type": "Element",
                },
            )
            overseas_residential_property_or_restricted_finance_costs_for_non_resident_trust: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "OverseasResidentialPropertyOrRestrictedFinanceCostsForNonResidentTrust",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            unused_overseas_residential_finance_costs_brought_forward: None | str = (
                field(
                    default=None,
                    metadata={
                        "name": "UnusedOverseasResidentialFinanceCostsBroughtForward",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
            )
            savings_income_nrsitrusts: (
                None | Mtr.Sa106.OtherOverseasIncomeAndGains.SavingsIncomeNrsitrusts
            ) = field(
                default=None,
                metadata={
                    "name": "SavingsIncomeNRSItrusts",
                    "type": "Element",
                },
            )
            dividend_income_nrsitrusts: (
                None | Mtr.Sa106.OtherOverseasIncomeAndGains.DividendIncomeNrsitrusts
            ) = field(
                default=None,
                metadata={
                    "name": "DividendIncomeNRSItrusts",
                    "type": "Element",
                },
            )
            discretionary_income_arising_from_nsinrtrusts: None | str = field(
                default=None,
                metadata={
                    "name": "DiscretionaryIncomeArisingFromNSINRtrusts",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            discretionary_income_arising_from_nsinrtrusts_figregime_claim_amount: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "DiscretionaryIncomeArisingFromNSINRtrustsFIGregimeClaimAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            capital_sums_paid_to_settlor_by_trustees: None | str = field(
                default=None,
                metadata={
                    "name": "CapitalSumsPaidToSettlorByTrustees",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            capital_sums_paid_to_settlor_by_trustees_figregime_claim_amount: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "CapitalSumsPaidToSettlorByTrusteesFIGregimeClaimAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_on_disposal_of_holdings_in_offshore_fund: None | str = field(
                default=None,
                metadata={
                    "name": "GainsOnDisposalOfHoldingsInOffshoreFund",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_on_disposal_of_holdings_in_offshore_fund_figregime_claim_amount: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "GainsOnDisposalOfHoldingsInOffshoreFundFIGregimeClaimAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            non_trade_income: None | str = field(
                default=None,
                metadata={
                    "name": "NonTradeIncome",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            non_trade_income_figregime_claim_amount: None | str = field(
                default=None,
                metadata={
                    "name": "NonTradeIncomeFIGregimeClaimAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_received_by_non_transferors_under_to_aa: None | str = field(
                default=None,
                metadata={
                    "name": "BenefitsReceivedByNonTransferorsUnderToAA",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_received_by_non_transferors_under_to_aafigregime_claim_amount: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "BenefitsReceivedByNonTransferorsUnderToAAFIGregimeClaimAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_received_by_transferor_matched_to_tpior_pfsitaxable_under_to_aa: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "BenefitsReceivedByTransferorMatchedToTPIorPFSItaxableUnderToAA",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_received_by_transferor_matched_to_tpior_pfsitaxable_under_to_aafigregime_claim_amount: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "BenefitsReceivedByTransferorMatchedToTPIorPFSItaxableUnderToAAFIGregimeClaimAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_chargeable_under_close_family_member_rules: None | str = field(
                default=None,
                metadata={
                    "name": "BenefitsChargeableUnderCloseFamilyMemberRules",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_chargeable_under_close_family_member_rules_figregime_claim_amount: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "BenefitsChargeableUnderCloseFamilyMemberRulesFIGregimeClaimAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_chargeable_under_onward_gifts_rules_under_to_aa: None | str = (
                field(
                    default=None,
                    metadata={
                        "name": "BenefitsChargeableUnderOnwardGiftsRulesUnderToAA",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
            )
            benefits_chargeable_under_onward_gifts_rules_under_to_aafigregime_claim_amount: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "BenefitsChargeableUnderOnwardGiftsRulesUnderToAAFIGregimeClaimAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_received_by_settlor_matched_to_ttior_pfsi: None | str = field(
                default=None,
                metadata={
                    "name": "BenefitsReceivedBySettlorMatchedToTTIorPFSI",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_received_by_settlor_matched_to_ttior_pfsifigregime_claim_amount: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "BenefitsReceivedBySettlorMatchedToTTIorPFSIFIGregimeClaimAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_received_by_close_family_member_matched_to_ttior_pfsi: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "BenefitsReceivedByCloseFamilyMemberMatchedToTTIorPFSI",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_received_by_close_family_member_matched_to_ttior_pfsifigregime_claim_amount: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "BenefitsReceivedByCloseFamilyMemberMatchedToTTIorPFSIFIGregimeClaimAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_chargeable_under_onward_gifts_rules_under_settlements: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "BenefitsChargeableUnderOnwardGiftsRulesUnderSettlements",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            benefits_chargeable_under_onward_gifts_rules_under_settlements_figregime_claim_amount: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "BenefitsChargeableUnderOnwardGiftsRulesUnderSettlementsFIGregimeClaimAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

            @dataclass(kw_only=True)
            class NonSavingsIncomeNrsitrusts:
                income_source: list[
                    Mtr.Sa106.OtherOverseasIncomeAndGains.NonSavingsIncomeNrsitrusts.IncomeSource
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "IncomeSource",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 5,
                    },
                )
                totals: None | MtrSa106SourceOfForeignIncomeTotals = field(
                    default=None,
                    metadata={
                        "name": "Totals",
                        "type": "Element",
                    },
                )
                non_savings_income_nrsitrusts_total_claimed_figregime: None | str = (
                    field(
                        default=None,
                        metadata={
                            "name": "NonSavingsIncomeNRSItrustsTotalClaimedFIGregime",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                )

                @dataclass(kw_only=True)
                class IncomeSource:
                    country_code: str = field(
                        metadata={
                            "name": "CountryCode",
                            "type": "Element",
                            "required": True,
                            "pattern": r"[A-Z]{3}",
                        }
                    )
                    income_before_tax: None | str = field(
                        default=None,
                        metadata={
                            "name": "IncomeBeforeTax",
                            "type": "Element",
                            "min_inclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    foreign_tax: None | str = field(
                        default=None,
                        metadata={
                            "name": "ForeignTax",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    special_withholding_tax: None | str = field(
                        default=None,
                        metadata={
                            "name": "SpecialWithholdingTax",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    claim_to_ftcr: None | MtrYesType = field(
                        default=None,
                        metadata={
                            "name": "ClaimToFTCR",
                            "type": "Element",
                        },
                    )
                    taxable_amount_on_interest_and_other_savings: None | str = field(
                        default=None,
                        metadata={
                            "name": "TaxableAmountOnInterestAndOtherSavings",
                            "type": "Element",
                            "min_inclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )

            @dataclass(kw_only=True)
            class SavingsIncomeNrsitrusts:
                income_source: list[
                    Mtr.Sa106.OtherOverseasIncomeAndGains.SavingsIncomeNrsitrusts.IncomeSource
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "IncomeSource",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 5,
                    },
                )
                totals: None | MtrSa106SourceOfForeignIncomeTotals = field(
                    default=None,
                    metadata={
                        "name": "Totals",
                        "type": "Element",
                    },
                )
                savings_income_nrsitrusts_total_claimed_figregime: None | str = field(
                    default=None,
                    metadata={
                        "name": "SavingsIncomeNRSItrustsTotalClaimedFIGregime",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

                @dataclass(kw_only=True)
                class IncomeSource:
                    country_code: str = field(
                        metadata={
                            "name": "CountryCode",
                            "type": "Element",
                            "required": True,
                            "pattern": r"[A-Z]{3}",
                        }
                    )
                    income_before_tax: None | str = field(
                        default=None,
                        metadata={
                            "name": "IncomeBeforeTax",
                            "type": "Element",
                            "min_inclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    foreign_tax: None | str = field(
                        default=None,
                        metadata={
                            "name": "ForeignTax",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    special_withholding_tax: None | str = field(
                        default=None,
                        metadata={
                            "name": "SpecialWithholdingTax",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    claim_to_ftcr: None | MtrYesType = field(
                        default=None,
                        metadata={
                            "name": "ClaimToFTCR",
                            "type": "Element",
                        },
                    )
                    taxable_amount_on_interest_and_other_savings: None | str = field(
                        default=None,
                        metadata={
                            "name": "TaxableAmountOnInterestAndOtherSavings",
                            "type": "Element",
                            "min_inclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )

            @dataclass(kw_only=True)
            class DividendIncomeNrsitrusts:
                income_source: list[
                    Mtr.Sa106.OtherOverseasIncomeAndGains.DividendIncomeNrsitrusts.IncomeSource
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "IncomeSource",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 5,
                    },
                )
                totals: None | MtrSa106SourceOfForeignIncomeTotals = field(
                    default=None,
                    metadata={
                        "name": "Totals",
                        "type": "Element",
                    },
                )
                dividend_income_nrsitrusts_total_claimed_figregime: None | str = field(
                    default=None,
                    metadata={
                        "name": "DividendIncomeNRSItrustsTotalClaimedFIGregime",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

                @dataclass(kw_only=True)
                class IncomeSource:
                    country_code: str = field(
                        metadata={
                            "name": "CountryCode",
                            "type": "Element",
                            "required": True,
                            "pattern": r"[A-Z]{3}",
                        }
                    )
                    income_before_tax: None | str = field(
                        default=None,
                        metadata={
                            "name": "IncomeBeforeTax",
                            "type": "Element",
                            "min_inclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    foreign_tax: None | str = field(
                        default=None,
                        metadata={
                            "name": "ForeignTax",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    special_withholding_tax: None | str = field(
                        default=None,
                        metadata={
                            "name": "SpecialWithholdingTax",
                            "type": "Element",
                            "min_exclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )
                    claim_to_ftcr: None | MtrYesType = field(
                        default=None,
                        metadata={
                            "name": "ClaimToFTCR",
                            "type": "Element",
                        },
                    )
                    taxable_amount_on_interest_and_other_savings: None | str = field(
                        default=None,
                        metadata={
                            "name": "TaxableAmountOnInterestAndOtherSavings",
                            "type": "Element",
                            "min_inclusive": "0.00",
                            "max_exclusive": "10000000000.00",
                            "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                        },
                    )

    @dataclass(kw_only=True)
    class Sa107:
        income_from_trusts_and_settlements: (
            None | Mtr.Sa107.IncomeFromTrustsAndSettlements
        ) = field(
            default=None,
            metadata={
                "name": "IncomeFromTrustsAndSettlements",
                "type": "Element",
            },
        )
        income_chargeable_on_settlors: None | Mtr.Sa107.IncomeChargeableOnSettlors = (
            field(
                default=None,
                metadata={
                    "name": "IncomeChargeableOnSettlors",
                    "type": "Element",
                },
            )
        )
        income_from_estates: None | Mtr.Sa107.IncomeFromEstates = field(
            default=None,
            metadata={
                "name": "IncomeFromEstates",
                "type": "Element",
            },
        )
        foreign_tax: None | str = field(
            default=None,
            metadata={
                "name": "ForeignTax",
                "type": "Element",
                "min_exclusive": "0.00",
                "max_exclusive": "10000000000.00",
                "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
            },
        )
        income_from_residential_property: (
            None | Mtr.Sa107.IncomeFromResidentialProperty
        ) = field(
            default=None,
            metadata={
                "name": "IncomeFromResidentialProperty",
                "type": "Element",
            },
        )
        any_other_information_space: None | str = field(
            default=None,
            metadata={
                "name": "AnyOtherInformationSpace",
                "type": "Element",
                "min_length": 1,
                "max_length": 20480,
                "pattern": r".*[^\s]+.*",
            },
        )

        @dataclass(kw_only=True)
        class IncomeFromTrustsAndSettlements:
            discretionary_income_payment: (
                None
                | Mtr.Sa107.IncomeFromTrustsAndSettlements.DiscretionaryIncomePayment
            ) = field(
                default=None,
                metadata={
                    "name": "DiscretionaryIncomePayment",
                    "type": "Element",
                },
            )
            nondiscretionary_income_entitlement_from_trusts: (
                None
                | Mtr.Sa107.IncomeFromTrustsAndSettlements.NondiscretionaryIncomeEntitlementFromTrusts
            ) = field(
                default=None,
                metadata={
                    "name": "NondiscretionaryIncomeEntitlementFromTrusts",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class DiscretionaryIncomePayment:
                discretionary_income_payment_net_amount: None | str = field(
                    default=None,
                    metadata={
                        "name": "DiscretionaryIncomePaymentNetAmount",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                payments_from_settlor_interested_trusts: None | str = field(
                    default=None,
                    metadata={
                        "name": "PaymentsFromSettlorInterestedTrusts",
                        "type": "Element",
                        "min_exclusive": "-10000000000.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?[0-9.]*[1-9]+[0-9.]*",
                    },
                )

            @dataclass(kw_only=True)
            class NondiscretionaryIncomeEntitlementFromTrusts:
                non_discretionary_income_taxed_at_basic_rate: None | str = field(
                    default=None,
                    metadata={
                        "name": "NonDiscretionaryIncomeTaxedAtBasicRate",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                non_discretionary_income_taxed_at_lower_rate: None | str = field(
                    default=None,
                    metadata={
                        "name": "NonDiscretionaryIncomeTaxedAtLowerRate",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                non_discretionary_income_taxed_at_dividend_rate: None | str = field(
                    default=None,
                    metadata={
                        "name": "NonDiscretionaryIncomeTaxedAtDividendRate",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                income_from_trusts_etc_non_resident_trustees: None | MtrYesType = field(
                    default=None,
                    metadata={
                        "name": "IncomeFromTrustsEtcNonResidentTrustees",
                        "type": "Element",
                    },
                )

        @dataclass(kw_only=True)
        class IncomeChargeableOnSettlors:
            net_settlor_income_taxed_at_basic_rate: None | str = field(
                default=None,
                metadata={
                    "name": "NetSettlorIncomeTaxedAtBasicRate",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            net_settlor_income_taxed_at_lower_rate: None | str = field(
                default=None,
                metadata={
                    "name": "NetSettlorIncomeTaxedAtLowerRate",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            net_settlor_income_taxed_at_dividend_rate: None | str = field(
                default=None,
                metadata={
                    "name": "NetSettlorIncomeTaxedAtDividendRate",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            net_settlor_income_taxed_at_trust_rate: None | str = field(
                default=None,
                metadata={
                    "name": "NetSettlorIncomeTaxedAtTrustRate",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            savings_income_at_trust_rate: None | str = field(
                default=None,
                metadata={
                    "name": "SavingsIncomeAtTrustRate",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            net_settlor_income_taxed_at_dividend_trust_rate: None | str = field(
                default=None,
                metadata={
                    "name": "NetSettlorIncomeTaxedAtDividendTrustRate",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gross_settlor_income_to_be_taxed_at_basic_rate: None | str = field(
                default=None,
                metadata={
                    "name": "GrossSettlorIncomeToBeTaxedAtBasicRate",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gross_settlor_income_to_be_taxed_at_lower_rate: None | str = field(
                default=None,
                metadata={
                    "name": "GrossSettlorIncomeToBeTaxedAtLowerRate",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            amount_of_uklife_insurance_policy: None | str = field(
                default=None,
                metadata={
                    "name": "AmountOfUKLifeInsurancePolicy",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class IncomeFromEstates:
            ukestates: None | Mtr.Sa107.IncomeFromEstates.Ukestates = field(
                default=None,
                metadata={
                    "name": "UKEstates",
                    "type": "Element",
                },
            )
            foreign_estates: None | Mtr.Sa107.IncomeFromEstates.ForeignEstates = field(
                default=None,
                metadata={
                    "name": "ForeignEstates",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Ukestates:
                estate_income_taxed_at_basic_rate: None | str = field(
                    default=None,
                    metadata={
                        "name": "EstateIncomeTaxedAtBasicRate",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                estate_income_taxed_at_lower_rate: None | str = field(
                    default=None,
                    metadata={
                        "name": "EstateIncomeTaxedAtLowerRate",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                estate_income_taxed_at_dividend_rate: None | str = field(
                    default=None,
                    metadata={
                        "name": "EstateIncomeTaxedAtDividendRate",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                estate_income_already_taxed_at75dividend_rate: None | str = field(
                    default=None,
                    metadata={
                        "name": "EstateIncomeAlreadyTaxedAt75dividendRate",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                estate_income_taxed_at_nonrepayable_basic_rate: None | str = field(
                    default=None,
                    metadata={
                        "name": "EstateIncomeTaxedAtNonrepayableBasicRate",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

            @dataclass(kw_only=True)
            class ForeignEstates:
                foreign_estate_income: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignEstateIncome",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                foreign_estate_income_figclaim: None | str = field(
                    default=None,
                    metadata={
                        "name": "ForeignEstateIncomeFIGclaim",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
                relief_for_uktax_accounted_for: None | str = field(
                    default=None,
                    metadata={
                        "name": "ReliefForUKTaxAccountedFor",
                        "type": "Element",
                        "min_exclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )

        @dataclass(kw_only=True)
        class IncomeFromResidentialProperty:
            residential_property_income_or_restricted_finance_costs: None | str = field(
                default=None,
                metadata={
                    "name": "ResidentialPropertyIncomeOrRestrictedFinanceCosts",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            unused_residential_finance_costs_brought_forward: None | str = field(
                default=None,
                metadata={
                    "name": "UnusedResidentialFinanceCostsBroughtForward",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Sa108:
        residential_property_and_carried_interest: (
            None | Mtr.Sa108.ResidentialPropertyAndCarriedInterest
        ) = field(
            default=None,
            metadata={
                "name": "ResidentialPropertyAndCarriedInterest",
                "type": "Element",
            },
        )
        cryptoassets: None | Mtr.Sa108.Cryptoassets = field(
            default=None,
            metadata={
                "name": "Cryptoassets",
                "type": "Element",
            },
        )
        other_property_assets_and_gains: (
            None | Mtr.Sa108.OtherPropertyAssetsAndGains
        ) = field(
            default=None,
            metadata={
                "name": "OtherPropertyAssetsAndGains",
                "type": "Element",
            },
        )
        listed_shares_and_securities: None | Mtr.Sa108.ListedSharesAndSecurities = (
            field(
                default=None,
                metadata={
                    "name": "ListedSharesAndSecurities",
                    "type": "Element",
                },
            )
        )
        unlisted_shares_and_securities: None | Mtr.Sa108.UnlistedSharesAndSecurities = (
            field(
                default=None,
                metadata={
                    "name": "UnlistedSharesAndSecurities",
                    "type": "Element",
                },
            )
        )
        losses_and_adjustments: None | Mtr.Sa108.LossesAndAdjustments = field(
            default=None,
            metadata={
                "name": "LossesAndAdjustments",
                "type": "Element",
            },
        )
        nrcgton_ukproperty_or_land_and_indirect_disposals: (
            None | Mtr.Sa108.NrcgtonUkpropertyOrLandAndIndirectDisposals
        ) = field(
            default=None,
            metadata={
                "name": "NRCGTonUKpropertyOrLandAndIndirectDisposals",
                "type": "Element",
            },
        )
        eisand_qahc: None | Mtr.Sa108.EisandQahc = field(
            default=None,
            metadata={
                "name": "EISandQAHC",
                "type": "Element",
            },
        )
        estimate_or_valuation: None | MtrYesType = field(
            default=None,
            metadata={
                "name": "EstimateOrValuation",
                "type": "Element",
            },
        )
        any_other_information_space: None | str = field(
            default=None,
            metadata={
                "name": "AnyOtherInformationSpace",
                "type": "Element",
                "min_length": 1,
                "max_length": 20480,
                "pattern": r".*[^\s]+.*",
            },
        )

        @dataclass(kw_only=True)
        class ResidentialPropertyAndCarriedInterest:
            number_of_disposals: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfDisposals",
                    "type": "Element",
                    "max_inclusive": 99999,
                },
            )
            disposal_proceeds: None | str = field(
                default=None,
                metadata={
                    "name": "DisposalProceeds",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            allowable_costs: None | str = field(
                default=None,
                metadata={
                    "name": "AllowableCosts",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_on_residential_property_in_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "GainsOnResidentialPropertyInTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_on_residential_property_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "GainsOnResidentialPropertyFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            losses_in_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "LossesInTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            claim_or_election_made: None | str = field(
                default=None,
                metadata={
                    "name": "ClaimOrElectionMade",
                    "type": "Element",
                    "pattern": r"[A-Z]{3}",
                },
            )
            gain_or_loss_from_ukproperty_disposal: None | str = field(
                default=None,
                metadata={
                    "name": "GainOrLossFromUKpropertyDisposal",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            ukproperty_disposal_tax_already_charged: None | str = field(
                default=None,
                metadata={
                    "name": "UKpropertyDisposalTaxAlreadyCharged",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gain_or_loss_from_rttreturn: None | str = field(
                default=None,
                metadata={
                    "name": "GainOrLossFromRTTreturn",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            rtttax_already_charged: None | str = field(
                default=None,
                metadata={
                    "name": "RTTtaxAlreadyCharged",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            carried_interest_arising_basis: None | str = field(
                default=None,
                metadata={
                    "name": "CarriedInterestArisingBasis",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            carried_interest_accruals_basis: None | str = field(
                default=None,
                metadata={
                    "name": "CarriedInterestAccrualsBasis",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_on_carried_interest_in_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "GainsOnCarriedInterestInTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_on_carried_interest_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "GainsOnCarriedInterestFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class Cryptoassets:
            number_of_disposals: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfDisposals",
                    "type": "Element",
                    "max_inclusive": 99999,
                },
            )
            disposal_proceeds: None | str = field(
                default=None,
                metadata={
                    "name": "DisposalProceeds",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            allowable_costs: None | str = field(
                default=None,
                metadata={
                    "name": "AllowableCosts",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_in_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "GainsInTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            losses_in_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "LossesInTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            claim_or_election_made: None | str = field(
                default=None,
                metadata={
                    "name": "ClaimOrElectionMade",
                    "type": "Element",
                    "pattern": r"[A-Z]{3}",
                },
            )
            gain_from_rttreturn: None | str = field(
                default=None,
                metadata={
                    "name": "GainFromRTTreturn",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            rtttax_already_charged: None | str = field(
                default=None,
                metadata={
                    "name": "RTTtaxAlreadyCharged",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class OtherPropertyAssetsAndGains:
            number_of_disposals: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfDisposals",
                    "type": "Element",
                    "max_inclusive": 99999,
                },
            )
            disposal_proceeds: None | str = field(
                default=None,
                metadata={
                    "name": "DisposalProceeds",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            allowable_costs: None | str = field(
                default=None,
                metadata={
                    "name": "AllowableCosts",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_in_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "GainsInTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "GainsFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            non_residential_disposals_included_in_box17: None | str = field(
                default=None,
                metadata={
                    "name": "NonResidentialDisposalsIncludedInBox17",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            land_and_property_disposals_where_badris_being_claimed: None | str = field(
                default=None,
                metadata={
                    "name": "LandAndPropertyDisposalsWhereBADRisBeingClaimed",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            shares_disposals_where_badris_being_claimed: None | str = field(
                default=None,
                metadata={
                    "name": "SharesDisposalsWhereBADRisBeingClaimed",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            other_disposals_where_badris_being_claimed: None | str = field(
                default=None,
                metadata={
                    "name": "OtherDisposalsWhereBADRisBeingClaimed",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            losses_in_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "LossesInTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            claim_or_election_made: None | str = field(
                default=None,
                metadata={
                    "name": "ClaimOrElectionMade",
                    "type": "Element",
                    "pattern": r"[A-Z]{3}",
                },
            )
            gain_from_rttreturn: None | str = field(
                default=None,
                metadata={
                    "name": "GainFromRTTreturn",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            rtttax_already_charged: None | str = field(
                default=None,
                metadata={
                    "name": "RTTtaxAlreadyCharged",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class ListedSharesAndSecurities:
            number_of_disposals: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfDisposals",
                    "type": "Element",
                    "max_inclusive": 99999,
                },
            )
            disposal_proceeds: None | str = field(
                default=None,
                metadata={
                    "name": "DisposalProceeds",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            allowable_costs: None | str = field(
                default=None,
                metadata={
                    "name": "AllowableCosts",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_in_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "GainsInTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "GainsFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            losses_in_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "LossesInTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            claim_or_election_made: None | str = field(
                default=None,
                metadata={
                    "name": "ClaimOrElectionMade",
                    "type": "Element",
                    "pattern": r"[A-Z]{3}",
                },
            )
            gain_from_rttreturn: None | str = field(
                default=None,
                metadata={
                    "name": "GainFromRTTreturn",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            rtttax_already_charged: None | str = field(
                default=None,
                metadata={
                    "name": "RTTtaxAlreadyCharged",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class UnlistedSharesAndSecurities:
            number_of_disposals: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfDisposals",
                    "type": "Element",
                    "max_inclusive": 99999,
                },
            )
            disposal_proceeds: None | str = field(
                default=None,
                metadata={
                    "name": "DisposalProceeds",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            allowable_costs: None | str = field(
                default=None,
                metadata={
                    "name": "AllowableCosts",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_in_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "GainsInTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "GainsFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            losses_in_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "LossesInTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            claim_or_election_made: None | str = field(
                default=None,
                metadata={
                    "name": "ClaimOrElectionMade",
                    "type": "Element",
                    "pattern": r"[A-Z]{3}",
                },
            )
            gain_from_rttreturn: None | str = field(
                default=None,
                metadata={
                    "name": "GainFromRTTreturn",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            rtttax_already_charged: None | str = field(
                default=None,
                metadata={
                    "name": "RTTtaxAlreadyCharged",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_exceeding_esslimit: None | str = field(
                default=None,
                metadata={
                    "name": "GainsExceedingESSlimit",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_invested_under_seed_eis: None | str = field(
                default=None,
                metadata={
                    "name": "GainsInvestedUnderSeedEIS",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            losses_used_against_return_year_income: None | str = field(
                default=None,
                metadata={
                    "name": "LossesUsedAgainstReturnYearIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            seisand_eisloss_relief_in_return_year: None | str = field(
                default=None,
                metadata={
                    "name": "SEISandEISlossReliefInReturnYear",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            losses_used_against_previous_return_year_income: None | str = field(
                default=None,
                metadata={
                    "name": "LossesUsedAgainstPreviousReturnYearIncome",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            seisand_eisloss_relief_in_previous_return_year: None | str = field(
                default=None,
                metadata={
                    "name": "SEISandEISlossReliefInPreviousReturnYear",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class LossesAndAdjustments:
            losses_brought_forward_and_used_in_the_return_year: None | str = field(
                default=None,
                metadata={
                    "name": "LossesBroughtForwardAndUsedInTheReturnYear",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            income_losses_of_the_return_year_set_against_gains: None | str = field(
                default=None,
                metadata={
                    "name": "IncomeLossesOfTheReturnYearSetAgainstGains",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            losses_to_be_carried_forward: None | str = field(
                default=None,
                metadata={
                    "name": "LossesToBeCarriedForward",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            losses_used_against_earlier_return_years_gain: None | str = field(
                default=None,
                metadata={
                    "name": "LossesUsedAgainstEarlierReturnYearsGain",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_qualifying_for_investors_relief: None | str = field(
                default=None,
                metadata={
                    "name": "GainsQualifyingForInvestorsRelief",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            gains_qualifying_for_business_asset_disposal_relief: None | str = field(
                default=None,
                metadata={
                    "name": "GainsQualifyingForBusinessAssetDisposalRelief",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            badrand_erclaimed_to_date: None | str = field(
                default=None,
                metadata={
                    "name": "BADRandERclaimedToDate",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            adjustment_to_cgt: None | str = field(
                default=None,
                metadata={
                    "name": "AdjustmentToCGT",
                    "type": "Element",
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            non_residentdual_resident_trust_liability: None | str = field(
                default=None,
                metadata={
                    "name": "NonResidentdualResidentTrustLiability",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class NrcgtonUkpropertyOrLandAndIndirectDisposals:
            total_gains_chargeable_for_direct_disposals_for_ukresidential_property: (
                None | str
            ) = field(
                default=None,
                metadata={
                    "name": "TotalGainsChargeableForDirectDisposalsForUKresidentialProperty",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_gains_chargeable_for_direct_disposals_for_uknrproperty: None | str = (
                field(
                    default=None,
                    metadata={
                        "name": "TotalGainsChargeableForDirectDisposalsForUKNRproperty",
                        "type": "Element",
                        "min_inclusive": "0.00",
                        "max_exclusive": "10000000000.00",
                        "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                    },
                )
            )
            gains_from_indirect_disposals: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "GainsFromIndirectDisposals",
                    "type": "Element",
                },
            )
            tax_on_gains_already_charged: None | str = field(
                default=None,
                metadata={
                    "name": "TaxOnGainsAlreadyCharged",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_losses_available_against_nrcgtgains_for_the_year: None | str = field(
                default=None,
                metadata={
                    "name": "TotalLossesAvailableAgainstNRCGTgainsForTheYear",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class EisandQahc:
            total_gains_from_eis: None | str = field(
                default=None,
                metadata={
                    "name": "TotalGainsFromEIS",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            eisgains_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "EISgainsFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_gains_from_qahc: None | str = field(
                default=None,
                metadata={
                    "name": "TotalGainsFromQAHC",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            qahcgains_figclaim: None | str = field(
                default=None,
                metadata={
                    "name": "QAHCgainsFIGclaim",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_losses_from_qahc: None | str = field(
                default=None,
                metadata={
                    "name": "TotalLossesFromQAHC",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Sa109:
        residence_status: None | Mtr.Sa109.ResidenceStatus = field(
            default=None,
            metadata={
                "name": "ResidenceStatus",
                "type": "Element",
            },
        )
        time_spent_in_uk: None | Mtr.Sa109.TimeSpentInUk = field(
            default=None,
            metadata={
                "name": "TimeSpentInUK",
                "type": "Element",
            },
        )
        personal_allowances: None | Mtr.Sa109.PersonalAllowances = field(
            default=None,
            metadata={
                "name": "PersonalAllowances",
                "type": "Element",
            },
        )
        residence_in_other_countries: None | Mtr.Sa109.ResidenceInOtherCountries = (
            field(
                default=None,
                metadata={
                    "name": "ResidenceInOtherCountries",
                    "type": "Element",
                },
            )
        )
        figowrtrf: None | Mtr.Sa109.Figowrtrf = field(
            default=None,
            metadata={
                "name": "FIGOWRTRF",
                "type": "Element",
            },
        )
        foreign_income_and_gains_figrelief: (
            None | Mtr.Sa109.ForeignIncomeAndGainsFigrelief
        ) = field(
            default=None,
            metadata={
                "name": "ForeignIncomeAndGainsFIGrelief",
                "type": "Element",
            },
        )
        remittance_basis: None | Mtr.Sa109.RemittanceBasis = field(
            default=None,
            metadata={
                "name": "RemittanceBasis",
                "type": "Element",
            },
        )
        overseas_workday_relief_owr: None | Mtr.Sa109.OverseasWorkdayReliefOwr = field(
            default=None,
            metadata={
                "name": "OverseasWorkdayReliefOWR",
                "type": "Element",
            },
        )
        temporary_repatriation_facility_trf: (
            None | Mtr.Sa109.TemporaryRepatriationFacilityTrf
        ) = field(
            default=None,
            metadata={
                "name": "TemporaryRepatriationFacilityTRF",
                "type": "Element",
            },
        )
        any_other_information_space: None | str = field(
            default=None,
            metadata={
                "name": "AnyOtherInformationSpace",
                "type": "Element",
                "min_length": 1,
                "max_length": 20480,
                "pattern": r".*[^\s]+.*",
            },
        )

        @dataclass(kw_only=True)
        class ResidenceStatus:
            not_resident_in_uk: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "NotResidentInUK",
                    "type": "Element",
                },
            )
            request_for_split_year_treatment: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "RequestForSplitYearTreatment",
                    "type": "Element",
                },
            )
            more_than_one_case_of_split_year_treatment_applies: None | MtrYesType = (
                field(
                    default=None,
                    metadata={
                        "name": "MoreThanOneCaseOfSplitYearTreatmentApplies",
                        "type": "Element",
                    },
                )
            )
            resident_in_ukfor_previous_year: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ResidentInUKForPreviousYear",
                    "type": "Element",
                },
            )
            split_year_treatment_date_from_which_the_ukpart_year_begins_or_ends: (
                None | XmlDate
            ) = field(
                default=None,
                metadata={
                    "name": "SplitYearTreatmentDateFromWhichTheUKpartYearBeginsOrEnds",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            meet_the_third_automatic_overseas_test: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "MeetTheThirdAutomaticOverseasTest",
                    "type": "Element",
                },
            )
            had_agap_between_employments_in_this_tax_year: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "HadAGapBetweenEmploymentsInThisTaxYear",
                    "type": "Element",
                },
            )
            had_ahome_overseas: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "HadAHomeOverseas",
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class TimeSpentInUk:
            number_of_days_spent_in_uk: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfDaysSpentInUK",
                    "type": "Element",
                    "min_inclusive": 0,
                    "max_inclusive": 366,
                },
            )
            number_of_days_due_to_exceptional_circumstances: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfDaysDueToExceptionalCircumstances",
                    "type": "Element",
                    "min_inclusive": 0,
                    "max_inclusive": 60,
                },
            )
            number_of_days_in_ukwhile_in_transit: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfDaysInUKwhileInTransit",
                    "type": "Element",
                    "min_inclusive": 0,
                    "max_inclusive": 366,
                },
            )
            how_many_ties_to_uk: None | int = field(
                default=None,
                metadata={
                    "name": "HowManyTiesToUK",
                    "type": "Element",
                    "max_inclusive": 999,
                },
            )
            number_of_workdays_in_ukfor_employment: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfWorkdaysInUKForEmployment",
                    "type": "Element",
                    "min_inclusive": 0,
                    "max_inclusive": 366,
                },
            )
            number_of_workdays_spent_overseas: None | int = field(
                default=None,
                metadata={
                    "name": "NumberOfWorkdaysSpentOverseas",
                    "type": "Element",
                    "min_inclusive": 0,
                    "max_inclusive": 366,
                },
            )

        @dataclass(kw_only=True)
        class PersonalAllowances:
            personal_allowances_claim_due_to_dta: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "PersonalAllowancesClaimDueToDTA",
                    "type": "Element",
                },
            )
            personal_allowances_claim_on_other_basis: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "PersonalAllowancesClaimOnOtherBasis",
                    "type": "Element",
                },
            )
            code_for_country_of_nationality_or_residence: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "CodeForCountryOfNationalityOrResidence",
                    "type": "Element",
                    "max_occurs": 3,
                    "max_length": 3,
                    "pattern": r"[A-Z]{3}",
                },
            )

        @dataclass(kw_only=True)
        class ResidenceInOtherCountries:
            code_for_country_of_residence_for_tax_in_year: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "CodeForCountryOfResidenceForTaxInYear",
                    "type": "Element",
                    "max_occurs": 2,
                    "max_length": 3,
                    "pattern": r"[A-Z]{3}",
                },
            )
            code_for_country_of_residence_in_previous_year: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "CodeForCountryOfResidenceInPreviousYear",
                    "type": "Element",
                    "max_occurs": 2,
                    "max_length": 3,
                    "pattern": r"[A-Z]{3}",
                },
            )
            amount_of_dtaincome_for_which_partial_relief_is_claimed: None | str = field(
                default=None,
                metadata={
                    "name": "AmountOfDTAincomeForWhichPartialReliefIsClaimed",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            dtarelief_claim_residence_in_another_country: None | str = field(
                default=None,
                metadata={
                    "name": "DTAReliefClaimResidenceInAnotherCountry",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            dtarelief_claim_other_provisions: None | str = field(
                default=None,
                metadata={
                    "name": "DTAReliefClaimOtherProvisions",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class Figowrtrf:
            date_of_arrival_in_the_uk: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "DateOfArrivalInTheUK",
                    "type": "Element",
                    "min_inclusive": XmlDate(1851, 1, 1),
                    "max_inclusive": XmlDate(2040, 1, 1),
                },
            )
            ukresident_prior_to_recent_arrival: None | str = field(
                default=None,
                metadata={
                    "name": "UKresidentPriorToRecentArrival",
                    "type": "Element",
                    "pattern": r"[0-9]{4}-[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class ForeignIncomeAndGainsFigrelief:
            claim_for_relief_on_foreign_income_under_fig: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ClaimForReliefOnForeignIncomeUnderFIG",
                    "type": "Element",
                },
            )
            claim_for_relief_on_foreign_gains_under_fig: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ClaimForReliefOnForeignGainsUnderFIG",
                    "type": "Element",
                },
            )
            qahcincome_or_gains: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "QAHCincomeOrGains",
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class RemittanceBasis:
            remitted_income_or_gains: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "RemittedIncomeOrGains",
                    "type": "Element",
                },
            )
            amount_of_relief_claimed_for_investment_in_qualifying_business: str = field(
                metadata={
                    "name": "AmountOfReliefClaimedForInvestmentInQualifyingBusiness",
                    "type": "Element",
                    "required": True,
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                }
            )
            company_registration_number: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "CompanyRegistrationNumber",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 3,
                    "min_length": 8,
                    "max_length": 8,
                    "pattern": r"([A-Z]{2}|[0-9]{2})[0-9]{6}",
                },
            )
            previous_investment_no_longer_qualifies: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "PreviousInvestmentNoLongerQualifies",
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class OverseasWorkdayReliefOwr:
            owrelection: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "OWRelection",
                    "type": "Element",
                },
            )
            owrclaim: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "OWRclaim",
                    "type": "Element",
                },
            )
            owrtransitional_provisions_claim: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "OWRtransitionalProvisionsClaim",
                    "type": "Element",
                },
            )
            qualifying_employment_income_after_deductions: None | str = field(
                default=None,
                metadata={
                    "name": "QualifyingEmploymentIncomeAfterDeductions",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            qualifying_foreign_employment_income_after_deductions: None | str = field(
                default=None,
                metadata={
                    "name": "QualifyingForeignEmploymentIncomeAfterDeductions",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            maximum_relief: None | str = field(
                default=None,
                metadata={
                    "name": "MaximumRelief",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            owrclaimed: None | str = field(
                default=None,
                metadata={
                    "name": "OWRclaimed",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            total_amount_relief_claimed: None | str = field(
                default=None,
                metadata={
                    "name": "TotalAmountReliefClaimed",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class TemporaryRepatriationFacilityTrf:
            election_under_trf: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ElectionUnderTRF",
                    "type": "Element",
                },
            )
            personal_trfdesignation_amount: None | str = field(
                default=None,
                metadata={
                    "name": "PersonalTRFdesignationAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            capital_payments_and_benefits_received_from_trusts: None | str = field(
                default=None,
                metadata={
                    "name": "CapitalPaymentsAndBenefitsReceivedFromTrusts",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            personal_trfdesignation_remitted_amount: None | str = field(
                default=None,
                metadata={
                    "name": "PersonalTRFdesignationRemittedAmount",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Sa110:
        self_assessment: Mtr.Sa110.SelfAssessment = field(
            metadata={
                "name": "SelfAssessment",
                "type": "Element",
                "required": True,
            }
        )
        underpaid_tax: Mtr.Sa110.UnderpaidTax = field(
            metadata={
                "name": "UnderpaidTax",
                "type": "Element",
                "required": True,
            }
        )
        payments_on_account: None | Mtr.Sa110.PaymentsOnAccount = field(
            default=None,
            metadata={
                "name": "PaymentsOnAccount",
                "type": "Element",
            },
        )
        surplus_allowances: None | Mtr.Sa110.SurplusAllowances = field(
            default=None,
            metadata={
                "name": "SurplusAllowances",
                "type": "Element",
            },
        )
        adjustments_to_tax_due: None | Mtr.Sa110.AdjustmentsToTaxDue = field(
            default=None,
            metadata={
                "name": "AdjustmentsToTaxDue",
                "type": "Element",
            },
        )
        any_other_information_space: None | str = field(
            default=None,
            metadata={
                "name": "AnyOtherInformationSpace",
                "type": "Element",
                "min_length": 1,
                "max_length": 20480,
                "pattern": r".*[^\s]+.*",
            },
        )

        @dataclass(kw_only=True)
        class SelfAssessment:
            total_tax_etc_due: str = field(
                metadata={
                    "name": "TotalTaxEtcDue",
                    "type": "Element",
                    "required": True,
                    "min_exclusive": "-10000000000.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                }
            )
            student_loan_repayment_due: None | str = field(
                default=None,
                metadata={
                    "name": "StudentLoanRepaymentDue",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            postgraduate_loan_repayment_due: None | str = field(
                default=None,
                metadata={
                    "name": "PostgraduateLoanRepaymentDue",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            class4_nics_due: None | str = field(
                default=None,
                metadata={
                    "name": "Class4NICsDue",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            class2_nics_due: None | str = field(
                default=None,
                metadata={
                    "name": "Class2NICsDue",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            capital_gains_tax_due: None | str = field(
                default=None,
                metadata={
                    "name": "CapitalGainsTaxDue",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            pension_charges_due: None | str = field(
                default=None,
                metadata={
                    "name": "PensionChargesDue",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class UnderpaidTax:
            underpaid_tax_for_earlier_years_included_in_code: None | str = field(
                default=None,
                metadata={
                    "name": "UnderpaidTaxForEarlierYearsIncludedInCode",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            underpaid_tax_for_year_included_in_future_code: None | str = field(
                default=None,
                metadata={
                    "name": "UnderpaidTaxForYearIncludedInFutureCode",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "max_inclusive": "999999.99",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            outstanding_debt_coded_out_amount: None | str = field(
                default=None,
                metadata={
                    "name": "OutstandingDebtCodedOutAmount",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class PaymentsOnAccount:
            claim_to_reduce_payments_on_account: None | MtrYesType = field(
                default=None,
                metadata={
                    "name": "ClaimToReducePaymentsOnAccount",
                    "type": "Element",
                },
            )
            first_payment_on_account: None | str = field(
                default=None,
                metadata={
                    "name": "FirstPaymentOnAccount",
                    "type": "Element",
                    "min_inclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class SurplusAllowances:
            surplus_blind_persons_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "SurplusBlindPersonsAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            surplus_married_couples_allowance: None | str = field(
                default=None,
                metadata={
                    "name": "SurplusMarriedCouplesAllowance",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

        @dataclass(kw_only=True)
        class AdjustmentsToTaxDue:
            increase_in_tax_from_adjustment_to_earlier_years: None | str = field(
                default=None,
                metadata={
                    "name": "IncreaseInTaxFromAdjustmentToEarlierYears",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            decrease_in_tax_from_adjustment_to_earlier_years: None | str = field(
                default=None,
                metadata={
                    "name": "DecreaseInTaxFromAdjustmentToEarlierYears",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )
            next_years_repayment_claimed_now: None | str = field(
                default=None,
                metadata={
                    "name": "NextYearsRepaymentClaimedNow",
                    "type": "Element",
                    "min_exclusive": "0.00",
                    "max_exclusive": "10000000000.00",
                    "pattern": r"-?(([1-9][0-9]*)|0)\.[0-9]{2}",
                },
            )

    @dataclass(kw_only=True)
    class Declaration:
        individual_declaration: None | MtrYesType = field(
            default=None,
            metadata={
                "name": "IndividualDeclaration",
                "type": "Element",
            },
        )
        agent_declaration: None | MtrYesType = field(
            default=None,
            metadata={
                "name": "AgentDeclaration",
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class AttachedFiles:
        attachment: list[Mtr.AttachedFiles.Attachment] = field(
            default_factory=list,
            metadata={
                "name": "Attachment",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class Attachment:
            value: bytes = field(
                default=b"",
                metadata={
                    "required": True,
                    "format": "base64",
                },
            )
            file_format: AttachmentFileFormat = field(
                metadata={
                    "name": "FileFormat",
                    "type": "Attribute",
                    "required": True,
                }
            )
            filename: str = field(
                metadata={
                    "name": "Filename",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r".*\.pdf",
                }
            )
            size: None | int = field(
                default=None,
                metadata={
                    "name": "Size",
                    "type": "Attribute",
                },
            )
            description: None | str = field(
                default=None,
                metadata={
                    "name": "Description",
                    "type": "Attribute",
                    "pattern": r"[^£$#~|€]+",
                },
            )


@dataclass(kw_only=True)
class MtrTelephoneStructure:
    class Meta:
        name = "MTR_TelephoneStructure"

    number: str = field(
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9\(\)\-\s]{1,35}",
        }
    )
    extension: None | str = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
            "min_length": 1,
            "max_length": 6,
            "pattern": r"[0-9]{1,6}",
        },
    )
    type_value: None | MtrWorkHomeType = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    mobile: None | MtrYesNoType = field(
        default=None,
        metadata={
            "name": "Mobile",
            "type": "Attribute",
        },
    )
    preferred: None | MtrYesNoType = field(
        default=None,
        metadata={
            "name": "Preferred",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class MtrContactDetailsStructure:
    class Meta:
        name = "MTR_ContactDetailsStructure"

    name: None | MtrContactDetailsStructure.Name = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
        },
    )
    email: list[MtrContactDetailsStructure.Email] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
        },
    )
    telephone: list[MtrTelephoneStructure] = field(
        default_factory=list,
        metadata={
            "name": "Telephone",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
        },
    )
    fax: list[MtrTelephoneStructure] = field(
        default_factory=list,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
        },
    )

    @dataclass(kw_only=True)
    class Name:
        ttl: None | str = field(
            default=None,
            metadata={
                "name": "Ttl",
                "type": "Element",
                "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
                "min_length": 1,
                "max_length": 4,
                "pattern": r"[A-Za-z][A-Za-z'\-]*",
            },
        )
        fore: list[str] = field(
            default_factory=list,
            metadata={
                "name": "Fore",
                "type": "Element",
                "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
                "min_occurs": 1,
                "max_occurs": 2,
                "min_length": 1,
                "max_length": 35,
                "pattern": r"[A-Za-z][A-Za-z'\-]*",
            },
        )
        sur: str = field(
            metadata={
                "name": "Sur",
                "type": "Element",
                "namespace": "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1",
                "required": True,
                "min_length": 1,
                "max_length": 35,
                "pattern": r"[A-Za-z0-9 ,\.\(\)/&\-']+",
            }
        )

    @dataclass(kw_only=True)
    class Email:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 3,
                "max_length": 254,
                "pattern": r'[^@\'<>"]+@[^@\'<>"]+',
            },
        )
        type_value: None | MtrWorkHomeType = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            },
        )
        preferred: None | MtrYesNoType = field(
            default=None,
            metadata={
                "name": "Preferred",
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class Irheader:
    """
    :ivar keys: This element contains identifiers for the sender of the
        message. Each identifier is contained within a &lt;Key&gt;
        element. Each &lt;Key&gt; element also contains a 'Type'
        attribute which describes the identifier type (e.g. &lt;Key
        Type='UTR'&gt;, &lt;Key Type='TaxOfficeNumber'&gt;, &lt;Key
        Type='TaxOfficeReference'&gt;).
    :ivar period_end:
    :ivar principal:
    :ivar agent:
    :ivar default_currency:
    :ivar manifest:
    :ivar irmark:
    :ivar sender:
    """

    class Meta:
        name = "IRheader"
        namespace = "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1"

    keys: None | Irheader.Keys = field(
        default=None,
        metadata={
            "name": "Keys",
            "type": "Element",
        },
    )
    period_end: XmlDate = field(
        metadata={
            "name": "PeriodEnd",
            "type": "Element",
            "required": True,
        }
    )
    principal: None | Irheader.Principal = field(
        default=None,
        metadata={
            "name": "Principal",
            "type": "Element",
        },
    )
    agent: None | Irheader.Agent = field(
        default=None,
        metadata={
            "name": "Agent",
            "type": "Element",
        },
    )
    default_currency: None | IrheaderDefaultCurrency = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Element",
        },
    )
    manifest: None | Irheader.Manifest = field(
        default=None,
        metadata={
            "name": "Manifest",
            "type": "Element",
        },
    )
    irmark: None | Irheader.Irmark = field(
        default=None,
        metadata={
            "name": "IRmark",
            "type": "Element",
        },
    )
    sender: IrheaderSender = field(
        metadata={
            "name": "Sender",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Keys:
        key: list[Irheader.Keys.Key] = field(
            default_factory=list,
            metadata={
                "name": "Key",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class Key:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                    "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./]*",
                },
            )
            type_value: None | str = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                    "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./]*",
                },
            )

    @dataclass(kw_only=True)
    class Principal:
        contact: MtrContactDetailsStructure = field(
            metadata={
                "name": "Contact",
                "type": "Element",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Agent:
        """
        :ivar agent_id: This identifier is for the agent's own reference
            and is not the same as any agent's credentials that might be
            used to identify the agent to the Government Gateway.
        :ivar company:
        :ivar address:
        :ivar contact:
        """

        agent_id: None | str = field(
            default=None,
            metadata={
                "name": "AgentID",
                "type": "Element",
                "min_length": 1,
                "max_length": 35,
                "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./]*",
            },
        )
        company: None | str = field(
            default=None,
            metadata={
                "name": "Company",
                "type": "Element",
                "min_length": 1,
                "max_length": 35,
                "pattern": r"[A-Za-z0-9 &'\(\)\*,\-\./]*",
            },
        )
        address: None | Irheader.Agent.Address = field(
            default=None,
            metadata={
                "name": "Address",
                "type": "Element",
            },
        )
        contact: None | MtrContactDetailsStructure = field(
            default=None,
            metadata={
                "name": "Contact",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class Address:
            line: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "Line",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 4,
                    "min_length": 1,
                    "max_length": 35,
                    "pattern": r'[A-Za-z0-9 ~!"@#$%&\'\(\)\*\+,\-\./:;<=>\?\[\\\]^_\{\}£€]*',
                },
            )
            post_code: None | str = field(
                default=None,
                metadata={
                    "name": "PostCode",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 8,
                    "pattern": r'[A-Za-z0-9 ~!"@#$%&\'\(\)\*\+,\-\./:;<=>\?\[\\\]^_\{\}£€]*',
                },
            )
            country: None | str = field(
                default=None,
                metadata={
                    "name": "Country",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 35,
                    "pattern": r'[A-Za-z0-9 ~!"@#$%&\'\(\)\*\+,\-\./:;<=>\?\[\\\]^_\{\}£€]*',
                },
            )

    @dataclass(kw_only=True)
    class Manifest:
        contains: Irheader.Manifest.Contains = field(
            metadata={
                "name": "Contains",
                "type": "Element",
                "required": True,
            }
        )

        @dataclass(kw_only=True)
        class Contains:
            reference: list[Irheader.Manifest.Contains.Reference] = field(
                default_factory=list,
                metadata={
                    "name": "Reference",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class Reference:
                namespace: str = field(
                    metadata={
                        "name": "Namespace",
                        "type": "Element",
                        "required": True,
                    }
                )
                schema_version: str = field(
                    metadata={
                        "name": "SchemaVersion",
                        "type": "Element",
                        "required": True,
                        "max_length": 13,
                        "pattern": r"[0-9]{4}\-v[0-9]{1,3}\.[0-9]{1,3}(\.[0-9]{1,3})?",
                    }
                )
                top_element_name: str = field(
                    metadata={
                        "name": "TopElementName",
                        "type": "Element",
                        "required": True,
                    }
                )

    @dataclass(kw_only=True)
    class Irmark:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        type_value: IrmarkType = field(
            metadata={
                "name": "Type",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass(kw_only=True)
class Irenvelope:
    """
    :ivar irheader: The following elements from the IRheader are
        required for SA MTR returns: Keys, PeriodEnd, DefaultCurrency,
        Manifest, IRmark
    :ivar mtr:
    """

    class Meta:
        name = "IRenvelope"
        namespace = "http://www.govtalk.gov.uk/taxation/SA/SA100/25-26/1"

    irheader: Irheader = field(
        metadata={
            "name": "IRheader",
            "type": "Element",
            "required": True,
        }
    )
    mtr: Mtr = field(
        metadata={
            "name": "MTR",
            "type": "Element",
            "required": True,
        }
    )
