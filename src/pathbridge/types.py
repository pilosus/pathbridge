from __future__ import annotations

import re
from collections.abc import Iterable, Sequence
from typing import (
    Protocol,
    TypeAlias,
    TypedDict,
    Union,
)

#
# Aliases
#

LocationT = str  # validator-reported path (e.g., XPath/JSONPath/Pointer)
ErrorMessageT = str  # error message text
DestinationPathT = str  # key in raw rules (validator/document path)
FacadePathT = str  # your app/model path (facades destination)
FacadePathTemplateT = (
    str  # your app/model path with capture placeholders, e.g 'mtr/sa103s[{i1-1}]'
)

#
# Rules
#

# Raw rules
RawRulesMapT = dict[DestinationPathT, FacadePathT]

# Compiled rule used at runtime
CompiledRuleT = tuple[re.Pattern[str], FacadePathTemplateT]
CompiledRulesT = Sequence[CompiledRuleT]

#
# Errors
#

ErrorItemT = tuple[LocationT, ErrorMessageT]


# Think of GovTalk-style error items
class ErrorItemClassT(Protocol):
    location: Sequence[LocationT]  # list of validator locations
    text: Sequence[str]  # list of messages


class ErrorItemDictT(TypedDict):
    location: LocationT
    text: str


# Union accepted by adapters
ErrorInputT = (
    Iterable[ErrorItemT] | Iterable[ErrorItemClassT] | Iterable[ErrorItemDictT]
)

#
# Adapter related types
#

# A recursive mapping of str/int -> (subtree | list[str] messages)
# This keeps type-checkers happy when building nested error dicts
MarshmallowValidationErrorT: TypeAlias = dict[
    str | int,
    Union["MarshmallowValidationErrorT", list[str]],
]

#
# Public API
#

__all__ = [
    "LocationT",
    "DestinationPathT",
    "FacadePathT",
    "FacadePathTemplateT",
    "RawRulesMapT",
    "CompiledRuleT",
    "CompiledRulesT",
    "ErrorItemT",
    "ErrorItemClassT",
    "ErrorItemDictT",
    "ErrorInputT",
    "MarshmallowValidationErrorT",
]
