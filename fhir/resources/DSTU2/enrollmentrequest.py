# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/enrollmentrequest.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import domainresource, fhirtypes
from .coding import Coding
from .identifier import Identifier
from .reference import Reference


class EnrollmentRequest(domainresource.DomainResource):
    """Enroll in coverage.
    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """

    resource_type: str = Field("EnrollmentRequest", const=True)

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
    )

    ruleset: Coding = Field(
        None,
        alias="ruleset",
        title="Resource version",
        description=(
            "The version of the style of resource contents. This should be"
            "mapped to the allowable profiles for this and supporting resources."
        ),
    )

    originalRuleset: Coding = Field(
        None,
        alias="originalRuleset",
        title="Original version",
        description=(
            "The style (standard) and version of the original material "
            "which was converted into this resource."
        ),
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description="The date when this resource was created.",
    )

    target: Reference = Field(
        None,
        alias="target",
        title="Target",
        description="The Insurer who is target  of the request.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    provider: Reference = Field(
        None,
        alias="provider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    organization: Reference = Field(
        None,
        alias="organization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the"
            "services rendered to the patient."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    subject: Reference = Field(
        ...,
        alias="subject",
        title="The subject to be enrolled",
        description="Patient Resource.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    coverage: Reference = Field(
        ...,
        alias="coverage",
        title="Insurance information",
        description="Reference to the program or plan identification, underwriter or payor.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Coverage"],
    )

    relationship: Coding = Field(
        ...,
        alias="relationship",
        title="Patient relationship to subscriber",
        description="The relationship of the patient to the subscriber.",
    )
