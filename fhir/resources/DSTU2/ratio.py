# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Ratio
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic.v1 import Field

from .element import Element
from .quantity import Quantity


class Ratio(Element):
    """A ratio of two Quantity values - a numerator and a denominator.

    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """

    resource_type: str = Field("Ratio", const=True)

    denominator: Quantity = Field(
        None,
        alias="denominator",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Denominator value",
    )

    numerator: Quantity = Field(
        None,
        alias="numerator",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Numerator value",
    )
