# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Claim
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .coding import Coding
from .domainresource import DomainResource
from .identifier import Identifier
from .money import Money
from .quantity import Quantity
from .reference import Reference


class Claim(DomainResource):
    """Claim, Pre-determination or Pre-authorization.

    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    resource_type: str = Field("Claim", const=True)

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Type",
    )

    accident: fhirtypes.Date = Field(
        None,
        alias="accident",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Accident Date",
    )
    accidentType: Coding = Field(
        None,
        alias="accidentType",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Accident Date",
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Creation date",
    )

    diagnosis: ListType["ClaimDiagnosis"] = Field(
        None,
        alias="diagnosis",
        title="List of `ClaimDiagnosis` items (represented as `dict` in JSON)",
        description="List of Diagnosis",
    )

    enterer: Reference = Field(
        None,
        alias="enterer",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Author",
    )

    facility: Reference = Field(
        None,
        alias="facility",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Servicing Facility",
    )

    fundsReserve: Coding = Field(
        None,
        alias="fundsReserve",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Funds requested to be reserved",
    )

    identifier: ListType[Identifier] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Claim number",
    )

    item: ListType["ClaimItem"] = Field(
        None,
        alias="item",
        title="List of `ClaimItem` items (represented as `dict` in JSON)",
        description="Goods and Services",
    )

    organization: Reference = Field(
        None,
        alias="organization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible organization",
    )

    originalPrescription: Reference = Field(
        None,
        alias="originalPrescription",
        title=(
            "Type `Reference` referencing `MedicationRequest` (represented as "
            "`dict` in JSON)"
        ),
        description="Original prescription if superceded by fulfiller",
    )

    patient: Reference = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="The subject of the Products and Services",
    )

    payee: "ClaimPayee" = Field(
        None,
        alias="payee",
        title="Type `ClaimPayee` (represented as `dict` in JSON)",
        description="Party to be paid any benefits payable",
    )

    prescription: Reference = Field(
        None,
        alias="prescription",
        title=(
            "Type `Reference` referencing `MedicationRequest, VisionPrescription` "
            "(represented as `dict` in JSON)"
        ),
        description="Prescription authorizing services or products",
    )

    priority: Coding = Field(
        None,
        alias="priority",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Desired processing priority",
    )

    provider: Reference = Field(
        None,
        alias="provider",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible provider",
    )

    referral: Reference = Field(
        None,
        alias="referral",
        title=(
            "Type `Reference` referencing `ReferralRequest` (represented as `dict` "
            "in JSON)"
        ),
        description="Treatment Referral",
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="complete | proposed | exploratory | other",
    )
    additionalMaterials: ListType[Coding] = Field(
        None,
        alias="additionalMaterials",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Additional materials, documents, etc..",
    )

    condition: ListType[Coding] = Field(
        None,
        alias="condition",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="List of presenting Conditions.",
    )
    coverage: ListType["ClaimCoverage"] = Field(
        None,
        alias="coverage",
        title="List of `ClaimCoverage` items (represented as `dict` in JSON).",
        description="Insurance or medical plan.",
    )

    exception: ListType[Coding] = Field(
        None,
        alias="exception",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Eligibility exceptions.",
    )

    interventionException: ListType[Coding] = Field(
        None,
        alias="interventionException",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Intervention and exception code (Pharma).",
    )

    missingTeeth: ListType["ClaimMissingTeeth"] = Field(
        None,
        alias="missingTeeth",
        title="List of `ClaimMissingTeeth` items (represented as `dict` in JSON).",
        description="Only if type = oral.",
    )

    originalRuleset: Coding = Field(
        None,
        alias="originalRuleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Original specification followed.",
    )

    ruleset: Coding = Field(
        None,
        alias="ruleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Current specification followed.",
    )

    school: fhirtypes.String = Field(
        None, alias="school", title="Type `str`.", description="Name of School."
    )

    target: Reference = Field(
        None,
        alias="target",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Insurer.",
    )


class ClaimCoverage(BackboneElement):
    """Insurance or medical plan.

    Financial instrument by which payment information for health care.
    """

    resource_type: str = Field("ClaimCoverage", const=True)

    businessArrangement: fhirtypes.String = Field(
        None,
        alias="businessArrangement",
        title="Type `str`.",
        description="Business agreement.",
    )

    claimResponse: Reference = Field(
        None,
        alias="claimResponse",
        title="Type `Reference` referencing `ClaimResponse` (represented as `dict` in JSON).",
        description="Adjudication results.",
    )

    coverage: Reference = Field(
        None,
        alias="coverage",
        title="Type `Reference` referencing `Coverage` (represented as `dict` in JSON).",
        description="Insurance information.",
    )

    focal: fhirtypes.Boolean = Field(
        None, alias="focal", title="Type `bool`.", description="The focal Coverage."
    )

    originalRuleset: Coding = Field(
        None,
        alias="originalRuleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Original version.",
    )

    preAuthRef: ListType[fhirtypes.String] = Field(
        None,
        alias="preAuthRef",
        title="List of `str` items.",
        description="Pre-Authorization/Determination Reference.",
    )

    relationship: Coding = Field(
        None,
        alias="relationship",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Patient relationship to subscriber.",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `int`.",
        description="Service instance identifier.",
    )


class ClaimDiagnosis(BackboneElement):
    """Diagnosis.

    Ordered list of patient diagnosis for which care is sought.
    """

    resource_type: str = Field("ClaimDiagnosis", const=True)

    diagnosis: Coding = Field(
        ...,
        alias="diagnosis",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Patient's list of diagnosis.",
    )
    sequence: fhirtypes.PositiveInt = Field(
        ..., alias="sequence", title="Type `int`.", description="Sequence of diagnosis."
    )


class ClaimItem(BackboneElement):
    """Goods and Services.

    First tier of goods and services.
    """

    resource_type = "ClaimItem"

    bodySite: Coding = Field(
        None,
        alias="bodySite",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Service Location.",
    )

    detail: ListType["ClaimItemDetail"] = Field(
        None,
        alias="detail",
        title="List of `ClaimItemDetail` items (represented as `dict` in JSON).",
        description="Additional items.",
    )

    diagnosisLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="diagnosisLinkId",
        title="List of `int` items.",
        description="Diagnosis Link.",
    )

    factor: fhirtypes.Decimal = Field(
        None, alias="factor", title="Type `float`.", description="Price scaling factor."
    )

    modifier: ListType[Coding] = Field(
        None,
        alias="modifier",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Service/Product billing modifiers.",
    )

    net: Money = Field(
        None,
        alias="net",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Total item cost.",
    )

    points: fhirtypes.Decimal = Field(
        None,
        alias="points",
        title="Type `float`.",
        description="Difficulty scaling factor.",
    )

    prosthesis: "ClaimItemProsthesis" = Field(
        None,
        alias="prosthesis",
        title="Type `ClaimItemProsthesis` (represented as `dict` in JSON).",
        description="Prosthetic details.",
    )

    provider: Reference = Field(
        None,
        alias="provider",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON).",
        description="Responsible practitioner.",
    )

    quantity: Quantity = Field(
        None,
        alias="quantity",
        title="Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON).",
        description="Count of Products or Services.",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ..., alias="sequence", title="type `int`.", description="Service instance."
    )

    service: Coding = Field(
        None,
        alias="service",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Item Code.",
    )

    serviceDate: fhirtypes.Date = Field(
        None,
        alias="serviceDate",
        title="Type `Date` (represented as `str` in JSON).",
        description="Date of Service.",
    )

    subSite: ListType[Coding] = Field(
        None,
        alias="subSite",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Service Sub-location.",
    )

    type: Coding = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Group or type of product or service.",
    )

    udi: Coding = Field(
        None,
        alias="udi",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Unique Device Identifier.",
    )

    unitPrice: Money = Field(
        None,
        alias="unitPrice",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Fee, charge or cost per point.",
    )


class ClaimItemDetail(BackboneElement):
    """Additional items.

    Second tier of goods and services.
    """

    resource_type: str = Field("ClaimItemDetail", const=True)

    type: Coding = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Group or type of product or service.",
    )

    udi: Coding = Field(
        None,
        alias="udi",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Unique Device Identifier.",
    )

    unitPrice: Money = Field(
        None,
        alias="unitPrice",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Fee, charge or cost per point.",
    )
    sequence: fhirtypes.PositiveInt = Field(
        ..., alias="sequence", title="type `int`.", description="Service instance."
    )

    service: Coding = Field(
        None,
        alias="service",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Item Code.",
    )
    quantity: Quantity = Field(
        None,
        alias="quantity",
        title="Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON).",
        description="Count of Products or Services.",
    )
    factor: fhirtypes.Decimal = Field(
        None, alias="factor", title="Type `float`.", description="Price scaling factor."
    )
    net: Money = Field(
        None,
        alias="net",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Total item cost.",
    )

    points: fhirtypes.Decimal = Field(
        None,
        alias="points",
        title="Type `float`.",
        description="Difficulty scaling factor.",
    )

    subDetail: ListType["ClaimItemDetailSubDetail"] = Field(
        None,
        alias="subDetail",
        title="List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON).",
        description="Additional items.",
    )


class ClaimItemDetailSubDetail(BackboneElement):
    """Additional items.

    Third tier of goods and services.
    """

    resource_type: str = Field("ClaimItemDetailSubDetail", const=True)

    type: Coding = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Group or type of product or service.",
    )
    udi: Coding = Field(
        None,
        alias="udi",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Unique Device Identifier.",
    )

    unitPrice: Money = Field(
        None,
        alias="unitPrice",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Fee, charge or cost per point.",
    )
    sequence: fhirtypes.PositiveInt = Field(
        ..., alias="sequence", title="type `int`.", description="Service instance."
    )

    service: Coding = Field(
        None,
        alias="service",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Item Code.",
    )
    quantity: Quantity = Field(
        None,
        alias="quantity",
        title="Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON).",
        description="Count of Products or Services.",
    )
    factor: fhirtypes.Decimal = Field(
        None, alias="factor", title="Type `float`.", description="Price scaling factor."
    )
    net: Money = Field(
        None,
        alias="net",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Total item cost.",
    )

    points: fhirtypes.Decimal = Field(
        None,
        alias="points",
        title="Type `float`.",
        description="Difficulty scaling factor.",
    )


class ClaimItemProsthesis(BackboneElement):
    """Prosthetic details.

    The materials and placement date of prior fixed prosthesis.
    """

    resource_type: str = Field("ClaimItemProsthesis", const=True)

    initial: fhirtypes.Boolean = Field(
        None,
        alias="initial",
        title="Type `bool`.",
        description="Is this the initial service.",
    )

    priorDate: fhirtypes.Date = Field(
        None,
        alias="priorDate",
        title="Type `Date` (represented as `str` in JSON).",
        description="Initial service Date.",
    )

    priorMaterial: Coding = Field(
        None,
        alias="priorMaterial",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Prosthetic Material.",
    )


class ClaimMissingTeeth(BackboneElement):
    """Only if type = oral.

    A list of teeth which would be expected but are not found due to having
    been previously  extracted or for other reasons.
    """

    resource_type: str = Field("ClaimMissingTeeth", const=True)

    extractionDate: fhirtypes.Date = Field(
        None,
        alias="extractionDate",
        title="Type `Date` (represented as `str` in JSON).",
        description="Date of Extraction.",
    )

    reason: Coding = Field(
        None,
        alias="reason",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Reason for missing.",
    )

    tooth: Coding = Field(
        None,
        alias="tooth",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Tooth Code.",
    )


class ClaimPayee(BackboneElement):
    """Payee.

    The party to be reimbursed for the services.
    """

    resource_type: str = Field("ClaimPayee", const=True)

    organization: Reference = Field(
        None,
        alias="organization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Organization who is the payee.",
    )

    person: Reference = Field(
        None,
        alias="person",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="Other person who is the payee.",
    )

    provider: Reference = Field(
        None,
        alias="provider",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON).",
        description="Provider who is the payee.",
    )

    type: Coding = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Party to be paid any benefits payable.",
    )


Claim.update_forward_refs()
ClaimItem.update_forward_refs()
ClaimItemDetailSubDetail.update_forward_refs()
