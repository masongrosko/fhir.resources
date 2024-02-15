# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Condition
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .reference import Reference


class Condition(DomainResource):
    """Detailed information about conditions, problems or diagnoses.

    Use to record detailed information about conditions, problems or diagnoses
    recognized by a clinician. There are many uses including: recording a
    diagnosis during an encounter; populating a problem list or a summary
    statement, such as a discharge summary.
    """

    resource_type: str = Field("Condition", const=True)

    abatementBoolean: bool = Field(
        None,
        alias="abatementBoolean",
        title="Type `bool`.",
        description="If/when in resolution/remission.",
        one_of_many="abatement",  # Choice of Data Types. i.e abatement[x]
        one_of_many_required=False,
    )
    abatementDateTime: fhirtypes.DateTime = Field(
        None,
        alias="abatementDateTime",
        title="Type `DateTime`.",
        description="If/when in resolution/remission.",
        one_of_many="abatement",  # Choice of Data Types. i.e abatement[x]
        one_of_many_required=False,
    )

    abatementPeriod: Period = Field(
        None,
        alias="abatementPeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="If/when in resolution/remission.",
        one_of_many="abatement",  # Choice of Data Types. i.e abatement[x]
        one_of_many_required=False,
    )

    abatementQuantity: Quantity = Field(
        None,
        alias="abatementQuantity",
        title="Type `Quantity` referencing `Age` (represented as `dict` in JSON).",
        description="If/when in resolution/remission.",
        one_of_many="abatement",  # Choice of Data Types. i.e abatement[x]
        one_of_many_required=False,
    )

    abatementRange: Range = Field(
        None,
        alias="abatementRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="If/when in resolution/remission.",
        one_of_many="abatement",  # Choice of Data Types. i.e abatement[x]
        one_of_many_required=False,
    )

    abatementString: fhirtypes.String = Field(
        None,
        alias="abatementString",
        title="Type `String`",
        description="If/when in resolution/remission.",
        one_of_many="abatement",  # Choice of Data Types. i.e abatement[x]
        one_of_many_required=False,
    )

    asserter: Reference = Field(
        None,
        alias="asserter",
        title=(
            "Type `Reference` referencing `Practitioner, "
            "Patient` (represented as `dict` in JSON)."
        ),
        description="Person who asserts this condition.",
    )

    bodySite: ListType[CodeableConcept] = Field(
        None,
        alias="bodySite",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Anatomical location, if relevant.",
    )
    category: CodeableConcept = Field(
        None,
        alias="category",
        title="`CodeableConcept` (represented as `dict` in JSON).",
        description="complaint | symptom | finding | diagnosis.",
    )

    clinicalStatus: fhirtypes.Code = Field(
        None,
        alias="clinicalStatus",
        title="Type `Code`.",
        description="active | relapse | remission | resolved.",
    )

    code: CodeableConcept = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Identification of the condition, problem or diagnosis.",
    )
    dateRecorded: fhirtypes.Date = Field(
        None,
        alias="dateRecorded",
        title="Type `Date`.",
        description="When first entered.",
    )

    encounter: Reference = Field(
        None,
        alias="encounter",
        title="Type `Reference` (represented as `dict` in JSON).",
        description="Encounter when condition first asserted.",
    )

    evidence: ListType["ConditionEvidence"] = Field(
        None,
        alias="evidence",
        title="Type `ConditionEvidence` (represented as `dict` in JSON).",
        description="Supporting evidence.",
    )
    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON).",
        description="External Ids for this condition.",
    )

    notes: fhirtypes.String = Field(
        None,
        alias="notes",
        title="Type `String`.",
        description="Additional information about the Condition.",
    )

    onsetDateTime: fhirtypes.DateTime = Field(
        None,
        alias="onsetDateTime",
        title="Type `DateTime`.",
        description="Estimated or actual date,  date-time, or age.",
        one_of_many="onset",  # Choice of Data Types. i.e onset[x]
        one_of_many_required=False,
    )

    onsetPeriod: Period = Field(
        None,
        alias="onsetPeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Estimated or actual date,  date-time, or age.",
        one_of_many="onset",  # Choice of Data Types. i.e onset[x]
        one_of_many_required=False,
    )

    onsetQuantity: Quantity = Field(
        None,
        alias="onsetQuantity",
        title="Type `Quantity` referencing `Age` (represented as `dict` in JSON).",
        description="Estimated or actual date,  date-time, or age.",
        one_of_many="onset",  # Choice of Data Types. i.e onset[x]
        one_of_many_required=False,
    )

    onsetRange: Range = Field(
        None,
        alias="onsetRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Estimated or actual date,  date-time, or age.",
        one_of_many="onset",  # Choice of Data Types. i.e onset[x]
        one_of_many_required=False,
    )

    onsetString: fhirtypes.String = Field(
        None,
        alias="onsetString",
        title="Type `String`",
        description="Estimated or actual date,  date-time, or age.",
        one_of_many="onset",  # Choice of Data Types. i.e onset[x]
        one_of_many_required=False,
    )

    patient: Reference = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="Who has the condition?.",
    )

    severity: CodeableConcept = Field(
        None,
        alias="severity",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Subjective severity of condition.",
    )

    stage: "ConditionStage" = Field(
        None,
        alias="stage",
        title="Type `ConditionStage` (represented as `dict` in JSON).",
        description="Stage/grade, usually assessed formally.",
    )

    verificationStatus: fhirtypes.Code = Field(
        None,
        alias="verificationStatus",
        title="Type `Code`.",
        description=(
            "provisional | differential "
            "| confirmed | refuted | entered-in-error| unknown."
        ),
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
            "onset": [
                "onsetString",
                "onsetRange",
                "onsetDateTime",
                "onsetQuantity",
                "onsetPeriod",
            ],
            "abatement": [
                "abatementDateTime",
                "abatementQuantity",
                "abatementBoolean",
                "abatementPeriod",
                "abatementRange",
                "abatementString",
            ],
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


class ConditionEvidence(BackboneElement):
    """Supporting evidence.

    Supporting Evidence / manifestations that are the basis on which this
    condition is suspected or confirmed.
    """

    resource_type: str = Field("ConditionEvidence", const=True)

    code: CodeableConcept = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Manifestation/symptom.",
    )
    detail: ListType[Reference] = Field(
        None,
        alias="detail",
        title=(
            "List of `Reference` items referencing "
            "`Resource` (represented as `dict` in JSON)."
        ),
        description="Supporting information found elsewhere.",
    )


class ConditionStage(BackboneElement):
    """Stage/grade, usually assessed formally.

    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """

    resource_type: str = Field("ConditionStage", const=True)
    summary: CodeableConcept = Field(
        None,
        alias="summary",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Simple summary (disease specific).",
    )
    assessment: ListType[Reference] = Field(
        None,
        alias="assessment",
        title=(
            "List of `Reference` items referencing `ClinicalImpression, "
            "DiagnosticReport, Observation` (represented as `dict` in JSON)."
        ),
        description="Formal record of assessment.",
    )


Condition.update_forward_refs()
