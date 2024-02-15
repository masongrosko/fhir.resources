# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Substance
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes
from .codeableconcept import CodeableConcept
from .codeablereference import CodeableReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio
from .reference import Reference


class Substance(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A homogeneous material with a definite composition.
    """

    resource_type: str = Field("Substance", const=True)

    category: typing.List[CodeableConcept] = Field(
        None,
        alias="category",
        title="What class/type of substance this is",
        description=(
            "A code that classifies the general type of substance.  This is used  "
            "for searching, sorting and display purposes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: CodeableReference = Field(
        ...,
        alias="code",
        title="What substance this is",
        description="A code (or set of codes) that identify this substance.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition"],
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Textual description of the substance, comments",
        description=(
            "A description of the substance - its appearance, handling "
            "requirements, and other usage notes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expiry: fhirtypes.DateTime = Field(
        None,
        alias="expiry",
        title="When no longer valid to use",
        description=(
            "When the substance is no longer valid to use. For some substances, a "
            "single arbitrary date is used for expiry."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expiry__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expiry", title="Extension field for ``expiry``."
    )

    identifier: typing.List[Identifier] = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description=(
            "Unique identifier for the substance. For an instance, an identifier "
            "associated with the package/container (usually a label affixed "
            "directly)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    ingredient: typing.List["SubstanceIngredient"] = Field(
        None,
        alias="ingredient",
        title="Composition information about the substance",
        description="A substance can be composed of other substances.",
        # if property is element of this resource.
        element_property=True,
    )

    instance: bool = Field(
        None,
        alias="instance",
        title="Is this an instance of a substance or a kind of one",
        description=(
            "A boolean to indicate if this an instance of a substance or a kind of "
            "one (a definition)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    instance__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_instance", title="Extension field for ``instance``."
    )

    quantity: Quantity = Field(
        None,
        alias="quantity",
        title="Amount of substance in the package",
        description="The amount of the substance.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description="A code to indicate if the substance is actively used.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "inactive", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Substance`` according specification,
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
            "instance",
            "status",
            "category",
            "code",
            "description",
            "expiry",
            "quantity",
            "ingredient",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1120(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("instance", "instance__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class SubstanceIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Composition information about the substance.
    A substance can be composed of other substances.
    """

    resource_type: str = Field("SubstanceIngredient", const=True)

    quantity: Ratio = Field(
        None,
        alias="quantity",
        title="Optional amount (concentration)",
        description="The amount of the ingredient in the substance - a concentration ratio.",
        # if property is element of this resource.
        element_property=True,
    )

    substanceCodeableConcept: CodeableConcept = Field(
        None,
        alias="substanceCodeableConcept",
        title="A component of the substance",
        description="Another substance that is a component of this substance.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e substance[x]
        one_of_many="substance",
        one_of_many_required=True,
    )

    substanceReference: Reference = Field(
        None,
        alias="substanceReference",
        title="A component of the substance",
        description="Another substance that is a component of this substance.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e substance[x]
        one_of_many="substance",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceIngredient`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "quantity",
            "substanceCodeableConcept",
            "substanceReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2168(
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
            "substance": ["substanceCodeableConcept", "substanceReference"]
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


Substance.update_forward_refs()
