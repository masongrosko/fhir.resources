# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/deviceuserequest.html
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


class EligibilityRequest(domainresource.DomainResource):
    """Eligibility request

    This resource provides the insurance eligibility details from the
    insurer regarding a specified coverage and optionally some class of service.
    """

    resource_type: str = Field("EligibilityRequest", const=True)

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description=("The Response business identifier."),
    )

    ruleset: Coding = Field(
        None,
        alias="ruleset",
        title="Resource version",
        description=(
            "The version of the style of resource contents."
            "This should be mapped to the allowable profiles for this and "
            "supporting resources."
        ),
    )

    originalRuleset: Coding = Field(
        None,
        alias="originalRuleset",
        title="Original version",
        description=(
            "The style (standard) and version of the original material"
            "which was converted into this resource."
        ),
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `FHIRDate` (represented as `str` in JSON).",
        description="Creation date",
    )

    target: Reference = Field(
        None,
        alias="target",
        title="Insurer",
        description=("The Insurer who is target of the request."),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    provider: Reference = Field(
        None,
        alias="provider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the"
            "services rendered to the patient."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    organization: Reference = Field(
        None,
        alias="organization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for "
            "the services rendered to the patient."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )
