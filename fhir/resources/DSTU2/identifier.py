# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Identifier
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""

from pydantic.v1 import Field

from . import fhirtypes
from .codeableconcept import CodeableConcept
from .element import Element
from .period import Period
from .reference import Reference


class Identifier(Element):
    """An identifier intended for computation.

    A technical identifier - identifies some entity uniquely and unambiguously.
    """

    resource_type: str = Field("Identifier", const=True)

    assigner: Reference = Field(
        None,
        alias="assigner",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization that issued id (may be just text)",
    )

    period: Period = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period when id is/was valid for use",
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="The namespace for the identifier value",
    )

    type: CodeableConcept = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Description of identifier",
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="usual | official | temp | secondary (If known)",
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="The value that is unique",
    )
