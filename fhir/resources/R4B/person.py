# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Person
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes
from .address import Address
from .attachment import Attachment
from .contactpoint import ContactPoint
from .humanname import HumanName
from .identifier import Identifier
from .reference import Reference


class Person(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A generic person record.
    Demographics and administrative information about a person independent of a
    specific health-related context.
    """

    resource_type: str = Field("Person", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="This person's record is in active use",
        description="Whether this person's record is in active use.",
        # if property is element of this resource.
        element_property=True,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    address: typing.List[Address] = Field(
        None,
        alias="address",
        title="One or more addresses for the person",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="The date on which the person was born",
        description="The birth date for the person.",
        # if property is element of this resource.
        element_property=True,
    )
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_birthDate", title="Extension field for ``birthDate``."
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="male | female | other | unknown",
        description="Administrative Gender.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["male", "female", "other", "unknown"],
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_gender", title="Extension field for ``gender``."
    )

    identifier: typing.List[Identifier] = Field(
        None,
        alias="identifier",
        title="A human identifier for this person",
        description="Identifier for a person within a particular scope.",
        # if property is element of this resource.
        element_property=True,
    )

    link: typing.List["PersonLink"] = Field(
        None,
        alias="link",
        title="Link to a resource that concerns the same actual person",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    managingOrganization: Reference = Field(
        None,
        alias="managingOrganization",
        title="The organization that is the custodian of the person record",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    name: typing.List[HumanName] = Field(
        None,
        alias="name",
        title="A name associated with the person",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    photo: Attachment = Field(
        None,
        alias="photo",
        title="Image of the person",
        description=(
            "An image that can be displayed as a thumbnail of the person to enhance"
            " the identification of the individual."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    telecom: typing.List[ContactPoint] = Field(
        None,
        alias="telecom",
        title="A contact detail for the person",
        description=(
            "A contact detail for the person, e.g. a telephone number or an email "
            "address."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Person`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "name",
            "telecom",
            "gender",
            "birthDate",
            "address",
            "photo",
            "managingOrganization",
            "active",
            "link",
        ]


class PersonLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Link to a resource that concerns the same actual person.
    """

    resource_type: str = Field("PersonLink", const=True)

    assurance: fhirtypes.Code = Field(
        None,
        alias="assurance",
        title="level1 | level2 | level3 | level4",
        description=(
            "Level of assurance that this link is associated with the target "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["level1", "level2", "level3", "level4"],
    )
    assurance__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_assurance", title="Extension field for ``assurance``."
    )

    target: Reference = Field(
        ...,
        alias="target",
        title="The resource to which this actual person is associated",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner", "RelatedPerson", "Person"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PersonLink`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "target", "assurance"]


Person.update_forward_refs()
