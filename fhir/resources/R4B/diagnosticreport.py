# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
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
from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .identifier import Identifier
from .period import Period
from .reference import Reference


class DiagnosticReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.
    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
    """

    resource_type: str = Field("DiagnosticReport", const=True)

    basedOn: typing.List[Reference] = Field(
        None,
        alias="basedOn",
        title="What was requested",
        description="Details concerning a service requested.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "CarePlan",
            "ImmunizationRecommendation",
            "MedicationRequest",
            "NutritionOrder",
            "ServiceRequest",
        ],
    )

    category: typing.List[CodeableConcept] = Field(
        None,
        alias="category",
        title="Service category",
        description=(
            "A code that classifies the clinical discipline, department or "
            "diagnostic service that created the report (e.g. cardiology, "
            "biochemistry, hematology, MRI). This is used for searching, sorting "
            "and display purposes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: CodeableConcept = Field(
        ...,
        alias="code",
        title="Name/Code for this diagnostic report",
        description="A code or name that describes this diagnostic report.",
        # if property is element of this resource.
        element_property=True,
    )

    conclusion: fhirtypes.String = Field(
        None,
        alias="conclusion",
        title="Clinical conclusion (interpretation) of test results",
        description=(
            "Concise and clinically contextualized summary conclusion "
            "(interpretation/impression) of the diagnostic report."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    conclusion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_conclusion", title="Extension field for ``conclusion``."
    )

    conclusionCode: typing.List[CodeableConcept] = Field(
        None,
        alias="conclusionCode",
        title="Codes for the clinical conclusion of test results",
        description=(
            "One or more codes that represent the summary conclusion "
            "(interpretation/impression) of the diagnostic report."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="Clinically relevant time/time-period for report",
        description=(
            "The time or time-period the observed values are related to. When the "
            "subject of the report is a patient, this is usually either the time of"
            " the procedure or of specimen collection(s), but very often the source"
            " of the date/time is not known, only the date/time itself."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=False,
    )
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_effectiveDateTime",
        title="Extension field for ``effectiveDateTime``.",
    )

    effectivePeriod: Period = Field(
        None,
        alias="effectivePeriod",
        title="Clinically relevant time/time-period for report",
        description=(
            "The time or time-period the observed values are related to. When the "
            "subject of the report is a patient, this is usually either the time of"
            " the procedure or of specimen collection(s), but very often the source"
            " of the date/time is not known, only the date/time itself."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=False,
    )

    encounter: Reference = Field(
        None,
        alias="encounter",
        title="Health care event when test ordered",
        description=(
            "The healthcare event  (e.g. a patient and healthcare provider "
            "interaction) which this DiagnosticReport is about."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: typing.List[Identifier] = Field(
        None,
        alias="identifier",
        title="Business identifier for report",
        description="Identifiers assigned to this report by the performer or other systems.",
        # if property is element of this resource.
        element_property=True,
    )

    imagingStudy: typing.List[Reference] = Field(
        None,
        alias="imagingStudy",
        title=(
            "Reference to full details of imaging associated with the diagnostic "
            "report"
        ),
        description=(
            "One or more links to full details of any imaging performed during the "
            "diagnostic investigation. Typically, this is imaging performed by "
            "DICOM enabled modalities, but this is not required. A fully enabled "
            "PACS viewer can use this information to provide views of the source "
            "images."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ImagingStudy"],
    )

    issued: fhirtypes.Instant = Field(
        None,
        alias="issued",
        title="DateTime this version was made",
        description=(
            "The date and time that this version of the report was made available "
            "to providers, typically after the report was reviewed and verified."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issued", title="Extension field for ``issued``."
    )

    media: typing.List["DiagnosticReportMedia"] = Field(
        None,
        alias="media",
        title="Key images associated with this report",
        description=(
            "A list of key images associated with this report. The images are "
            "generally created during the diagnostic process, and may be directly "
            "of the patient, or of treated specimens (i.e. slides of interest)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    performer: typing.List[Reference] = Field(
        None,
        alias="performer",
        title="Responsible Diagnostic Service",
        description="The diagnostic service that is responsible for issuing the report.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "CareTeam",
        ],
    )

    presentedForm: typing.List[Attachment] = Field(
        None,
        alias="presentedForm",
        title="Entire report as issued",
        description=(
            "Rich text representation of the entire result as issued by the "
            "diagnostic service. Multiple formats are allowed but they SHALL be "
            "semantically equivalent."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    result: typing.List[Reference] = Field(
        None,
        alias="result",
        title="Observations",
        description=(
            "[Observations](observation.html)  that are part of this diagnostic "
            "report."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Observation"],
    )

    resultsInterpreter: typing.List[Reference] = Field(
        None,
        alias="resultsInterpreter",
        title="Primary result interpreter",
        description=(
            "The practitioner or organization that is responsible for the report's "
            "conclusions and interpretations."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "CareTeam",
        ],
    )

    specimen: typing.List[Reference] = Field(
        None,
        alias="specimen",
        title="Specimens this report is based on",
        description="Details about the specimens on which this diagnostic report is based.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="registered | partial | preliminary | final +",
        description="The status of the diagnostic report.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["registered", "partial", "preliminary", "final", "+"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: Reference = Field(
        None,
        alias="subject",
        title="The subject of the report - usually, but not always, the patient",
        description=(
            "The subject of the report. Usually, but not always, this is a patient."
            " However, diagnostic services also perform analyses on specimens "
            "collected from a variety of other sources."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Group",
            "Device",
            "Location",
            "Organization",
            "Procedure",
            "Practitioner",
            "Medication",
            "Substance",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DiagnosticReport`` according specification,
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
            "basedOn",
            "status",
            "category",
            "code",
            "subject",
            "encounter",
            "effectiveDateTime",
            "effectivePeriod",
            "issued",
            "performer",
            "resultsInterpreter",
            "specimen",
            "result",
            "imagingStudy",
            "media",
            "conclusion",
            "conclusionCode",
            "presentedForm",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1849(
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
    def validate_one_of_many_1849(
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
        one_of_many_fields = {"effective": ["effectiveDateTime", "effectivePeriod"]}
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


class DiagnosticReportMedia(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Key images associated with this report.
    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """

    resource_type: str = Field("DiagnosticReportMedia", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Comment about the image (e.g. explanation)",
        description=(
            "A comment about the image. Typically, this is used to provide an "
            "explanation for why the image is included, or to draw the viewer's "
            "attention to important features."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    link: Reference = Field(
        ...,
        alias="link",
        title="Reference to the image source",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Media"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DiagnosticReportMedia`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "comment", "link"]


DiagnosticReport.update_forward_refs()
