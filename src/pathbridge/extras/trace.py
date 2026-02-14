from __future__ import annotations

import contextlib
import dataclasses
import enum
import inspect
import re
import types
import typing as t

from pathbridge.types import RawRulesMapT

#
# Public API
#


def trace_converter(
    *,
    model_module: t.Any,
    converter: t.Callable[[t.Any], t.Any],
    lift: t.Iterable[str] | None = None,
    root_tag: str = "root",
    destination_prefix: str | None = None,
) -> TraceContext:
    """
    Context manager that enables tracing patches. Yields a callable:
        run(shape) -> (result, rules_dict)

    - model_module: module where destination dataclasses/enums live
    - converter: your converter callable (facade -> destination model)
    - lift: names to 'lift' through (functions that should preserve Tagged)
            Accepts simple names resolvable in converter's globals, or fully
            qualified 'pkg.mod:func' strings.
    - root_tag: starting facade segment, e.g. "mtr"
    - destination_prefix: optional prefix for destination XML path segments,
            e.g. "MTR" to render "MTR:ElementName[1]"

    Returns a context manager. Inside it, call the yielded function with a *facade*
    instance (your shape); it returns (result_object, rules_dict).
    """
    return TraceContext(
        model_module=model_module,
        converter=converter,
        lift=tuple(lift or ()),
        root_tag=root_tag,
        destination_prefix=destination_prefix,
    )


def build_rules(
    *,
    model_module: t.Any,
    converter: t.Callable[[t.Any], t.Any],
    shape: t.Any,
    lift: t.Iterable[str] | None = None,
    root_tag: str = "root",
    destination_prefix: str | None = None,
) -> RawRulesMapT:
    """
    Build a destination-to-facade rules map from one traced conversion run.

    This is a convenience wrapper around `trace_converter(...)`. It patches
    destination dataclasses/enums for the duration of the call, executes
    `converter(shape)`, and captures leaf assignments as
    `{destination_path: facade_path}`.

    Args:
        model_module: Module that contains destination dataclasses/enums used
            by `converter`.
        converter: Callable that converts facade input into destination model
            objects.
        shape: Sample facade object to pass into `converter` while tracing.
        lift: Optional helper function names that should preserve path tags
            (`"name"` or `"pkg.mod:func"`).
        root_tag: Root token used as the facade-path prefix in recorded rules.
        destination_prefix: Optional destination segment prefix
            (e.g. `"MTR"` -> `MTR:Element[1]`).

    Returns:
        Mapping of destination paths to facade paths (`DEST -> FACADE`).
    """
    with trace_converter(
        model_module=model_module,
        converter=converter,
        lift=lift,
        root_tag=root_tag,
        destination_prefix=destination_prefix,
    ) as run:
        _, rules = run(shape)
        return rules


#
# Internals
#


U = t.TypeVar("U")
InitCallable = t.Callable[..., None]
LiftRecord = tuple[types.ModuleType, str, t.Callable[..., t.Any]]
LeafRecord = tuple[list[str], str]
ParentStack = tuple[tuple[str, int], ...]
CounterKey = tuple[ParentStack, str]
NodeKey = tuple[ParentStack, str, str]
TRACER_LEAVES_ATTR = "__tracer_leaves__"


class Tagged(t.Generic[U]):
    __slots__ = ("value", "path")

    def __init__(self, value: t.Any, path: str) -> None:
        self.value = value
        self.path = path

    def __repr__(self) -> str:
        return f"Tagged({self.value!r}, {self.path})"


def _wrap_src(obj: t.Any, path: str) -> t.Any:
    if dataclasses.is_dataclass(obj):
        return _DataclassProxy(obj, path)
    if isinstance(obj, (list, tuple)):
        return type(obj)(_wrap_src(v, f"{path}[{i}]") for i, v in enumerate(obj))
    if isinstance(obj, dict):
        return {k: _wrap_src(v, f"{path}/{k}") for k, v in obj.items()}
    return Tagged(obj, path)


class _DataclassProxy:
    __slots__ = ("__obj", "__path")

    def __init__(self, obj: t.Any, path: str) -> None:
        object.__setattr__(self, "_DataclassProxy__obj", obj)
        object.__setattr__(self, "_DataclassProxy__path", path)

    def __getattr__(self, name: str) -> t.Any:
        obj = object.__getattribute__(self, "_DataclassProxy__obj")
        path = object.__getattribute__(self, "_DataclassProxy__path")
        return _wrap_src(getattr(obj, name), f"{path}/{name}")


def _xml_class_name(cls: type) -> str:
    meta = getattr(cls, "Meta", None)
    return getattr(meta, "name", cls.__name__)


def _xml_field_name(cls: type, py_name: str) -> str:
    fld = cls.__dataclass_fields__[py_name]  # type: ignore[attr-defined]
    meta = fld.metadata or {}
    return t.cast(str, meta.get("name", py_name))


def _escape_step(name: str) -> str:
    return name


def _format_step(name: str, destination_prefix: str | None) -> str:
    escaped = _escape_step(name)
    if destination_prefix:
        return f"{destination_prefix}:{escaped}"
    return escaped


