# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .identifier import Identifier
from .reference import Reference


class DiagnosticOrder(DomainResource):
    """A request for a diagnostic service.

    A record of a request for a diagnostic investigation service to be
    performed.
    """

    resource_type: str = Field("DiagnosticOrder", const=True)

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description=(
            "proposed | draft | planned | requested | received | accepted | "
            "in-progress | review | completed | cancelled | suspended | rejected | "
            "failed"
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "proposed",
            "draft",
            "planned",
            "requested",
            "received",
            "accepted",
            "in-progress",
            "review",
            "completed",
            "cancelled",
            "suspended",
            "rejected",
            "failed",
        ],
    )

    subject: Reference = Field(
        ...,
        alias="subject",
        title=(
            "Type `FHIRReference` referencing `Patient, Group, Location, Device` "
            "(represented as `dict` in JSON)."
        ),
        description="Who and/or what test is about.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group", "Location", "Device"],
    )

    encounter: Reference = Field(
        None,
        alias="encounter",
        title="Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON).",
        description="The encounter that this diagnostic order is associated with.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Identifiers assigned to this order.",
    )

    specimen: ListType[Reference] = Field(
        None,
        alias="specimen",
        title=(
            "List of `FHIRReference` items referencing `Specimen` (represented as "
            "`dict` in JSON)."
        ),
        description="If the whole order relates to specific specimens.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    orderer: Reference = Field(
        None,
        alias="orderer",
        title=(
            "Type `FHIRReference` referencing `Practitioner` "
            "(represented as `dict` in JSON)."
        ),
        description="Who ordered the test.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    reason: ListType[CodeableConcept] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Explanation/Justification for test.",
    )

    supportingInformation: ListType[Reference] = Field(
        None,
        alias="supportingInformation",
        title=(
            "List of `FHIRReference` items referencing `Observation, Condition, "
            "DocumentReference` (represented as `dict` in JSON)."
        ),
        description="Additional clinical information.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Observation", "Condition", "DocumentReference"],
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `str`.",
        description="routine | urgent | stat | asap",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["routine", "urgent", "asap", "stat"],
    )

    event: ListType["DiagnosticOrderEvent"] = Field(
        None,
        alias="event",
        title="List of `DiagnosticOrderEvent` items (represented as `dict` in JSON).",
        description="A list of events of interest in the lifecycle.",
    )

    item: ListType["DiagnosticOrderItem"] = Field(
        None,
        alias="item",
        title="List of `DiagnosticOrderItem` items (represented as `dict` in JSON).",
        description="The items the orderer requested.",
    )

    note: ListType[Annotation] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON).",
        description="Other notes and comments.",
    )


class DiagnosticOrderEvent(BackboneElement):
    """A list of events of interest in the lifecycle.

    A summary of the events of interest that have occurred as the request is
    processed; e.g. when the order was made, various processing steps
    (specimens received), when it was completed.
    """

    resource_type: str = Field("DiagnosticOrderEvent", const=True)

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `str`.",
        description=(
            "proposed | draft | planned | requested | received | accepted | "
            "in-progress | review | completed | cancelled | suspended | rejected | "
            "failed"
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "proposed",
            "draft",
            "planned",
            "requested",
            "received",
            "accepted",
            "in-progress",
            "review",
            "completed",
            "cancelled",
            "suspended",
            "rejected",
            "failed",
        ],
    )

    description: CodeableConcept = Field(
        None,
        alias="description",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="More information about the event and its context.",
    )

    dateTime: fhirtypes.DateTime = Field(
        ...,
        alias="dateTime",
        title="Type `DateTime` (represented as `str` in JSON).",
        description="The date at which the event happened.",
    )

    actor: Reference = Field(
        None,
        alias="actor",
        title=(
            "Type `Reference` referencing `Practitioner, "
            "Device` (represented as `dict` in JSON)."
        ),
        description="Who recorded or did this.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Device"],
    )


class DiagnosticOrderItem(BackboneElement):
    """The items the orderer requested.

    The specific diagnostic investigations that are requested as part of this
    request. Sometimes, there can only be one item per request, but in most
    contexts, more than one investigation can be requested.
    """

    resource_type: str = Field("DiagnosticOrderItem", const=True)

    code: CodeableConcept = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Code to indicate the item (test or panel) being ordered.",
    )

    specimen: ListType[Reference] = Field(
        None,
        alias="specimen",
        title=(
            "List of `FHIRReference` items referencing `Specimen` "
            "(represented as `dict` in JSON)."
        ),
        description="If this item relates to specific specimens.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    bodySite: CodeableConcept = Field(
        None,
        alias="bodySite",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Location of requested test (if applicable).",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `str`.",
        description=(
            "proposed | draft | planned | requested | received | accepted | "
            "in-progress | review | completed | cancelled | suspended | "
            "rejected | failed"
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "proposed",
            "draft",
            "planned",
            "requested",
            "received",
            "accepted",
            "in-progress",
            "review",
            "completed",
            "cancelled",
            "suspended",
            "rejected",
            "failed",
        ],
    )

    event: ListType["DiagnosticOrderEvent"] = Field(
        None,
        alias="event",
        title="List of `DiagnosticOrderEvent` items (represented as `dict` in JSON).",
        description="A list of events of interest in the lifecycle.",
    )


DiagnosticOrder.update_forward_refs()
DiagnosticOrderItem.update_forward_refs()
