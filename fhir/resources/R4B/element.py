# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing
from typing import TYPE_CHECKING

from pydantic.v1 import Field
from pydantic.v1.parse import load_str_bytes

from fhir.resources.core import fhirabstractmodel

from . import fhirtypes
from .fhirtypesvalidators import fhir_model_validator

if TYPE_CHECKING:
    from pydantic.v1.typing import CallableGenerator


class classproperty:
    def __init__(self, func):
        self.fget = func

    def __get__(self, instance, owner):
        return self.fget(owner)


class Element(fhirabstractmodel.FHIRAbstractModel):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base for all elements.
    Base definition for all elements in a resource.
    """

    resource_type: str = Field("Element", const=True)

    extension: typing.List[fhirtypes.ExtensionType] = Field(
        None,
        alias="extension",
        title="Additional content defined by implementations",
        description=(
            "May be used to represent additional information that is not part of "
            "the basic definition of the element. To make the use of extensions "
            "safe and manageable, there is a strict set of governance  applied to "
            "the definition and use of extensions. Though any implementer can "
            "define an extension, there is a set of requirements that SHALL be met "
            "as part of the definition of the extension."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    id: fhirtypes.Id = Field(
        None,
        alias="id",
        title="Unique id for inter-element referencing",
        description=(
            "Unique id for the element within a resource (for internal references)."
            " This may be any string value that does not contain spaces."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Element`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension"]

    __fhir_release__: str = "R4B"

    @classproperty
    def __resource_type__(cls) -> str:
        """Resource type."""
        return cls.__name__

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":
        yield cls.validate

    @classmethod
    def validate(cls, v, values, config, field):
        """ """
        if isinstance(v, fhirabstractmodel.FHIRAbstractModel):
            resource_type = v.resource_type
        elif "resourceType" not in cls.__fields__:
            if isinstance(v, (bytes, str)):
                input_data = load_str_bytes(v)
                resource_type = input_data.get("resourceType", None)
            else:
                resource_type = v.get("resourceType", None)
        else:
            resource_type = None
        if resource_type is None:
            resource_type = cls.__resource_type__
        v = fhir_model_validator(resource_type, v)
        return v

    @classmethod
    def is_primitive(cls) -> bool:
        """ """
        return False

    @classmethod
    def fhir_type_name(cls) -> str:
        """ """
        return cls.__resource_type__
