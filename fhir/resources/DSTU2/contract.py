# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Contract
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity
from .reference import Reference


class Contract(DomainResource):
    """Contract.

    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    resource_type: str = Field("Contract", const=True)

    action: ListType[CodeableConcept] = Field(
        None,
        alias="action",
        title="Action stipulated by this Contract",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    actionReason: ListType[CodeableConcept] = Field(
        None,
        alias="actionReason",
        title="Contract Action Reason.",
        description="List of `CodeableConcept` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    actor: ListType["ContractActor"] = Field(
        None,
        alias="actor",
        title="Contract Actor.",
        description="List of `ContractActor` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )
    authority: ListType[Reference] = Field(
        None,
        alias="authority",
        title="Authority under which this Contract has standing.",
        description="List of `Reference` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    domain: ListType[Reference] = Field(
        None,
        alias="domain",
        title="Domain in which this Contract applies.",
        description="List of `Reference` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    friendly: ListType["ContractFriendly"] = Field(
        None,
        alias="friendly",
        title="Contractfriendly  applies.",
        description="List of `ContractFriendly` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    legal: ListType["ContractLegal"] = Field(
        None,
        alias="legal",
        title="Contract Legal Language.",
        description="List of `ContractLegal` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    rule: ListType["ContractRule"] = Field(
        None,
        alias="rule",
        title="Computable Contract Language.",
        description="List of `ContractRule` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    signer: ListType["ContractSigner"] = Field(
        None,
        alias="signer",
        title="Contract Signer.",
        description="List of `ContractSigner` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    type: ListType[CodeableConcept] = Field(
        None,
        alias="type",
        title="Contract Type.",
        description="List of `CodeableConcept` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    subType: ListType[CodeableConcept] = Field(
        None,
        alias="subType",
        title="Contract Subtype.",
        description="List of `CodeableConcept` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    subject: ListType[Reference] = Field(
        None,
        alias="subject",
        title="Subject of this Contract.",
        description=(
            "List of `Reference` items referencing `Resource` "
            "(represented as `dict` in JSON)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    term: ListType["ContractTerm"] = Field(
        None,
        alias="term",
        title="Contract Term List.",
        description="List of `ContractTerm` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    valuedItem: ListType["ContractValuedItem"] = Field(
        None,
        alias="valuedItem",
        title="Contract Valued Item.",
        description="List of `ContractValuedItem` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    applies: Period = Field(
        None,
        alias="applies",
        title="Effective time.",
        description="`Period` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
    )

    bindingAttachment: Attachment = Field(
        None,
        alias="bindingAttachment",
        title="Binding Contract.",
        description="`Attachment` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e binding[x]
        one_of_many="binding",
        one_of_many_required=False,
    )

    bindingReference: Reference = Field(
        None,
        alias="bindingReference",
        title="Binding Contract.",
        description=(
            "Type `Reference` referencing `Composition, DocumentReference,"
            " QuestionnaireResponse` (represented as `dict` in JSON)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e binding[x]
        one_of_many="binding",
        one_of_many_required=False,
    )

    identifier: Identifier = Field(
        None,
        alias="identifier",
        title="Contract identifier.",
        description="`Identifier` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
    )

    issued: fhirtypes.DateTime = Field(
        None,
        alias="issued",
        title="Contract identifier.",
        description="`DateTime",
        # if property is element of this resource.
        element_property=True,
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
        one_of_many_fields = {"binding": ["bindingAttachment", "bindingReference"]}
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


class ContractActor(BackboneElement):
    """Contract Actor.

    List of Contract actors.
    """

    resource_type: str = Field("ContractActor", const=True)

    entity: Reference = Field(
        ...,
        alias="entity",
        title="Contract Actor Type.",
        description=(
            "Type `Reference` referencing `Contract, Device,"
            " Group, Location, Organization, Patient, Practitioner, "
            "RelatedPerson, Substance` (represented as `dict` in JSON)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    role: ListType[CodeableConcept] = Field(
        None,
        alias="role",
        title="Contract  Actor Role.",
        description="List of `CodeableConcept` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )


class ContractFriendly(BackboneElement):
    """Contract Friendly Language.

    The "patient friendly language" versionof the Contract in whole or in
    parts. "Patient friendly language" means the representation of the Contract
    and Contract Provisions in a manner that is readily accessible and
    understandable by a layperson in accordance with best practices for
    communication styles that ensure that those agreeing to or signing the
    Contract understand the roles, actions, obligations, responsibilities, and
    implication of the agreement.
    """

    resource_type: str = Field("ContractFriendly", const=True)

    contentAttachment: Attachment = Field(
        None,
        alias="contentAttachment",
        title="Easily comprehended representation of this Contract.",
        description="`Attachment` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e binding[x]
        one_of_many="content",
        one_of_many_required=True,
    )

    contentReference: Reference = Field(
        None,
        alias="contentReference",
        title="Easily comprehended representation of this Contract.",
        description=(
            "Type `Reference` referencing `Composition, DocumentReference,"
            " QuestionnaireResponse` (represented as `dict` in JSON)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
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
        one_of_many_fields = {"content": ["contentAttachment", "contentReference"]}
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


class ContractLegal(BackboneElement):
    """Contract Legal Language.

    List of Legal expressions or representations of this Contract.
    """

    resource_type: str = Field("ContractLegal", const=True)

    contentAttachment: Attachment = Field(
        None,
        alias="contentAttachment",
        title="Contract Legal Text.",
        description="`Attachment` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e binding[x]
        one_of_many="content",
        one_of_many_required=True,
    )

    contentReference: Reference = Field(
        None,
        alias="contentReference",
        title="Contract Legal Text.",
        description=(
            "Type `Reference` referencing `Composition, "
            "DocumentReference, QuestionnaireResponse` (represented as `dict` in JSON)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
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
        one_of_many_fields = {"content": ["contentAttachment", "contentReference"]}
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


class ContractRule(BackboneElement):
    """Computable Contract Language.

    List of Computable Policy Rule Language Representations of this Contract.
    """

    resource_type: str = Field("ContractRule", const=True)

    contentAttachment: Attachment = Field(
        None,
        alias="contentAttachment",
        title="Computable Contract Rules.",
        description="`Attachment` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e binding[x]
        one_of_many="content",
        one_of_many_required=True,
    )

    contentReference: Reference = Field(
        None,
        alias="contentReference",
        title="Computable Contract Rules.",
        description=(
            "Type `Reference` referencing DocumentReference "
            "(represented as `dict` in JSON)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
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
        one_of_many_fields = {"content": ["contentAttachment", "contentReference"]}
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


class ContractSigner(BackboneElement):
    """Contract Signer.

    Party signing this Contract.
    """

    resource_type: str = Field("ContractSigner", const=True)

    party: Reference = Field(
        ...,
        alias="party",
        title="Contract Signatory Party.",
        description=(
            "Type `Reference` referencing `Organization, "
            "Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    signature: fhirtypes.String = Field(
        ...,
        alias="signature",
        title="Contract Documentation Signature.",
        description="Type `String`.",
        # if property is element of this resource.
        element_property=True,
    )
    type: Coding = Field(
        ...,
        alias="type",
        title="Contract Signer Type.",
        description="Type `Coding` (represented as `dict` in JSON)..",
        # if property is element of this resource.
        element_property=True,
    )


class ContractTerm(BackboneElement):
    """Contract Term List.

    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """

    resource_type: str = Field("ContractTerm", const=True)

    action: ListType[CodeableConcept] = Field(
        None,
        alias="action",
        title="Contract Term Action.",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    actionReason: ListType[CodeableConcept] = Field(
        None,
        alias="actionReason",
        title="Contract Term Action Reason.",
        description="List of `CodeableConcept` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    actor: ListType["ContractTermActor"] = Field(
        None,
        alias="actor",
        title="Contract Term Actor List.",
        description="List of `ContractTermActor` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    applies: Period = Field(
        None,
        alias="applies",
        title="Contract Term Effective Time.",
        description="`Period` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
    )

    group: ListType["ContractTerm"] = Field(
        None,
        alias="group",
        title="Nested Contract Term Group.",
        description="List of `ContractTerm` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    type: CodeableConcept = Field(
        None,
        alias="type",
        title="Contract Term Type.",
        description="List of `CodeableConcept` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    subType: CodeableConcept = Field(
        None,
        alias="subType",
        title="Contract Term Subtype.",
        description="`CodeableConcept` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    subject: Reference = Field(
        None,
        alias="subject",
        title="Subject of this Contract Term.",
        description="`Reference` referencing `Resource` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: Identifier = Field(
        None,
        alias="identifier",
        title="Contract Term identifier.",
        description="`Identifier` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )
    issued: fhirtypes.DateTime = Field(
        None,
        alias="issued",
        title="Contract Term Issue Date Time.",
        description="`DateTime`.",
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Human readable Contract term text.",
        description="`String`.",
        # if property is element of this resource.
        element_property=True,
    )

    valuedItem: ListType["ContractTermValuedItem"] = Field(
        None,
        alias="valuedItem",
        title="Nested Contract Term Group.",
        description="List of `ContractTermValuedItem` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )


class ContractTermActor(BackboneElement):
    """Contract Term Actor List.

    List of actors participating in this Contract Provision.
    """

    resource_type: str = Field("ContractTermActor", const=True)

    entity: Reference = Field(
        ...,
        alias="entity",
        title="Contract Term Actor.",
        description=(
            "Type `Reference` referencing `Contract, Device, Group, Location, "
            "Organization, Patient, Practitioner, RelatedPerson, Substance` "
            "(represented as `dict` in JSON)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    role: ListType[CodeableConcept] = Field(
        None,
        alias="role",
        title="Contract Term Actor Role.",
        description="List of `CodeableConcept` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )


class ContractTermValuedItem(BackboneElement):
    """Contract Term Valued Item.

    Contract Provision Valued Item List.
    """

    resource_type: str = Field("ContractTermValuedItem", const=True)

    effectiveTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveTime",
        title="Contract Term Valued Item Effective Tiem.",
        description="Type `DateTime`.",
        # if property is element of this resource.
        element_property=True,
    )

    entityCodeableConcept: CodeableConcept = Field(
        None,
        alias="entityCodeableConcept",
        title="Contract Term Valued Item Type.",
        description="Type `CodeableConcept` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e entity[x]
        one_of_many="entity",
        one_of_many_required=False,
    )

    entityReference: Reference = Field(
        None,
        alias="entityReference",
        title="Contract Term Valued Item Type.",
        description="Type `Reference` referencing `Resource` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e entity[x]
        one_of_many="entity",
        one_of_many_required=False,
    )

    identifier: Identifier = Field(
        None,
        alias="identifier",
        title="Contract Term Valued Item Identifier.",
        description="Type `Identifier` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    net: Money = Field(
        None,
        alias="net",
        title="Total Contract Term Valued Item Value.",
        description="Type `Money` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    quantity: Quantity = Field(
        None,
        alias="quantity",
        title="Contract Term Valued Item Count.",
        description="Type `Quantity` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    unitPrice: Money = Field(
        None,
        alias="quantity",
        title="Contract Term Valued Item fee, charge, or cost.",
        description="Type `Money` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Contract Term Valued Item Price Scaling Factor.",
        description="Type `Decimal`.",
        # if property is element of this resource.
        element_property=True,
    )

    points: fhirtypes.Decimal = Field(
        None,
        alias="points",
        title="Contract Term Valued Item Difficulty Scaling Factor.",
        description="Type `Decimal`.",
        # if property is element of this resource.
        element_property=True,
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
        one_of_many_fields = {"entity": ["entityCodeableConcept", "entityReference"]}
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


class ContractValuedItem(BackboneElement):
    """Contract Valued Item.

    Contract Valued Item List.
    """

    resource_type: str = Field("ContractValuedItem", const=True)

    effectiveTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveTime",
        title="Contract Valued Item Effective Tiem.",
        description="Type `DateTime`.",
        # if property is element of this resource.
        element_property=True,
    )

    entityCodeableConcept: CodeableConcept = Field(
        None,
        alias="entityCodeableConcept",
        title="Contract Valued Item Type.",
        description="Type `CodeableConcept` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e entity[x]
        one_of_many="entity",
        one_of_many_required=False,
    )

    entityReference: Reference = Field(
        None,
        alias="entityReference",
        title="Contract Valued Item Type.",
        description="Type `Reference` referencing `Resource` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e entity[x]
        one_of_many="entity",
        one_of_many_required=False,
    )

    identifier: Identifier = Field(
        None,
        alias="identifier",
        title="Contract Valued Item Identifier.",
        description="Type `Identifier` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    net: Money = Field(
        None,
        alias="net",
        title="Total Contract Valued Item Value.",
        description="Type `Money` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    quantity: Quantity = Field(
        None,
        alias="quantity",
        title="Contract Valued Item Count.",
        description="Type `Quantity` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    unitPrice: Money = Field(
        None,
        alias="quantity",
        title="Contract Valued Item fee, charge, or cost.",
        description="Type `Money` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Contract Valued Item Price Scaling Factor.",
        description="Type `Decimal`.",
        # if property is element of this resource.
        element_property=True,
    )

    points: fhirtypes.Decimal = Field(
        None,
        alias="points",
        title="Contract Valued Item Difficulty Scaling Factor.",
        description="Type `Decimal`.",
        # if property is element of this resource.
        element_property=True,
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
        one_of_many_fields = {"entity": ["entityCodeableConcept", "entityReference"]}
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


Contract.update_forward_refs()
ContractTerm.update_forward_refs()
