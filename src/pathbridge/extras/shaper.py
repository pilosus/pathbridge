from __future__ import annotations

import contextlib
import dataclasses
import datetime as dt
import inspect
import sys
import types
import typing as t
from decimal import Decimal
from enum import Enum
from uuid import UUID

T = t.TypeVar("T")
_NO_DEFAULT = object()
TypeDefaultMapping = dict[t.Any, t.Any | t.Callable[[], t.Any]]

DEFAULT_TYPE_DEFAULTS: TypeDefaultMapping = {
    str: "",
    int: 0,
    float: 0.0,
    bool: True,
    Decimal: Decimal("0"),
    dt.date: dt.date(1970, 1, 1),
    dt.datetime: dt.datetime(1970, 1, 1),
    UUID: UUID(int=0),
}

#
# Public API
#


def make_shape(
    spec: type[T] | T | t.Callable[[], T],
    *,
    list_len: int = 1,
    overrides: dict[str, t.Any] | None = None,
    type_defaults: TypeDefaultMapping | None = None,
) -> T:
    """
    Construct a 'truthy' instance for the given facade class/instance/factory.

    - spec: dataclass class, an instance (will be cloned shallowly), or a zero-arg factory
    - list_len: default length for list fields
    - overrides: dotted-path -> value to force (supports [index])
    - type_defaults: optional mapping `{type: default_or_factory}` to override
      built-in scalar defaults.

    Heuristics:
      - dataclasses: recursively instantiate with non-empty defaults
      - Optional[T]: pick T with a non-empty value
      - enums: pick first member
      - str: ""; int: 0; Decimal: 0; bool: True; date: 1970-01-01
      - lists: [truthy(T) for _ in range(list_len)]
    """
    resolved_type_defaults: TypeDefaultMapping = dict(DEFAULT_TYPE_DEFAULTS)
    if type_defaults:
        resolved_type_defaults.update(type_defaults)

    if inspect.isclass(spec):
        if dataclasses.is_dataclass(spec):
            base = _shape_dataclass(
                t.cast(type[T], spec),
                list_len=list_len,
                overrides=overrides,
                seen=set(),
                type_defaults=resolved_type_defaults,
            )
        else:
            raise TypeError(
                "make_shape expects a dataclass class/instance or a zero-arg factory"
            )
    elif dataclasses.is_dataclass(spec):
        # already an instance: (re)apply overrides and return
        base = t.cast(T, spec)
        if overrides:
            _apply_overrides(base, overrides)
    elif callable(spec):
        base = spec()
    else:
        raise TypeError(
            "make_shape expects a dataclass class/instance or a zero-arg factory"
        )
    return base


#
# Helpers
#


def _is_dataclass_type(tp: t.Any) -> t.TypeGuard[type[t.Any]]:
    return inspect.isclass(tp) and dataclasses.is_dataclass(tp)


def _dataclass_fields(cls: type[t.Any]) -> tuple[dataclasses.Field[t.Any], ...]:
    return dataclasses.fields(cls)


def _strip_annotated(tp: t.Any) -> t.Any:
    origin = t.get_origin(tp)
    if origin is t.Annotated:
        args = t.get_args(tp)
        if args:
            return args[0]
    return tp


def _resolve_type_hints(cls: type[t.Any]) -> dict[str, t.Any]:
    module = sys.modules.get(cls.__module__)
    module_ns: dict[str, t.Any] = vars(module).copy() if module is not None else {}
    try:
        return t.get_type_hints(
            cls,
            globalns=module_ns,
            localns=module_ns,
            include_extras=True,
        )
    except Exception:
        return {f.name: f.type for f in _dataclass_fields(cls)}


def _default_for_custom_scalar(origin: t.Any) -> t.Any:
    if not inspect.isclass(origin):
        return _NO_DEFAULT

    cls_name = origin.__name__

    # Factory methods are often the safest constructor path for xsdata wrappers.
    from_string = getattr(origin, "from_string", None)
    if callable(from_string):
        for literal in ("1970-01-01", "1970-01-01T00:00:00", "00:00:00"):
            with contextlib.suppress(Exception):
                return from_string(literal)

    from_date = getattr(origin, "from_date", None)
    if callable(from_date):
        with contextlib.suppress(Exception):
            return from_date(dt.date(1970, 1, 1))

    from_datetime = getattr(origin, "from_datetime", None)
    if callable(from_datetime):
        with contextlib.suppress(Exception):
            return from_datetime(dt.datetime(1970, 1, 1))

    # Common constructor style used by xsdata scalar date/time wrappers.
    if cls_name in {"XmlDate", "XmlDateTime", "XmlTime"} or cls_name.startswith("Xml"):
        for args in (
            (),
            (1970, 1, 1),
            (1970, 1, 1, 0, 0, 0),
            (0, 0, 0),
        ):
            with contextlib.suppress(Exception):
                return origin(*args)

    return _NO_DEFAULT


def _mapping_default(
    tp: t.Any,
    origin: t.Any,
    type_defaults: TypeDefaultMapping,
) -> t.Any:
    for key in (tp, origin):
        if key in type_defaults:
            configured = type_defaults[key]
            return configured() if callable(configured) else configured
    return _NO_DEFAULT