def _normalize_xml_name(name: str) -> str:
    return re.sub(r"\W+", "", name).upper()


def _nested_segment_name(parent_cls: type, field_name: str, child_value: t.Any) -> str:
    field_xml = _xml_field_name(parent_cls, field_name)
    child_xml = _xml_class_name(type(child_value))
    if _normalize_xml_name(field_xml) == _normalize_xml_name(child_xml):
        return child_xml
    return field_xml


def _get_leaves(obj: t.Any) -> list[LeafRecord]:
    leaves = getattr(obj, TRACER_LEAVES_ATTR, None)
    if isinstance(leaves, list):
        return t.cast(list[LeafRecord], leaves)
    return []


def _unwrap_field_value(
    cls: type,
    field_name: str,
    value: t.Any,
) -> tuple[t.Any, list[LeafRecord]]:
    field_xml_name = _xml_field_name(cls, field_name)

    if isinstance(value, Tagged):
        return value.value, [([field_xml_name], value.path)]

    if isinstance(value, (list, tuple)):
        unwrapped_items: list[t.Any] = []
        leaves: list[LeafRecord] = []
        for item in value:
            if isinstance(item, Tagged):
                # Keep two steps to preserve item index in generated destination path.
                leaves.append(([field_xml_name, field_xml_name], item.path))
                unwrapped_items.append(item.value)
            else:
                unwrapped_items.append(item)
        if isinstance(value, tuple):
            return tuple(unwrapped_items), leaves
        return unwrapped_items, leaves

    return value, []


def _split_facade_path(path: str) -> list[str]:
    return [part for part in path.split("/") if part]


def _leaves_to_rules(
    leaves: list[LeafRecord], destination_prefix: str | None
) -> RawRulesMapT:
    rules: RawRulesMapT = {}
    counters: dict[CounterKey, int] = {}
    nodes: dict[NodeKey, int] = {}

    for segments, src_path in leaves:
        if not segments:
            continue

        src_parts = _split_facade_path(src_path)
        stack: list[tuple[str, int]] = []
        rendered_parts: list[str] = []
        for depth, name in enumerate(segments):
            if depth < len(src_parts):
                src_prefix = "/".join(src_parts[: depth + 1])
            else:
                src_prefix = f"{src_path}#d{depth}"

            parent = tuple(stack)
            node_key = (parent, name, src_prefix)
            if node_key in nodes:
                idx = nodes[node_key]
            else:
                counter_key = (parent, name)
                idx = counters.get(counter_key, 0) + 1
                counters[counter_key] = idx
                nodes[node_key] = idx

            stack.append((name, idx))
            rendered_parts.append(f"{_format_step(name, destination_prefix)}[{idx}]")

            # Include intermediate parent path mappings when facade depth exists.
            # Depth 0 is the root object and usually too broad to be useful.
            if depth > 0 and depth < len(src_parts) - 1:
                parent_dest = "/".join(rendered_parts)
                parent_src = "/".join(src_parts[: depth + 1])
                if parent_dest not in rules:
                    rules[parent_dest] = parent_src

        rules["/".join(rendered_parts)] = src_path

    return rules


