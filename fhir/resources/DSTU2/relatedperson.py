# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedPerson
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .address import Address
from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .humanname import HumanName
from .identifier import Identifier
from .period import Period
from .reference import Reference


class RelatedPerson(DomainResource):
    """An person that is related to a patient, but who is not a direct target of
    care.

    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """

    resource_type: str = Field("RelatedPerson", const=True)

    address: ListType[Address] = Field(
        None,
        alias="address",
        title="List of `Address` items (represented as `dict` in JSON).",
        description="Address where the related person can be contacted or visited.",
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="Type `Date`",
        description="The date on which the related person was born.",
    )
    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="Type `Code`",
        description="male | female | other | unknown.",
    )

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="A human identifier for this person.",
    )

    name: HumanName = Field(
        None,
        alias="name",
        title="Type `HumanName` (represented as `dict` in JSON).",
        description="A name associated with the person.",
    )

    patient: Reference = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="The patient this person is related to.",
    )

    period: Period = Field(
        None,
        alias="period",
        title="Type `Period`  (represented as `dict` in JSON).",
        description="Period of time that this relationship is considered valid.",
    )

    relationship: CodeableConcept = Field(
        None,
        alias="relationship",
        title="Type `CodeableConcept`  (represented as `dict` in JSON).",
        description="The nature of the relationship.",
    )

    photo: ListType[Attachment] = Field(
        None,
        alias="photo",
        title="List of `Attachment` items (represented as `dict` in JSON).",
        description="Image of the person.",
    )

    telecom: ListType[Attachment] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="A contact detail for the person.",
    )
