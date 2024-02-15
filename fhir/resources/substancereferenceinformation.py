# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator

from . import backboneelement, domainresource, fhirtypes
from .codeableconcept import CodeableConcept
from .identifier import Identifier
from .quantity import Quantity
from .range import Range
from .reference import Reference


class SubstanceReferenceInformation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type: str = Field("SubstanceReferenceInformation", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    gene: typing.List["SubstanceReferenceInformationGene"] = Field(
        None,
        alias="gene",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    geneElement: typing.List["SubstanceReferenceInformationGeneElement"] = Field(
        None,
        alias="geneElement",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    target: typing.List["SubstanceReferenceInformationTarget"] = Field(
        None,
        alias="target",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceReferenceInformation`` according specification,
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
            "comment",
            "gene",
            "geneElement",
            "target",
        ]


class SubstanceReferenceInformationGene(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type: str = Field("SubstanceReferenceInformationGene", const=True)

    gene: CodeableConcept = Field(
        None,
        alias="gene",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    geneSequenceOrigin: CodeableConcept = Field(
        None,
        alias="geneSequenceOrigin",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[Reference] = Field(
        None,
        alias="source",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceReferenceInformationGene`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "geneSequenceOrigin",
            "gene",
            "source",
        ]


class SubstanceReferenceInformationGeneElement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type: str = Field("SubstanceReferenceInformationGeneElement", const=True)

    element: Identifier = Field(
        None,
        alias="element",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[Reference] = Field(
        None,
        alias="source",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    type: CodeableConcept = Field(
        None,
        alias="type",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceReferenceInformationGeneElement`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "element", "source"]


class SubstanceReferenceInformationTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Todo.
    """

    resource_type: str = Field("SubstanceReferenceInformationTarget", const=True)

    amountQuantity: Quantity = Field(
        None,
        alias="amountQuantity",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountRange: Range = Field(
        None,
        alias="amountRange",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )

    amountString: fhirtypes.String = Field(
        None,
        alias="amountString",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e amount[x]
        one_of_many="amount",
        one_of_many_required=False,
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_amountString", title="Extension field for ``amountString``."
    )

    amountType: CodeableConcept = Field(
        None,
        alias="amountType",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    interaction: CodeableConcept = Field(
        None,
        alias="interaction",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    organism: CodeableConcept = Field(
        None,
        alias="organism",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    organismType: CodeableConcept = Field(
        None,
        alias="organismType",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    source: typing.List[Reference] = Field(
        None,
        alias="source",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    target: Identifier = Field(
        None,
        alias="target",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: CodeableConcept = Field(
        None,
        alias="type",
        title="Todo",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceReferenceInformationTarget`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "target",
            "type",
            "interaction",
            "organism",
            "organismType",
            "amountQuantity",
            "amountRange",
            "amountString",
            "amountType",
            "source",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3819(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
            "amount": ["amountQuantity", "amountRange", "amountString"]
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


SubstanceReferenceInformation.update_forward_refs()
