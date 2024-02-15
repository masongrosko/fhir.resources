# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DomainResource
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from .extension import Extension
from .narrative import Narrative
from .resource import Resource


class DomainResource(Resource):
    """A resource with narrative, extensions, and contained resources.

    A resource that includes narrative, extensions, and contained resources.
    """

    resource_type: str = Field("DomainResource", const=True)

    contained: ListType[Resource] = Field(
        None,
        alias="contained",
        title="List of `Resource` items (represented as `dict` in JSON)",
        description="Contained, inline Resources",
    )

    extension: ListType[Extension] = Field(
        None,
        alias="extension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Additional Content defined by implementations",
    )

    modifierExtension: ListType[Extension] = Field(
        None,
        alias="modifierExtension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Extensions that cannot be ignored",
    )

    text: Narrative = Field(
        None,
        alias="text",
        title="Type `Narrative` (represented as `dict` in JSON)",
        description="Text summary of the resource, for human interpretation",
    )
