# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coverage
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""

from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .coding import Coding
from .domainresource import DomainResource
from .identifier import Identifier
from .period import Period
from .reference import Reference


class Coverage(DomainResource):
    """Insurance or medical plan.

    Financial instrument which may be used to pay for or reimburse health care
    products and services.
    """

    resource_type: str = Field("Coverage", const=True)

    bin: Identifier = Field(
        None,
        alias="bin",
        title="BIN Number.",
        description="`Identifier` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
    )
    contract: ListType[Reference] = Field(
        None,
        alias="contract",
        title="BIN Number.",
        description=(
            "List of `Reference` items referencing `Contract`"
            " (represented as `dict` in JSON)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    group: fhirtypes.String = Field(
        None,
        alias="group",
        title="An identifier for the group.",
        description="String",
        # if property is element of this resource.
        element_property=True,
    )

    dependent: fhirtypes.PositiveInt = Field(
        None,
        alias="dependent",
        title="The dependent number.",
        description="PositiveInt",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="The primary coverage ID.",
        description="List of `Identifier` items (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    issuer: Reference = Field(
        None,
        alias="issuer",
        title="An identifier for the plan issuer.",
        description=(
            "Type `Reference` referencing `Organization` "
            "(represented as `dict` in JSON)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    network: Identifier = Field(
        None,
        alias="network",
        title="Insurer network.",
        description="`Identifier` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
    )
    period: Period = Field(
        None,
        alias="period",
        title="Coverage start and end dates.",
        description="`Period` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
    )
    plan: fhirtypes.String = Field(
        None,
        alias="plan",
        title="An identifier for the plan.",
        description="String",
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="The plan instance or sequence counter.",
        description="PositiveInt",
        # if property is element of this resource.
        element_property=True,
    )

    subPlan: fhirtypes.String = Field(
        None,
        alias="subPlan",
        title="An identifier for the subsection of the plan.",
        description="`Identifier` represented as `string`.",
        # if property is element of this resource.
        element_property=True,
    )

    subscriberId: Identifier = Field(
        None,
        alias="subscriberId",
        title="Subscriber ID.",
        description="`Identifier` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
    )

    type: Coding = Field(
        None,
        alias="type",
        title="Type of coverage.",
        description="`Coding` represented as `dict` in JSON.",
        # if property is element of this resource.
        element_property=True,
    )

    subscriber: Reference = Field(
        None,
        alias="subscriber",
        title="Plan holder information.",
        description="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )
