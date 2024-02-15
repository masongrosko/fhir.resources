# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/medicationorder.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import backboneelement, domainresource, fhirtypes
from .codeableconcept import CodeableConcept
from .duration import Duration
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .reference import Reference
from .timing import Timing


class MedicationOrder(domainresource.DomainResource):
    """Prescription of medication to for patient.

    An order for both supply of the medication and the instructions for
    administration of the medication to a patient. The resource is called
    "MedicationOrder" rather than "MedicationPrescription" to generalize the
    use across inpatient and outpatient settings as well as for care plans,
    etc.
    """

    resource_type: str = Field("MedicationOrder", const=True)

    dateEnded: fhirtypes.DateTime = Field(
        None,
        alias="dateEnded",
        title="Type `Date` (represented as `str` in JSON).",
        description="When prescription was stopped.",
    )

    dateWritten: fhirtypes.DateTime = Field(
        None,
        alias="dateWritten",
        title="Type `Date` (represented as `str` in JSON).",
        description="When prescription was authorized.",
    )

    dispenseRequest: "MedicationOrderDispenseRequest" = Field(
        None,
        alias="dispenseRequest",
        title="Type `MedicationOrderDispenseRequest` (represented as `dict` in JSON).",
        description="Medication supply authorization.",
    )

    dosageInstruction: ListType["MedicationOrderDosageInstruction"] = Field(
        None,
        alias="dosageInstruction",
        title=(
            "List of `MedicationOrderDosageInstruction` items (represented as `dict` "
            "in JSON)."
        ),
        description="How medication should be taken.",
    )

    encounter: Reference = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in JSON)."
        ),
        description="Created during encounter/admission/stay.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="External identifier.",
    )

    medicationCodeableConcept: CodeableConcept = Field(
        None,
        alias="medicationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Medication to be taken.",
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
    )

    medicationReference: Reference = Field(
        None,
        alias="medicationReference",
        title=(
            "Type `Reference` referencing `Medication` (represented as `dict` in JSON)."
        ),
        description="Medication to be taken.",
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication"],
    )

    note: fhirtypes.String = Field(
        None,
        alias="note",
        title="Type `str`.",
        description="Information about the prescription.",
    )

    patient: Reference = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="Who prescription is for.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    prescriber: Reference = Field(
        None,
        alias="prescriber",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)."
        ),
        description="Who ordered the medication(s).",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    priorPrescription: Reference = Field(
        None,
        alias="priorPrescription",
        title=(
            "Type `Reference` referencing `MedicationOrder` (represented as `dict` in "
            "JSON)."
        ),
        description="An order/prescription that this supersedes.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationOrder"],
    )

    reasonCodeableConcept: CodeableConcept = Field(
        None,
        alias="reasonCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Reason or indication for writing the prescription.",
        # Choice of Data Types. i.e medication[x]
        one_of_many="reason",
        one_of_many_required=False,
    )

    reasonEnded: CodeableConcept = Field(
        None,
        alias="reasonEnded",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Why prescription was stopped.",
    )

    reasonReference: Reference = Field(
        None,
        alias="reasonReference",
        title=(
            "Type `Reference` referencing `Condition` (represented as `dict` in JSON)."
        ),
        description="Reason or indication for writing the prescription.",
        # Choice of Data Types. i.e reason[x]
        one_of_many="reason",
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `str`.",
        description="active | on-hold | completed | entered-in-error | stopped | draft.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "active",
            "on-hold",
            "completed",
            "entered-in-error",
            "stopped",
            "draft",
        ],
    )

    substitution: "MedicationOrderSubstitution" = Field(
        None,
        alias="substitution",
        title="Type `MedicationOrderSubstitution` (represented as `dict` in JSON).",
        description="Any restrictions on medication substitution.",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "medication": ["medicationCodeableConcept", "medicationReference"],
            "reason": ["reasonCodeableConcept", "reasonReference"],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class MedicationOrderDispenseRequest(backboneelement.BackboneElement):
    """Medication supply authorization.

    Indicates the specific details for the dispense or medication supply part
    of a medication order (also known as a Medication Prescription).  Note that
    this information is NOT always sent with the order.  There may be in some
    settings (e.g. hospitals) institutional or system support for completing
    the dispense details in the pharmacy department.
    """

    resource_type: str = Field("MedicationOrderDispenseRequest", const=True)

    expectedSupplyDuration: Duration = Field(
        None,
        alias="expectedSupplyDuration",
        title="Type `Quantity` referencing `Duration` (represented as `dict` in JSON).",
        description="Number of days supply per dispense.",
    )

    medicationCodeableConcept: CodeableConcept = Field(
        None,
        alias="medicationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Product to be supplied.",
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=False,
    )

    medicationReference: Reference = Field(
        None,
        alias="medicationReference",
        title=(
            "Type `Reference` referencing `Medication` (represented as `dict` in JSON)."
        ),
        description="Product to be supplied.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication"],
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=False,
    )

    numberOfRepeatsAllowed: fhirtypes.PositiveInt = Field(
        None,
        alias="numberOfRepeatsAllowed",
        title="Type `int`.",
        description="Number of refills authorized.",
    )

    quantity: Quantity = Field(
        None,
        alias="quantity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Amount of medication to supply per dispense.",
    )

    validityPeriod: Period = Field(
        None,
        alias="validityPeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Time period supply is authorized for.",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "medication": ["medicationCodeableConcept", "medicationReference"],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class MedicationOrderDosageInstruction(backboneelement.BackboneElement):
    """How medication should be taken.

    Indicates how the medication is to be used by the patient.
    """

    resource_type: str = Field("MedicationOrderDosageInstruction", const=True)

    additionalInstructions: CodeableConcept = Field(
        None,
        alias="additionalInstructions",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description='Supplemental instructions - e.g. "with meals".',
    )

    asNeededBoolean: fhirtypes.Boolean = Field(
        None,
        alias="asNeededBoolean",
        title="Type `bool`.",
        description='Take "as needed" (for x).',
        # Choice of Data Types. i.e asNeeded[x]
        one_of_many="asNeeded",
        one_of_many_required=False,
    )

    asNeededCodeableConcept: CodeableConcept = Field(
        None,
        alias="asNeededCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description='Take "as needed" (for x).',
        # Choice of Data Types. i.e asNeeded[x]
        one_of_many="asNeeded",
        one_of_many_required=False,
    )

    doseQuantity: Quantity = Field(
        None,
        alias="doseQuantity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Amount of medication per dose.",
        # Choice of Data Types. i.e dose[x]
        one_of_many="dose",
        one_of_many_required=False,
    )

    doseRange: Range = Field(
        None,
        alias="doseRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Amount of medication per dose.",
        # Choice of Data Types. i.e dose[x]
        one_of_many="dose",
        one_of_many_required=False,
    )

    maxDosePerPeriod: Ratio = Field(
        None,
        alias="maxDosePerPeriod",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Upper limit on medication per unit of time.",
    )

    method: CodeableConcept = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Technique for administering medication.",
    )

    rateRange: Range = Field(
        None,
        alias="rateRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Amount of medication per unit of time.",
        # Choice of Data Types. i.e rate[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    rateRatio: Ratio = Field(
        None,
        alias="rateRatio",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Amount of medication per unit of time.",
        # Choice of Data Types. i.e rate[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    route: CodeableConcept = Field(
        None,
        alias="route",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="How drug should enter body.",
    )

    siteCodeableConcept: CodeableConcept = Field(
        None,
        alias="siteCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Body site to administer to.",
        # Choice of Data Types. i.e site[x]
        one_of_many="site",
        one_of_many_required=False,
    )

    siteReference: Reference = Field(
        None,
        alias="siteReference",
        title=(
            "Type `Reference` referencing `BodySite` (represented as `dict` in JSON)."
        ),
        description="Body site to administer to.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["BodySite"],
        # Choice of Data Types. i.e site[x]
        one_of_many="site",
        one_of_many_required=False,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `str`.",
        description="Dosage instructions expressed as text.",
    )

    timing: Timing = Field(
        None,
        alias="timing",
        title="Type `Timing` (represented as `dict` in JSON).",
        description="When medication should be administered.",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "asNeeded": ["asNeededBoolean", "asNeededCodeableConcept"],
            "dose": ["doseQuantity", "doseRange"],
            "rate": ["rateRange", "rateRatio"],
            "site": ["siteCodeableConcept", "siteReference"],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class MedicationOrderSubstitution(backboneelement.BackboneElement):
    """Any restrictions on medication substitution.

    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen, and in others it does not matter. This block
    explains the prescriber's intent. If nothing is specified substitution may
    be done.
    """

    resource_type: str = Field("MedicationOrderSubstitution", const=True)

    reason: CodeableConcept = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Why should (not) substitution be made.",
    )

    type: CodeableConcept = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="generic | formulary +.",
    )


MedicationOrder.update_forward_refs()
