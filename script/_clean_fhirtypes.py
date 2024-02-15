"""Clean all fhirtype files."""

import re
from collections import defaultdict, deque
from pathlib import Path

REQUIRED_ABSTRACT_TYPES = {
    "BackboneElement": ["Extension"],
    "BackboneType": ["Extension"],
    "Element": ["Extension"],
    "Reference": ["Identifier"],
}

PRE_BASE = """
from typing import TYPE_CHECKING
from pydantic.v1.parse import load_str_bytes
from fhir.resources.core import fhirabstractmodel
from .fhirtypesvalidators import fhir_model_validator

if TYPE_CHECKING:
    from pydantic.v1.typing import CallableGenerator


class classproperty:
    def __init__(self, func):
        self.fget = func

    def __get__(self, instance, owner):
        return self.fget(owner)


class {class_name}("""

POST_BASE = '''
    __fhir_release__: str = "{fhir_release}"

    @classproperty
    def __resource_type__(cls) -> str:
        """Resource type."""
        return cls.__name__

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":
        yield cls.validate

    @classmethod
    def validate(cls, v, values, config, field):
        """
        """
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
'''


def add_base_validator(doc, class_name, fhir_release):
    """Add validator code to base."""
    doc = doc.replace(
        f"class {class_name}(",
        PRE_BASE.format(class_name=class_name),
    )
    doc = doc + POST_BASE.format(fhir_release=fhir_release)

    return doc


def _type_exclusion_defaultdict(file_exclusion_mapping):
    excluded_types_by_file = defaultdict(lambda: ["FHIRPrimitiveExtension"])
    for key, value in file_exclusion_mapping.items():
        excluded_types_by_file[key].extend(value)

    return excluded_types_by_file


def _remove_defined_values(doc, pattern, excluded, all_suffix=""):
    """Remove defined value from doc."""
    any_class_name = r"(.*)"

    pat_matches = re.finditer(pattern.format(class_name=any_class_name), doc)
    for pat_match in pat_matches:
        if pat_match.group(1) in excluded:
            continue

        to_remove = re.search(pattern.format(class_name=pat_match.group(1)), doc)
        if to_remove is None:
            raise ValueError(f"Could not find {pat_match.group(1)} in doc.")

        doc = doc[: to_remove.start()] + doc[to_remove.end() :]

        remove_from_all = re.search(rf'"{pat_match.group(1)}{all_suffix}",.*', doc)
        if remove_from_all is None:
            print(f"Could not find {pat_match.group(1)} in __all__, weird.")
        else:
            doc = doc[: remove_from_all.start()] + doc[remove_from_all.end() :]

    return doc


def remove_unused_validators(doc):
    """Remove unused validators from fhirtypesvalidators."""
    validator_function = r"def\s{class_name}_validator\([\s\S]+?\n\n\n"
    excluded_types_by_file = _type_exclusion_defaultdict(REQUIRED_ABSTRACT_TYPES)
    excluded_validators: set = {
        _type.lower() for _, val in excluded_types_by_file.items() for _type in val
    }
    return _remove_defined_values(
        doc,
        pattern=validator_function,
        excluded=excluded_validators | {"fhir_model"},
        all_suffix="_validator",
    )


def remove_unused_types(doc):
    """Remove unused types from fhirtypes."""
    abstract_type_class = r"class\s{class_name}\(\s*Abstract.*Type\s*\)[\s\S]+?\n\n\n"
    excluded_types_by_file = _type_exclusion_defaultdict(REQUIRED_ABSTRACT_TYPES)
    excluded_types: set = {
        _type + "Type" for key, val in excluded_types_by_file.items() for _type in val
    }
    return _remove_defined_values(
        doc, pattern=abstract_type_class, excluded=excluded_types
    )


def fix_fhir_types(doc):
    """Fix fhir types typing."""
    excluded_types_by_file = _type_exclusion_defaultdict(REQUIRED_ABSTRACT_TYPES)
    fhir_type_pattern = r"fhirtypes\.(.*)Type"

    new_file = doc
    pat_matches = re.finditer(fhir_type_pattern, doc)
    imported_classes = []
    for pat_match in pat_matches:
        class_name = pat_match.group(1)
        if class_name in excluded_types_by_file[get_file_name(doc)]:
            continue

        replace_str = class_name

        if re.search(f"class {re.escape(class_name)}", doc) is not None:
            replace_str = f'"{class_name}"'
            class_to_reload = re.findall(
                r"\nclass (\w*)", new_file[: pat_match.start()]
            ).pop()
            reload_str = f"\n{class_to_reload}.update_forward_refs()"
            if class_to_reload and reload_str not in new_file:
                new_file = new_file + reload_str

        elif class_name not in imported_classes:
            new_file = add_import_statement(class_name, new_file)
            imported_classes.append(class_name)

        new_file = re.sub(
            rf"fhirtypes\.{re.escape(class_name)}Type", replace_str, new_file
        )

    return new_file


def fix_resource_type(doc):
    """Fix resource type typing."""
    resource_type_pattern = r"resource_type = Field\(\s*\"(.*)\""

    return re.sub(resource_type_pattern, 'resource_type: str = Field("\\1"', doc)


