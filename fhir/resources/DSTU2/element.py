# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import TYPE_CHECKING
from typing import List as ListType

from pydantic.v1 import Field
from pydantic.v1.parse import load_str_bytes

from fhir.resources.core import fhirabstractmodel

from . import fhirtypes
from .fhirabstractmodel import FHIRAbstractModel
from .fhirtypesvalidators import fhir_model_validator

if TYPE_CHECKING:
    from pydantic.v1.typing import CallableGenerator


class classproperty:
    def __init__(self, func):
        self.fget = func

    def __get__(self, instance, owner):
        return self.fget(owner)


class Element(FHIRAbstractModel):
    """Base for all elements.
    Base definition for all elements in a resource.
    """

    resource_type: str = Field("Element", const=True)

    extension: ListType[fhirtypes.ExtensionType] = Field(
        None,
        alias="extension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Additional Content defined by implementations",
    )

    id: fhirtypes.String = Field(
        None,
        alias="id",
        title="Type `String` (represented as `dict` in JSON)",
        description="xml:id (or equivalent in JSON)",
    )

    __fhir_release__: str = "DSTU2"

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
