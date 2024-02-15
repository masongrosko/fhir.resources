# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""

from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .quantity import Quantity
from .ratio import Ratio
from .reference import Reference


class Medication(DomainResource):
    """Definition of a Medication.

    This resource is primarily used for the identification and definition of a
    medication. It covers the ingredients and the packaging for a medication.
    """

    resource_type: str = Field("Medication", const=True)

    code: CodeableConcept = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Codes that identify this medication.",
    )

    isBrand: fhirtypes.Boolean = Field(
        None, alias="isBrand", title="Type `Boolean`.", description="True if a brand."
    )

    manufacturer: Reference = Field(
        None,
        alias="manufacturer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Manufacturer of the item.",
    )

    package: "MedicationPackage" = Field(
        None,
        alias="package",
        title="Type `MedicationPackage` (represented as `dict` in JSON).",
        description="Details about packaged medications.",
    )

    product: "MedicationProduct" = Field(
        None,
        alias="product",
        title="Type `MedicationProduct` (represented as `dict` in JSON).",
        description="Administrable medication details.",
    )


class MedicationPackage(BackboneElement):
    """Details about packaged medications.

    Information that only applies to packages (not products).
    """

    resource_type: str = Field("MedicationPackage", const=True)

    container: CodeableConcept = Field(
        None,
        alias="container",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="E.g. box, vial, blister-pack.",
    )

    content: ListType["MedicationPackageContent"] = Field(
        None,
        alias="content",
        title="List of `MedicationPackageContent` items (represented as `dict` in JSON).",
        description="What is  in the package.",
    )


class MedicationPackageContent(BackboneElement):
    """What is  in the package.

    A set of components that go to make up the described item.
    """

    resource_type: str = Field("MedicationPackageContent", const=True)

    amount: Quantity = Field(
        None,
        alias="amount",
        title="Type `Quantity` (represented as `dict` in JSON).",
        description="Quantity present in the package.",
    )

    item: Reference = Field(
        None,
        alias="item",
        title="Type `Reference` referencing `Medication` (represented as `dict` in JSON).",
        description="A product in the package.",
    )


class MedicationProduct(BackboneElement):
    """Administrable medication details.

    Information that only applies to products (not packages).
    """

    resource_type: str = Field("MedicationProduct", const=True)

    form: CodeableConcept = Field(
        None,
        alias="form",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="powder | tablets | carton +.",
    )
    batch: ListType["MedicationProductBatch"] = Field(
        None,
        alias="batch",
        title="List of `MedicationProductBatch` items (represented as `dict` in JSON).",
        description=None,
    )

    ingredient: ListType["MedicationProductIngredient"] = Field(
        None,
        alias="ingredient",
        title="List of `MedicationProductIngredient` items (represented as `dict` in JSON).",
        description="Active or inactive ingredient.",
    )


class MedicationProductBatch(BackboneElement):
    """None.

    Information about a group of medication produced or packaged from one
    production run.
    """

    resource_type: str = Field("MedicationProductBatch", const=True)

    expirationDate: fhirtypes.DateTime = Field(
        None, alias="expirationDate", title="Type `DateTime`.", description=None
    )
    lotNumber: fhirtypes.String = Field(
        None, alias="lotNumber", title="Type `String`.", description=None
    )


class MedicationProductIngredient(BackboneElement):
    """Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """

    resource_type: str = Field("MedicationProductIngredient", const=True)

    amount: Ratio = Field(
        None,
        alias="amount",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Quantity of ingredient present.",
    )

    item: Reference = Field(
        None,
        alias="item",
        title=(
            "Type `Reference` referencing "
            "`Substance, Medication` (represented as `dict` in JSON)."
        ),
        description="The product contained.",
    )


Medication.update_forward_refs()
MedicationPackage.update_forward_refs()
MedicationProduct.update_forward_refs()