def add_import_statement(class_name, doc):
    """Add import statements."""
    try:
        last_import_in_doc = deque(re.finditer(r"\nfrom .* import .*\n", doc)).pop()
    except IndexError:
        raise ValueError("Document has no 'from . import' statements.")

    new_doc = (
        doc[: last_import_in_doc.end()]
        + f"from .{class_name.lower()} import {class_name}\n"
        + doc[last_import_in_doc.end() :]
    )

    return new_doc


def remove_unused_imports(doc):
    """Remove unused imports."""
    modules_pattern = r"([^(\n]*)(\([^)]*\))?"
    import_pattern = rf"(from\s+\..*\s+import\s+){modules_pattern}"
    # group 1: base import statement
    # group 2: all imported modules in single line import
    # group 3: all imported modules in multi line import

    out = doc
    pat_matches = re.finditer(import_pattern, doc)
    for pat_match in pat_matches:
        modules_str = pat_match.group(2) or pat_match.group(3) or ""
        modules = re.split(
            r",\s+", modules_str.strip("(").strip(")").strip().strip(",")
        )

        active_modules = []
        for module in modules:
            if len(re.findall(rf"\b{module}\b", out)) > 1:
                active_modules.append(module)
            else:
                print(get_file_name(doc))

        if len(active_modules) == len(modules):
            continue

        new_import_line = ""
        if active_modules:
            new_import_line = f"{pat_match.group(1)}{', '.join(active_modules)}"

        out = re.sub(rf"{pat_match.group(1)}{modules_pattern}", new_import_line, out)

    return out


def get_file_name(doc):
    file_name = re.search("http.*", doc[:200])
    if file_name:
        return f"{file_name.group().rsplit('/', 1)[-1]}"
    else:
        return ""


def test_remove_unused_import():
    out = remove_unused_imports(
        """
http://test_url/fake_file.com
from .asdf import asdfe, asdfg, asdf
from .ddd import rddrdr, rdrds
from . import (
    adfas,
    adfasdfasd,
    asdfad,
)
from .dddf import dffddf

asdfe
asdfad
adfasdfasd
dffddf
        """
    )

    print(out)


def sort_dot_imports(doc):
    """Sort import statements."""
    try:
        import isort
    except ImportError:
        min_start = float("inf")
        max_end = -1

        import_stmts = {}
        for import_stmt in re.finditer(r"\nfrom \.(.*) import .*", doc):
            min_start = min(min_start, import_stmt.start())
            max_end = max(max_end, import_stmt.end())

            import_stmts[import_stmt.group(1)] = import_stmt

        if not import_stmts:
            return doc

        out_str = ""
        for key in sorted(import_stmts.keys()):
            out_str += import_stmts[key].group()

        out_str = out_str.replace(r"\n\n", r"\n")

        return doc[:min_start] + out_str + doc[max_end:]
    else:
        return isort.code(doc)


def clean_up_files():
    """Remove files I added."""
    for py_file in Path(__file__).parent.rglob("*test_run.py"):
        py_file.unlink()


def format_doc(doc):
    """Format doc using black"""
    try:
        from black import FileMode, format_str
    except ImportError:
        return doc
    else:
        return format_str(doc, mode=FileMode())


def run_tests():
    import pytest

    folders_to_test = [
        [
            "fhir/resources",
            "--ignore=fhir/resources/DSTU2",
            "--ignore=fhir/resources/STU3",
            "--ignore=fhir/resources/R4B",
        ],
        ["fhir/resources/DSTU2"],
        ["fhir/resources/STU3"],
        ["fhir/resources/R4B"],
        ["tests"],
    ]
    for folder_to_test in folders_to_test:
        print(folder_to_test)
        ret_code = pytest.main(folder_to_test)
        print(ret_code)


if __name__ == "__main__":
    if vars().get("__file__") is None:
        __file__ = "./scripts/_clean_fhirtypes.py"

    folders_to_clean = [
        ("R5", "resources"),
        ("DSTU2", "resources/DSTU2"),
        ("STU3", "resources/STU3"),
        ("R4B", "resources/R4B"),
    ]
    for fhir_release, folder_to_clean in folders_to_clean:
        for py_file in Path(__file__).parents[1].rglob(f"fhir/*{folder_to_clean}/*.py"):
            if py_file.stem == "__init__":
                continue

            if py_file.stem.endswith("_test_run"):
                continue

            with open(py_file, "r") as f:
                og_file = f.read()

            new_file = fix_fhir_types(og_file)
            new_file = fix_resource_type(new_file)

            if py_file.stem in ["resource", "element"]:
                new_file = add_base_validator(
                    new_file, py_file.stem.title(), fhir_release
                )

            new_file = remove_unused_imports(new_file)
            new_file = sort_dot_imports(new_file)
            new_file = format_doc(new_file)

            if py_file.stem == "fhirtypes":
                new_file = remove_unused_types(new_file)
                new_file = format_doc(new_file)

            if py_file.stem != "fhirtypesvalidators":
                new_file = remove_unused_validators(new_file)
                new_file = format_doc(new_file)

            if new_file == og_file:
                continue

            out_path = py_file.with_stem(f"{py_file.stem}_test_run")
            out_path = py_file
            with open(out_path, "w") as f:
                f.write(new_file)
