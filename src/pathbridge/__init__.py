import sys
from importlib.metadata import version as _get_version

from .adapter import to_marshmallow
from .compiler import compile_rules, insert_error, translate_location

__version__ = _get_version("pathbridge")

version = f"{__version__}, Python {sys.version}"

__all__ = [
    "compile_rules",
    "translate_location",
    "insert_error",
    "to_marshmallow",
]