def _is_optional(tp: t.Any) -> tuple[bool, t.Any]:
    """Return (is_optional, inner_type)."""
    tp = _strip_annotated(tp)
    origin = t.get_origin(tp)
    if origin in (t.Union, types.UnionType):  # Optional[T] is Union[T, NoneType]
        args = [a for a in t.get_args(tp) if a is not type(None)]
        if args:
            return True, args[0]
    return False, tp


def _is_list(tp: t.Any) -> tuple[bool, t.Any]:
    tp = _strip_annotated(tp)
    origin = t.get_origin(tp)
    if origin in (list, list):
        args = t.get_args(tp)
        return True, (args[0] if args else t.Any)
    return False, tp


def _is_dict(tp: t.Any) -> tuple[bool, t.Any, t.Any]:
    tp = _strip_annotated(tp)
    origin = t.get_origin(tp)
    if origin in (dict, dict):
        args = t.get_args(tp)
        key_t = args[0] if args else t.Any
        val_t = args[1] if len(args) > 1 else t.Any
        return True, key_t, val_t
    return False, tp, tp


def _safe_first_enum(enum_cls: type[Enum]) -> Enum:
    try:
        return next(iter(enum_cls))
    except StopIteration:
        raise ValueError(f"Enum {enum_cls!r} has no members") from None


def _default_for_type(tp: t.Any) -> t.Any:
    """Produce a non-empty, truthy default for a scalar-ish type."""
    return _default_for_type_with_mapping(tp, DEFAULT_TYPE_DEFAULTS)


def _default_for_type_with_mapping(
    tp: t.Any,
    type_defaults: TypeDefaultMapping,
) -> t.Any:
    """Produce a default scalar value using built-ins and user overrides."""
    tp = _strip_annotated(tp)
    origin = t.get_origin(tp) or tp

    mapped = _mapping_default(tp, origin, type_defaults)
    if mapped is not _NO_DEFAULT:
        return mapped

    if inspect.isclass(origin) and issubclass(origin, Enum):
        return _safe_first_enum(origin)
    custom_default = _default_for_custom_scalar(origin)
    if custom_default is not _NO_DEFAULT:
        return custom_default
    return 0


def _apply_overrides(obj: t.Any, overrides: dict[str, t.Any]) -> t.Any:
    """
    Apply dotted-path overrides like:
      "foo.bar[2].baz": 42
    Works with dataclasses, lists, and dicts.
    """
    for path, value in overrides.items():
        parts = [p for p in path.split(".") if p]
        target = obj
        for i, token in enumerate(parts):
            # handle [idx] suffix
            name, idx = token, None
            if "[" in token and token.endswith("]"):
                name, idx = (
                    token[: token.index("[")],
                    int(token[token.index("[") + 1 : -1]),
                )

            if i == len(parts) - 1:
                # set leaf
                if idx is None:
                    if dataclasses.is_dataclass(target):
                        setattr(target, name, value)
                    elif isinstance(target, dict):
                        target[name] = value
                    else:
                        setattr(target, name, value)
                else:
                    seq = getattr(target, name)
                    seq[idx] = value
                break

            # descend
            if dataclasses.is_dataclass(target):
                target = getattr(target, name)
            elif isinstance(target, dict):
                target = target[name]
            else:
                target = getattr(target, name)

            if idx is not None:
                target = target[idx]
    return obj


def _shape_for_type(
    tp: t.Any,
    *,
    list_len: int,
    seen: set[type],
    type_defaults: TypeDefaultMapping,
) -> t.Any:
    tp = _strip_annotated(tp)
    is_opt, inner = _is_optional(tp)
    if is_opt:
        tp = inner

    is_list, elem_t = _is_list(tp)
    if is_list:
        return [
            _shape_for_type(
                elem_t,
                list_len=list_len,
                seen=seen,
                type_defaults=type_defaults,
            )
            for _ in range(list_len)
        ]

    is_dict, _key_t, _val_t = _is_dict(tp)
    if is_dict:
        return {}

    origin = t.get_origin(tp)
    if origin in (t.Union, types.UnionType):
        args = t.get_args(tp)
        if args:
            return _shape_for_type(
                args[0],
                list_len=list_len,
                seen=seen,
                type_defaults=type_defaults,
            )

    resolved = origin or tp
    if _is_dataclass_type(resolved):
        return _shape_dataclass(
            resolved,
            list_len=list_len,
            overrides=None,
            seen=seen,
            type_defaults=type_defaults,
        )
    return _default_for_type_with_mapping(resolved, type_defaults)


def _shape_dataclass(
    cls: type[T],
    *,
    list_len: int,
    overrides: dict[str, t.Any] | None,
    seen: set[type],
    type_defaults: TypeDefaultMapping,
) -> T:
    if cls in seen:
        # stop infinite recursion; build minimal
        minimal_kwargs: dict[str, t.Any] = {}
        for f in _dataclass_fields(cls):
            minimal_kwargs[f.name] = None
        return cls(**minimal_kwargs)
    seen.add(cls)

    try:
        type_hints = _resolve_type_hints(cls)
        kwargs: dict[str, t.Any] = {}
        for f in _dataclass_fields(cls):
            field_type = type_hints.get(f.name, f.type)
            kwargs[f.name] = _shape_for_type(
                field_type,
                list_len=list_len,
                seen=seen,
                type_defaults=type_defaults,
            )

        inst = cls(**kwargs)
        if overrides:
            _apply_overrides(inst, overrides)
        return inst
    finally:
        seen.remove(cls)
