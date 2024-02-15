# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AuditEvent
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .identifier import Identifier
from .reference import Reference


class AuditEvent(DomainResource):
    """Event record kept for security purposes.

    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    resource_type: str = Field("AuditEvent", const=True)

    event: "AuditEventEvent" = Field(
        ...,
        alias="event",
        title="Type `AuditEventEvent` (represented as `dict` in JSON). ",
        description="A What was done.",
    )
    source: "AuditEventSource" = Field(
        ...,
        alias="source",
        title="Type `AuditEventSource` (represented as `dict` in JSON)",
        description="Audit Event Reporter",
    )

    object: ListType["AuditEventObject"] = Field(
        None,
        alias="entity",
        title="List of `AuditEventObject` items (represented as `dict` in JSON).",
        description="Specific instances of data or objects that have been accessed.",
    )

    participant: ListType["AuditEventParticipant"] = Field(
        None,
        alias="entity",
        title="List of `AuditEventParticipant` items (represented as `dict` in JSON).",
        description="A person, a hardware device or software process.",
    )


class AuditEventEvent(BackboneElement):
    """What was done.

    Identifies the name, action type, time, and disposition of the audited
    event.
    """

    resource_type: str = Field("AuditEventEvent", const=True)

    action: fhirtypes.Code = Field(
        None,
        alias="action",
        title="Type `str`.",
        description="Type of action performed during the event.",
    )
    dateTime: fhirtypes.Instant = Field(
        ...,
        alias="dateTime",
        title="Type `Instant` (represented as `str` in JSON).",
        description="Time when the event occurred on source.",
    )

    outcome: fhirtypes.Code = Field(
        None,
        alias="outcome",
        title="Type `str`.",
        description="Whether the event succeeded or failed.",
    )

    outcomeDesc: fhirtypes.String = Field(
        None,
        alias="outcomeDesc",
        title="Type `str`.",
        description="Description of the event outcome.",
    )

    purposeOfEvent: ListType[Coding] = Field(
        None,
        alias="purposeOfEvent",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="The purposeOfUse of the event.",
    )

    subtype: ListType[Coding] = Field(
        None,
        alias="subtype",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="More specific type/id for the event.",
    )

    type: Coding = Field(
        ...,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Type/identifier of event.",
    )


class AuditEventObject(BackboneElement):
    """Specific instances of data or objects that have been accessed."""

    resource_type: str = Field("AuditEventObject", const=True)

    description: fhirtypes.String = Field(
        None, alias="description", title="Type `str`.", description="Descriptive text."
    )

    detail: ListType["AuditEventObjectDetail"] = Field(
        None,
        alias="detail",
        title=(
            "List of `AuditEventObjectDetail` items " "(represented as `dict` in JSON)."
        ),
        description="Additional Information about the Object.",
    )

    identifier: Identifier = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON).",
        description="Specific instance of object (e.g. versioned).",
    )

    lifecycle: Coding = Field(
        None,
        alias="lifecycle",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Life-cycle stage for the object.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `str`.",
        description="Instance-specific descriptor for Object.",
    )

    query: fhirtypes.Base64Binary = Field(
        None, alias="query", title="Type `str`.", description="Actual query for object."
    )

    reference: Reference = Field(
        None,
        alias="reference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON).",
        description="Specific instance of resource (e.g. versioned).",
    )

    role: Coding = Field(
        None,
        alias="role",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="What role the Object played.",
    )

    securityLabel: ListType[Coding] = Field(
        None,
        alias="securityLabel",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Security labels applied to the object.",
    )

    type: Coding = Field(
        None,
        alias="type",
        title="Type of object involved.",
        description="Type `Coding` (represented as `dict` in JSON).",
    )


class AuditEventObjectDetail(BackboneElement):
    """Additional Information about the Object."""

    resource_type: str = Field("AuditEventObjectDetail", const=True)

    type: fhirtypes.String = Field(
        ..., alias="type", title="Type `str`.", description="Name of the property."
    )
    value: fhirtypes.Base64Binary = Field(
        ..., alias="value", title="Type `str`.", description="Property value."
    )


class AuditEventParticipant(BackboneElement):
    """A person, a hardware device or software process."""

    resource_type: str = Field("AuditEventParticipant", const=True)

    altId: fhirtypes.String = Field(
        None,
        alias="altId",
        title="Type `str`.",
        description="Alternative User id e.g. authentication.",
    )

    location: Reference = Field(
        None,
        alias="location",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON).",
        description="Where.",
    )
    media: Coding = Field(
        None,
        alias="media",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Type of media.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `str`.",
        description="Human-meaningful name for the user.",
    )

    network: "AuditEventParticipantNetwork" = Field(
        None,
        alias="network",
        title="Type `AuditEventParticipantNetwork` (represented as `dict` in JSON).",
        description="Logical network location for application activity.",
    )

    policy: ListType[fhirtypes.Uri] = Field(
        None,
        alias="policy",
        title="List of `str` items.",
        description="Policy that authorized event.",
    )

    purposeOfUse: ListType[Coding] = Field(
        None,
        alias="purposeOfUse",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Reason given for this user.",
    )

    reference: Reference = Field(
        None,
        alias="reference",
        title=(
            "Type `Reference` referencing `Practitioner, "
            "Organization, Device, Patient, RelatedPerson` "
            "(represented as `dict` in JSON)."
        ),
        description="Direct reference to resource.",
    )

    requestor: fhirtypes.Boolean = Field(
        None,
        alias="requestor",
        title="Type `bool`.",
        description="Whether user is initiator.",
    )

    role: ListType[CodeableConcept] = Field(
        None,
        alias="role",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="User roles (e.g. local RBAC codes).",
    )

    userId: Identifier = Field(
        None,
        alias="userId",
        title="Type `Identifier` (represented as `dict` in JSON).",
        description="Unique identifier for the user.",
    )


class AuditEventParticipantNetwork(BackboneElement):
    """Logical network location for application activity.

    Logical network location for application activity, if the activity has a
    network location.
    """

    resource_type: str = Field("AuditEventParticipantNetwork", const=True)

    address: fhirtypes.String = Field(
        None,
        alias="address",
        title="Type `str`.",
        description="Identifier for the network access point of the user device.",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `str`.",
        description="The type of network access point.",
    )


class AuditEventSource(BackboneElement):
    """Application systems and processes."""

    resource_type: str = Field("AuditEventSource", const=True)

    identifier: Identifier = Field(
        ...,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON).",
        description="The identity of source detecting the event.",
    )

    site: fhirtypes.String = Field(
        None,
        alias="site",
        title="Type `str`.",
        description="Logical source location within the enterprise.",
    )

    type: ListType[Coding] = Field(
        None,
        alias="type",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="The type of source where event originated.",
    )


AuditEvent.update_forward_refs()
AuditEventObject.update_forward_refs()
AuditEventParticipant.update_forward_refs()
