# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/substance.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio
from .reference import Reference


class Substance(domainresource.DomainResource):
    """A homogeneous material with a definite composition
    A homogeneous material with a definite composition.
    """

    resource_type: str = Field("Substance", const=True)

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="List of Unique identifier (represented as 'dict' in JSON)",
        description="Unique identifier for the substance",
        element_property=True,
    )

    category: ListType[CodeableConcept] = Field(
        None,
        alias="category",
        title="List of Type `CodeableConcept` (represented as `dict` in JSON).",
        description="What class/type of substance this is",
        element_property=True,
    )

    code: CodeableConcept = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="What substance this is",
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Textual description of the substance, comments",
        element_property=True,
    )

    instance: ListType["SubstanceInstance"] = Field(
        None,
        alias="instance",
        title="List of Type `SubstanceInstance` (represented as `dict` in JSON).",
        description="If this describes a specific package/container of the substance",
        element_property=True,
    )

    ingredient: ListType["SubstanceIngredient"] = Field(
        None,
        alias="ingredient",
        title="List of Type `SubstanceIngredient` (represented as `dict` in JSON).",
        description="Composition information about the substance",
        element_property=True,
    )


class SubstanceInstance(BackboneElement):
    """If this describes a specific package/container of the substance

    If this describes a specific package/container of the substance.
    """

    resource_type: str = Field("SubstanceInstance", const=True)

    identifier: Identifier = Field(
        None,
        alias="identifier",
        title="Identifier of the package/container",
        description=(
            "Identifier associated with the package/container"
            " (usually a label affixed directly)"
        ),
        element_property=True,
    )

    expiry: fhirtypes.DateTime = Field(
        None,
        alias="expiry",
        title="When no longer valid to use",
        description=(
            "When the substance is no longer valid to use. "
            "For some substances, a single arbitrary date is used for expiry."
        ),
        element_property=True,
    )

    quantity: Quantity = Field(
        None,
        alias="quantity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Amount of substance in the package",
        element_property=True,
    )


class SubstanceIngredient(BackboneElement):
    """Composition information about the substance


    A substance can be composed of other substances.
    """

    resource_type: str = Field("SubstanceIngredient", const=True)

    quantity: Ratio = Field(
        None,
        alias="quantity",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Optional amount (concentration)",
        element_property=True,
    )

    substance: Reference = Field(
        None,
        alias="substance",
        title=(
            "`Reference` items referencing `Substance` (represented as `dict` in"
            " JSON)"
        ),
        description="A component of the substance",
        enum_reference_types=["Substance"],
        element_property=True,
    )


Substance.update_forward_refs()
