# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Range
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic.v1 import Field

from .element import Element
from .quantity import Quantity


class Range(Element):
    """Set of values bounded by low and high.

    A set of ordered Quantities defined by a low and high limit.
    """

    resource_type: str = Field("Range", const=True)

    high: Quantity = Field(
        None,
        alias="high",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="High limit",
    )

    low: Quantity = Field(
        None,
        alias="low",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Low limit",
    )
