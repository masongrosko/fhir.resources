# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItem
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes
from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity
from .reference import Reference
from .timing import Timing


class ChargeItem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item containing charge code(s) associated with the provision of healthcare
    provider products.
    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like date,
    time, amounts and participating organizations and persons. Main Usage of
    the ChargeItem is to enable the billing process and internal cost
    allocation.
    """

    resource_type: str = Field("ChargeItem", const=True)

    account: typing.List[Reference] = Field(
        None,
        alias="account",
        title="Account to place this charge",
        description="Account into which this ChargeItems belongs.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Account"],
    )

    bodysite: typing.List[CodeableConcept] = Field(
        None,
        alias="bodysite",
        title="Anatomical location, if relevant",
        description="The anatomical location where the related service has been applied.",
        # if property is element of this resource.
        element_property=True,
    )

    code: CodeableConcept = Field(
        ...,
        alias="code",
        title="A code that identifies the charge, like a billing code",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    context: Reference = Field(
        None,
        alias="context",
        title="Encounter / Episode associated with event",
        description=(
            "The encounter or episode of care that establishes the context for this"
            " event."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    costCenter: Reference = Field(
        None,
        alias="costCenter",
        title="Organization that has ownership of the (potential, future) revenue",
        description="The financial cost center permits the tracking of charge attribution.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    definitionCanonical: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="definitionCanonical",
        title="Resource defining the code of this ChargeItem",
        description=(
            "References the source of pricing information, rules of application for"
            " the code this ChargeItem uses."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ChargeItemDefinition"],
    )
    definitionCanonical__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_definitionCanonical",
        title="Extension field for ``definitionCanonical``.",
    )

    definitionUri: typing.List[typing.Optional[fhirtypes.Uri]] = Field(
        None,
        alias="definitionUri",
        title="Defining information about the code of this charge item",
        description=(
            "References the (external) source of pricing information, rules of "
            "application for the code this ChargeItem uses."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    definitionUri__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_definitionUri", title="Extension field for ``definitionUri``."
    )

    enteredDate: fhirtypes.DateTime = Field(
        None,
        alias="enteredDate",
        title="Date the charge item was entered",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    enteredDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_enteredDate", title="Extension field for ``enteredDate``."
    )

    enterer: Reference = Field(
        None,
        alias="enterer",
        title="Individual who was entering",
        description="The device, practitioner, etc. who entered the charge item.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "Patient",
            "Device",
            "RelatedPerson",
        ],
    )

    factorOverride: fhirtypes.Decimal = Field(
        None,
        alias="factorOverride",
        title="Factor overriding the associated rules",
        description=(
            "Factor overriding the factor determined by the rules associated with "
            "the code."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    factorOverride__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factorOverride", title="Extension field for ``factorOverride``."
    )

    identifier: typing.List[Identifier] = Field(
        None,
        alias="identifier",
        title="Business Identifier for item",
        description="Identifiers assigned to this event performer or other systems.",
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[Annotation] = Field(
        None,
        alias="note",
        title="Comments made about the ChargeItem",
        description=(
            "Comments made about the event by the performer, subject or other "
            "participants."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When the charged service was applied",
        description="Date/time(s) or duration when the charged service was applied.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: Period = Field(
        None,
        alias="occurrencePeriod",
        title="When the charged service was applied",
        description="Date/time(s) or duration when the charged service was applied.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    occurrenceTiming: Timing = Field(
        None,
        alias="occurrenceTiming",
        title="When the charged service was applied",
        description="Date/time(s) or duration when the charged service was applied.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    overrideReason: fhirtypes.String = Field(
        None,
        alias="overrideReason",
        title="Reason for overriding the list price/factor",
        description=(
            "If the list price or the rule-based factor associated with the code is"
            " overridden, this attribute can capture a text to indicate the  reason"
            " for this action."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    overrideReason__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_overrideReason", title="Extension field for ``overrideReason``."
    )

    partOf: typing.List[Reference] = Field(
        None,
        alias="partOf",
        title="Part of referenced ChargeItem",
        description=(
            "ChargeItems can be grouped to larger ChargeItems covering the whole "
            "set."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ChargeItem"],
    )

    performer: typing.List["ChargeItemPerformer"] = Field(
        None,
        alias="performer",
        title="Who performed charged service",
        description=(
            "Indicates who or what performed or participated in the charged " "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    performingOrganization: Reference = Field(
        None,
        alias="performingOrganization",
        title="Organization providing the charged service",
        description="The organization requesting the service.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    priceOverride: Money = Field(
        None,
        alias="priceOverride",
        title="Price overriding the associated rules",
        description=(
            "Total price of the charge overriding the list price associated with "
            "the code."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    productCodeableConcept: CodeableConcept = Field(
        None,
        alias="productCodeableConcept",
        title="Product charged",
        description=(
            "Identifies the device, food, drug or other product being charged "
            "either by type code or reference to an instance."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e product[x]
        one_of_many="product",
        one_of_many_required=False,
    )

    productReference: Reference = Field(
        None,
        alias="productReference",
        title="Product charged",
        description=(
            "Identifies the device, food, drug or other product being charged "
            "either by type code or reference to an instance."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e product[x]
        one_of_many="product",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device", "Medication", "Substance"],
    )

    quantity: Quantity = Field(
        None,
        alias="quantity",
        title="Quantity of which the charge item has been serviced",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    reason: typing.List[CodeableConcept] = Field(
        None,
        alias="reason",
        title="Why was the charged  service rendered?",
        description="Describes why the event occurred in coded or textual form.",
        # if property is element of this resource.
        element_property=True,
    )

    requestingOrganization: Reference = Field(
        None,
        alias="requestingOrganization",
        title="Organization requesting the charged service",
        description="The organization performing the service.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    service: typing.List[Reference] = Field(
        None,
        alias="service",
        title="Which rendered service is being charged?",
        description="Indicated the rendered service that caused this charge.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "DiagnosticReport",
            "ImagingStudy",
            "Immunization",
            "MedicationAdministration",
            "MedicationDispense",
            "Observation",
            "Procedure",
            "SupplyDelivery",
        ],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "planned | billable | not-billable | aborted | billed | entered-in-"
            "error | unknown"
        ),
        description="The current state of the ChargeItem.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "planned",
            "billable",
            "not-billable",
            "aborted",
            "billed",
            "entered-in-error",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: Reference = Field(
        ...,
        alias="subject",
        title="Individual service was done for/to",
        description=(
            "The individual or set of individuals the action is being or was "
            "performed on."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    supportingInformation: typing.List[Reference] = Field(
        None,
        alias="supportingInformation",
        title="Further information supporting this charge",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ChargeItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "definitionUri",
            "definitionCanonical",
            "status",
            "partOf",
            "code",
            "subject",
            "context",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "performer",
            "performingOrganization",
            "requestingOrganization",
            "costCenter",
            "quantity",
            "bodysite",
            "factorOverride",
            "priceOverride",
            "overrideReason",
            "enterer",
            "enteredDate",
            "reason",
            "service",
            "productReference",
            "productCodeableConcept",
            "account",
            "note",
            "supportingInformation",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1161(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1161(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
            ],
            "product": ["productCodeableConcept", "productReference"],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class ChargeItemPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed charged service.
    Indicates who or what performed or participated in the charged service.
    """

    resource_type: str = Field("ChargeItemPerformer", const=True)

    actor: Reference = Field(
        ...,
        alias="actor",
        title="Individual who was performing",
        description=(
            "The device, practitioner, etc. who performed or participated in the "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "CareTeam",
            "Patient",
            "Device",
            "RelatedPerson",
        ],
    )

    function: CodeableConcept = Field(
        None,
        alias="function",
        title="What type of performance was done",
        description=(
            "Describes the type of performance or participation(e.g. primary "
            "surgeon, anesthesiologiest, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ChargeItemPerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]


ChargeItem.update_forward_refs()
