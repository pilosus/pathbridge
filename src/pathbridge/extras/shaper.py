from __future__ import annotations

import dataclasses
import datetime as dt
import inspect
import types
import typing as t
from decimal import Decimal
from enum import Enum
from uuid import UUID

T = t.TypeVar("T")


def _is_dataclass_type(tp: t.Any) -> t.TypeGuard[type[t.Any]]:
    return inspect.isclass(tp) and dataclasses.is_dataclass(tp)


def _dataclass_fields(cls: type[t.Any]) -> tuple[dataclasses.Field[t.Any], ...]:
    return dataclasses.fields(cls)


def _is_optional(tp: t.Any) -> tuple[bool, t.Any]:
    """Return (is_optional, inner_type)."""
    origin = t.get_origin(tp)
    if origin in (t.Union, types.UnionType):  # Optional[T] is Union[T, NoneType]
        args = [a for a in t.get_args(tp) if a is not type(None)]
        if len(args) == 1:
            return True, args[0]
    return False, tp


def _is_list(tp: t.Any) -> tuple[bool, t.Any]:
    origin = t.get_origin(tp)
    if origin in (list, list):
        args = t.get_args(tp)
        return True, (args[0] if args else t.Any)
    return False, tp


def _is_dict(tp: t.Any) -> tuple[bool, t.Any, t.Any]:
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
    if tp in (str, str, t.Any):
        return "x"
    if tp in (int,):
        return 1
    if tp in (float,):
        return 1.0
    if tp is Decimal:
        return Decimal("1")
    if tp is bool:
        return True
    if tp is dt.date:
        return dt.date.today()
    if tp is dt.datetime:
        return dt.datetime.now()
    if tp is UUID:
        return UUID(int=1)
    return "x"  # generic truthy fallback


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


def _shape_dataclass(
    cls: type[T],
    *,
    list_len: int,
    overrides: dict[str, t.Any] | None,
    seen: set[type],
) -> T:
    if cls in seen:
        # stop infinite recursion; build minimal
        minimal_kwargs: dict[str, t.Any] = {}
        for f in _dataclass_fields(cls):
            minimal_kwargs[f.name] = None
        return cls(**minimal_kwargs)
    seen.add(cls)

    kwargs: dict[str, t.Any] = {}
    for f in _dataclass_fields(cls):
        tp = f.type
        is_opt, inner = _is_optional(tp)
        if is_opt:
            tp = inner

        is_list, elem_t = _is_list(tp)
        if is_list:
            elems: list[t.Any] = []
            for _ in range(list_len):
                if _is_dataclass_type(elem_t):
                    elems.append(
                        _shape_dataclass(
                            elem_t, list_len=list_len, overrides=None, seen=seen
                        )
                    )
                else:
                    # nested optionals, enums, scalars
                    opt2, inner2 = _is_optional(elem_t)
                    if opt2:
                        elem_t = inner2
                    if inspect.isclass(elem_t) and issubclass(elem_t, Enum):
                        elems.append(_safe_first_enum(elem_t))
                    else:
                        elems.append(_default_for_type(elem_t))
            kwargs[f.name] = elems
            continue

        is_dict, key_t, val_t = _is_dict(tp)
        if is_dict:
            # make a tiny dict with one truthy item
            k = "k" if key_t is str else 1
            if _is_dataclass_type(val_t):
                v = _shape_dataclass(
                    val_t, list_len=list_len, overrides=None, seen=seen
                )
            else:
                v = _default_for_type(val_t)
            kwargs[f.name] = {k: v}
            continue

        # nested dataclass
        if _is_dataclass_type(tp):
            kwargs[f.name] = _shape_dataclass(
                tp, list_len=list_len, overrides=None, seen=seen
            )
            continue

        # enums
        if inspect.isclass(tp) and issubclass(tp, Enum):
            kwargs[f.name] = _safe_first_enum(tp)
            continue

        # scalar fallback
        kwargs[f.name] = _default_for_type(tp)

    inst = cls(**kwargs)
    if overrides:
        _apply_overrides(inst, overrides)
    seen.remove(cls)
    return inst


def make_shape(
    spec: type[T] | T | t.Callable[[], T],
    *,
    list_len: int = 1,
    overrides: dict[str, t.Any] | None = None,
) -> T:
    """
    Construct a 'truthy' instance for the given facade class/instance/factory.

    - spec: dataclass class, an instance (will be cloned shallowly), or a zero-arg factory
    - list_len: default length for list fields
    - overrides: dotted-path -> value to force (supports [index])

    Heuristics:
      - dataclasses: recursively instantiate with non-empty defaults
      - Optional[T]: pick T with a non-empty value
      - enums: pick first member
      - str: "x"; int: 1; Decimal: 1; bool: True; date: today
      - lists: [truthy(T) for _ in range(list_len)]
    """
    if inspect.isclass(spec):
        if dataclasses.is_dataclass(spec):
            base = _shape_dataclass(
                t.cast(type[T], spec),
                list_len=list_len,
                overrides=overrides,
                seen=set(),
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
