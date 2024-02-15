# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/paymentnotice.html
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


class PaymentNotice(domainresource.DomainResource):
    """PaymentNotice request



    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """

    resource_type: str = Field("PaymentNotice", const=True)

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description="The Response business identifier.",
        element_property=True,
    )

    ruleset: Coding = Field(
        None,
        alias="ruleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Resource version",
        element_property=True,
    )

    originalRuleset: Coding = Field(
        None,
        alias="originalRuleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Original version",
        element_property=True,
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description="The date when this resource was created.",
        element_property=True,
    )

    target: Reference = Field(
        None,
        alias="target",
        title="Type 'Reference' referencing 'Organization'  (represented as 'dict' in JSON).",
        description="Insurer or Regulatory body",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
        element_property=True,
    )

    provider: Reference = Field(
        None,
        alias="provider",
        title="Type 'Reference' referencing 'Practitioner'  (represented as 'dict' in JSON).",
        description="Responsible practitioner",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
        element_property=True,
    )

    organization: Reference = Field(
        None,
        alias="organization",
        title="Type 'Reference' referencing 'Organization'  (represented as 'dict' in JSON).",
        description="Responsible organization",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
        element_property=True,
    )

    request: Reference = Field(
        None,
        alias="request",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Request reference",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    response: Reference = Field(
        None,
        alias="response",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Response reference",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    paymentStatus: Coding = Field(
        None,
        alias="paymentStatus",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Status of the payment",
        element_property=True,
    )
