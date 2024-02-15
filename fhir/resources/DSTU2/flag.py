# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Flag
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .identifier import Identifier
from .period import Period
from .reference import Reference


class Flag(DomainResource):
    """Key information to flag to healthcare providers.

    Prospective warnings of potential issues when providing care to the
    patient.
    """

    resource_type: str = Field("Flag", const=True)

    author: Reference = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Device, Organization, Patient, "
            "Practitioner` (represented as `dict` in JSON)"
        ),
        description="Flag creator",
    )

    category: CodeableConcept = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Clinical, administrative, etc.",
    )

    code: CodeableConcept = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Coded or textual message to display to user",
    )

    encounter: Reference = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Alert relevant during encounter",
    )

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier",
    )

    period: Period = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period when flag is active",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | inactive | entered-in-error",
    )

    subject: Reference = Field(
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Location, Group, Organization, "
            "Practitioner, PlanDefinition, Medication, Procedure` (represented as "
            "`dict` in JSON)"
        ),
        description="Who/What is flag about?",
    )
