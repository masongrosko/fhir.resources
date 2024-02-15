# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Person
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .humanname import HumanName
from .identifier import Identifier
from .reference import Reference


class Person(DomainResource):
    """A generic person record.

    Demographics and administrative information about a person independent of a
    specific health-related context.
    """

    resource_type: str = Field("Person", const=True)

    active: fhirtypes.Boolean = Field(
        None,
        alias="active",
        title="Type `Boolean`",
        description="This person's record is in active use.",
    )

    purpose: CodeableConcept = Field(
        None,
        alias="purpose",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="The type of contact.",
    )
    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="Type `Date`.",
        description="The date on which the person was born.",
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="Type `Code`.",
        description="male | female | other | unknown.",
    )

    address: ListType[Address] = Field(
        None,
        alias="address",
        title="List of `Address` items (represented as `dict` in JSON).",
        description="One or more addresses for the person.",
    )

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="A human identifier for this person.",
    )

    link: ListType["PersonLink"] = Field(
        None,
        alias="link",
        title="List of `PersonLink` items (represented as `dict` in JSON).",
        description="Link to a resource that concerns the same actual person.",
    )

    managingOrganization: Reference = Field(
        None,
        alias="managingOrganization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="The organization that is the custodian of the person record.",
    )

    name: ListType[HumanName] = Field(
        None,
        alias="name",
        title="List of `HumanName` items (represented as `dict` in JSON).",
        description="A name associated with the person.",
    )

    telecom: ListType[ContactPoint] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="A contact detail for the person.",
    )

    photo: Attachment = Field(
        None,
        alias="photo",
        title="Type `Attachment` (represented as `dict` in JSON).",
        description="Image of the person.",
    )


class PersonLink(BackboneElement):
    """Link to a resource that concerns the same actual person."""

    resource_type: str = Field("PersonLink", const=True)

    assurance: fhirtypes.Code = Field(
        None,
        alias="assurance",
        title="Type `Code`.",
        description="level1 | level2 | level3 | level4.",
    )
    target: Reference = Field(
        None,
        alias="target",
        title=(
            "Type `Reference` referencing `Patient, "
            "Practitioner, RelatedPerson, Person` (represented as `dict` in JSON)."
        ),
        description="The resource to which this actual person is associated.",
    )


Person.update_forward_refs()