class TraceContext:
    def __init__(
        self,
        *,
        model_module: t.Any,
        converter: t.Callable[[t.Any], t.Any],
        lift: tuple[str, ...],
        root_tag: str,
        destination_prefix: str | None,
    ) -> None:
        self.model_module = model_module
        self.converter = converter
        self.lift = lift
        self.root_tag = root_tag
        self.destination_prefix = destination_prefix

        self._orig_inits: dict[type, InitCallable] = {}
        self._orig_enummeta_getitem: (
            t.Callable[[type[enum.Enum], t.Any], t.Any] | None
        ) = None
        self._lifted: list[LiftRecord] = []

    def __enter__(self) -> t.Callable[[t.Any], tuple[t.Any, RawRulesMapT]]:
        self._patch_dataclasses()
        self._patch_enum_meta()
        self._patch_lift_functions()
        return self._run

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: types.TracebackType | None,
    ) -> None:
        _ = (exc_type, exc, tb)
        self._restore_lift_functions()
        self._restore_enum_meta()
        self._restore_dataclasses()

    def _run(self, facade_root: t.Any) -> tuple[t.Any, RawRulesMapT]:
        proxied = _wrap_src(facade_root, self.root_tag)
        result = self.converter(proxied)
        if dataclasses.is_dataclass(result):
            return result, _leaves_to_rules(
                _get_leaves(result), self.destination_prefix
            )
        return result, {}

    def _iter_destination_classes(self) -> list[type]:
        out: list[type] = []
        visited: set[type] = set()

        def visit(candidate: type) -> None:
            if candidate in visited:
                return
            visited.add(candidate)
            if dataclasses.is_dataclass(candidate):
                out.append(candidate)
            for _, child in vars(candidate).items():
                if isinstance(child, type):
                    visit(child)

        for _, obj in vars(self.model_module).items():
            if isinstance(obj, type):
                visit(obj)
        return out

    def _patch_dataclasses(self) -> None:
        for cls in self._iter_destination_classes():
            if cls in self._orig_inits:
                continue
            orig_init_obj = vars(cls).get("__init__")
            if not callable(orig_init_obj):
                continue
            orig_init = t.cast(InitCallable, orig_init_obj)
            self._orig_inits[cls] = orig_init

            def wrapper(
                _self: t.Any,
                *args: t.Any,
                __cls: type = cls,
                __orig: InitCallable = orig_init,
                **kwargs: t.Any,
            ) -> None:
                xml_self_name = _xml_class_name(__cls)
                direct_leaves: list[LeafRecord] = []
                kwargs_for_init: dict[str, t.Any] = dict(kwargs)

                for f in dataclasses.fields(__cls):
                    if f.name not in kwargs_for_init:
                        continue
                    raw_value = kwargs_for_init[f.name]
                    unwrapped, leaves = _unwrap_field_value(__cls, f.name, raw_value)
                    kwargs_for_init[f.name] = unwrapped
                    for segments, src_path in leaves:
                        direct_leaves.append(([xml_self_name] + segments, src_path))

                __orig(_self, *args, **kwargs_for_init)

                all_leaves = list(direct_leaves)
                for f in dataclasses.fields(__cls):
                    with contextlib.suppress(Exception):
                        field_value = getattr(_self, f.name)
                        if dataclasses.is_dataclass(field_value):
                            nested_name = _nested_segment_name(
                                __cls, f.name, field_value
                            )
                            for segments, src_path in _get_leaves(field_value):
                                tail = segments[1:] if segments else []
                                all_leaves.append(
                                    ([xml_self_name, nested_name] + tail, src_path)
                                )
                        elif isinstance(field_value, (list, tuple)):
                            for item in field_value:
                                if dataclasses.is_dataclass(item):
                                    nested_name = _nested_segment_name(
                                        __cls, f.name, item
                                    )
                                    for segments, src_path in _get_leaves(item):
                                        tail = segments[1:] if segments else []
                                        all_leaves.append(
                                            (
                                                [xml_self_name, nested_name] + tail,
                                                src_path,
                                            )
                                        )

                setattr(_self, TRACER_LEAVES_ATTR, all_leaves)

            type.__setattr__(cls, "__init__", wrapper)

    def _restore_dataclasses(self) -> None:
        with contextlib.suppress(Exception):
            for cls, orig in self._orig_inits.items():
                type.__setattr__(cls, "__init__", orig)
        self._orig_inits.clear()

    def _patch_enum_meta(self) -> None:
        if self._orig_enummeta_getitem is not None:
            return
        orig_getitem_obj = vars(enum.EnumMeta).get("__getitem__")
        if not callable(orig_getitem_obj):
            return
        self._orig_enummeta_getitem = t.cast(
            t.Callable[[type[enum.Enum], t.Any], t.Any], orig_getitem_obj
        )

        def patched_getitem(cls: type[enum.Enum], name: t.Any) -> t.Any:
            getter = self._orig_enummeta_getitem
            if getter is None:
                raise RuntimeError("EnumMeta.__getitem__ patch is not installed")

            if isinstance(name, Tagged):
                member = getter(cls, name.value)
                return Tagged(member, name.path)

            return getter(cls, name)

        type.__setattr__(enum.EnumMeta, "__getitem__", patched_getitem)

    def _restore_enum_meta(self) -> None:
        if self._orig_enummeta_getitem is not None:
            type.__setattr__(enum.EnumMeta, "__getitem__", self._orig_enummeta_getitem)
            self._orig_enummeta_getitem = None

    def _resolve_lift_target(self, spec: str) -> tuple[types.ModuleType, str] | None:
        if ":" in spec:
            mod_name, attr = spec.split(":", 1)
            imported_mod = __import__(mod_name, fromlist=[attr])
            return (imported_mod, attr)

        converter_mod = inspect.getmodule(self.converter)
        if converter_mod and hasattr(converter_mod, spec):
            return (converter_mod, spec)
        return None

    def _patch_lift_functions(self) -> None:
        for name in self.lift:
            resolved = self._resolve_lift_target(name)
            if not resolved:
                continue
            mod, attr = resolved
            orig = getattr(mod, attr)

            def lifted(
                *args: t.Any, __orig: t.Callable[..., t.Any] = orig, **kwargs: t.Any
            ) -> t.Any:
                first_tag_path: str | None = None

                def unwrap(x: t.Any) -> t.Any:
                    nonlocal first_tag_path
                    if isinstance(x, Tagged):
                        first_tag_path = first_tag_path or x.path
                        return x.value
                    return x

                ua = tuple(unwrap(a) for a in args)
                uk = {k: unwrap(v) for k, v in kwargs.items()}
                out = __orig(*ua, **uk)
                if first_tag_path is not None:
                    if isinstance(out, Tagged):
                        return out
                    return Tagged(out, first_tag_path)
                return out

            setattr(mod, attr, lifted)
            self._lifted.append((mod, attr, t.cast(t.Callable[..., t.Any], orig)))

    def _restore_lift_functions(self) -> None:
        with contextlib.suppress(Exception):
            for mod, attr, orig in self._lifted:
                setattr(mod, attr, orig)
        self._lifted.clear()
