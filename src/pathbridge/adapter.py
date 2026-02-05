from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import Any

from .compiler import insert_error, translate_location
from .types import (
    CompiledRulesT,
    ErrorInputT,
    ErrorItemT,
    LocationT,
    MarshmallowValidationErrorT,
)

#
# Public API
#


def to_marshmallow(
    items: ErrorInputT,
    compiled_rules: CompiledRulesT,
    *,
    default_message: str = "Invalid",
    include_meta: bool = False,
) -> dict[str | int, Any]:
    """
    Translate validator locations to facade paths and fold into a Marshmallow-style nested dict.

    include_meta adds a `_meta` key-val with translation stats and misses.

    Returns
    -------
    dict
        Nested structure compatible with Marshmallow errors, e.g.:
        {
          'mtr': {
            'sa103s': {
              6: {'net_profit_or_loss': ['The amount must equal ...']}
            }
          },
          '_meta': { ... }  # only when include_meta=True
        }
    """
    errors: MarshmallowValidationErrorT = {}
    total = 0
    matched = 0
    misses: list[tuple[LocationT, str]] = []

    for loc, msg in _iter_error_pairs(items, default_message):
        total += 1
        facade = translate_location(loc, compiled_rules)
        if facade is None:
            misses.append((loc, msg))
            continue
        insert_error(errors, facade, msg)
        matched += 1

    # shallow copy for meta injection
    result: dict[str | int, Any] = dict(errors)
    if include_meta:
        result["_meta"] = {
            "total": total,
            "matched": matched,
            "missed": len(misses),
            "misses": [{"location": loc, "message": msg} for (loc, msg) in misses],
        }
    return result


#
# Helpers
#


def _iter_error_pairs(items: ErrorInputT, default_message: str) -> Iterator[ErrorItemT]:
    """
    Normalize different error input shapes into (location, message) pairs.

    Supports:
      - Iterable[tuple[str, str]]
      - Iterable[dict] with 'location' (str|list[str]) and optional 'message' or 'text'
      - Iterable[objects] with .location (Sequence[str]) and .text (Sequence[str])
    """
    for item in items:
        # Case 1: already a (location, message) pair
        if (
            isinstance(item, tuple)
            and len(item) == 2
            and all(isinstance(x, str) for x in item)
        ):
            yield item
            continue

        # Case 2: dict-like (JSON-derived)
        if isinstance(item, dict) and "location" in item:
            locs = _as_list(item.get("location"))
            msgs = _as_list(item.get("message", item.get("text")))
            for idx, loc in enumerate(locs):
                if not isinstance(loc, str):
                    continue
                msg = (
                    msgs[idx]
                    if idx < len(msgs) and isinstance(msgs[idx], str)
                    else default_message
                )
                yield (loc, msg)
            continue

        # Case 3: Dataclasses with .location / .text
        locs = _as_list(getattr(item, "location", None))
        if locs is not None:
            msgs = _as_list(getattr(item, "text", None))
            loc_list = list(
                locs
                if isinstance(locs, Sequence) and not isinstance(locs, str)
                else [locs]
            )
            msg_list = (
                list(msgs)
                if isinstance(msgs, Sequence) and not isinstance(msgs, str)
                else ([] if msgs is None else [str(msgs)])
            )
            for idx, loc in enumerate(loc_list):
                if not isinstance(loc, str):
                    continue
                msg = msg_list[idx] if idx < len(msg_list) else default_message
                yield (loc, msg)
            continue

        # Fallback: ignore unknown shapes


def _as_list(x: Any) -> list[Any]:
    if x is None:
        return []
    if isinstance(x, list):
        return x
    if isinstance(x, tuple):
        return list(x)
    return [x]


__all__ = [
    "to_marshmallow",
]
