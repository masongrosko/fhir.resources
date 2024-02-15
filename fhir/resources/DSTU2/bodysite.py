# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BodySite
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .identifier import Identifier
from .reference import Reference


class BodySite(DomainResource):
    """Specific and identified anatomical location.

    Record details about the anatomical location of a specimen or body part.
    This resource may be used when a coded concept does not provide the
    necessary detail needed for the use case.
    """

    resource_type: str = Field("BodySite", const=True)

    code: CodeableConcept = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Named anatomical location",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Anatomical location description",
    )

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Bodysite identifier",
    )

    image: ListType[Attachment] = Field(
        None,
        alias="image",
        title="List of `Attachment` items (represented as `dict` in JSON)",
        description="Attached images",
    )

    patient: Reference = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who this is about",
    )

    modifier: ListType[CodeableConcept] = Field(
        None,
        alias="modifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Modification to location code",
    )
