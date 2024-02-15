# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Media
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


class Media(DomainResource):
    """A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """

    resource_type: str = Field("Media", const=True)

    content: Attachment = Field(
        ...,
        alias="content",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Actual Media - reference or data",
    )

    deviceName: fhirtypes.String = Field(
        None,
        alias="deviceName",
        title=("Type str"),
        description="Observing Device Name",
    )

    duration: fhirtypes.UnsignedInt = Field(
        None,
        alias="duration",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Length in seconds (audio / video)",
    )

    frames: fhirtypes.PositiveInt = Field(
        None,
        alias="frames",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Number of frames if \u003e 1 (photo)",
    )

    height: fhirtypes.PositiveInt = Field(
        None,
        alias="height",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Height of the image in pixels (photo/video)",
    )

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Identifier(s) for the image",
    )

    operator: Reference = Field(
        None,
        alias="operator",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="The person who generated the image",
    )

    subject: Reference = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, Group, Device, "
            "Specimen` (represented as `dict` in JSON)"
        ),
        description="Who/What this Media is a record of",
    )

    subtype: CodeableConcept = Field(
        None,
        alias="subtype",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of acquisition equipment/process",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="photo | video | audio",
    )

    view: CodeableConcept = Field(
        None,
        alias="view",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Imaging view, e.g. Lateral or Antero-posterior",
    )

    width: fhirtypes.PositiveInt = Field(
        None,
        alias="width",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Width of the image in pixels (photo/video)",
    )
