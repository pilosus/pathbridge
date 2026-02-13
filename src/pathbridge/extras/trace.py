from __future__ import annotations

import contextlib
import dataclasses
import enum
import inspect
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

    Returns a context manager. Inside it, call the yielded function with a *facade*
    instance (your shape); it returns (result_object, rules_dict).
    """
    return TraceContext(
        model_module=model_module,
        converter=converter,
        lift=tuple(lift or ()),
        root_tag=root_tag,
    )


def build_rules(
    *,
    model_module: t.Any,
    converter: t.Callable[[t.Any], t.Any],
    shape: t.Any,
    lift: t.Iterable[str] | None = None,
    root_tag: str = "root",
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

    Returns:
        Mapping of destination paths to facade paths (`DEST -> FACADE`).
    """
    with trace_converter(
        model_module=model_module, converter=converter, lift=lift, root_tag=root_tag
    ) as run:
        _, rules = run(shape)
        return rules


#
# Internals
#


U = t.TypeVar("U")
InitCallable = t.Callable[..., None]
LiftRecord = tuple[types.ModuleType, str, t.Callable[..., t.Any]]
ParentStack = tuple[tuple[str, int], ...]
CounterKey = tuple[ParentStack, str]


# A minimal tag that carries a source facade path alongside a value.
class Tagged(t.Generic[U]):
    __slots__ = ("value", "path")

    def __init__(self, value: t.Any, path: str) -> None:
        self.value = value
        self.path = path

    def __repr__(self) -> str:
        return f"Tagged({self.value!r}, {self.path})"


def _is_scalar(x: t.Any) -> bool:
    return not dataclasses.is_dataclass(x) and not isinstance(x, (list, tuple, dict))


def _wrap_src(obj: t.Any, path: str) -> t.Any:
    """Wrap a facade object with proxies that yield Tagged leaves."""
    # dataclass -> attribute-proxy
    if dataclasses.is_dataclass(obj):
        return _DataclassProxy(obj, path)
    # list/tuple -> collection of proxies
    if isinstance(obj, (list, tuple)):
        return type(obj)(_wrap_src(v, f"{path}[{i}]") for i, v in enumerate(obj))
    # dict -> proxy each value
    if isinstance(obj, dict):
        return {k: _wrap_src(v, f"{path}/{k}") for k, v in obj.items()}
    # leaf -> Tagged
    return Tagged(obj, path)


class _DataclassProxy:
    """
    Lightweight facade proxy that mirrors a dataclass and returns Tagged leaves.
    """

    __slots__ = ("__obj", "__path")

    def __init__(self, obj: t.Any, path: str) -> None:
        object.__setattr__(self, "_DataclassProxy__obj", obj)
        object.__setattr__(self, "_DataclassProxy__path", path)

    def __getattr__(self, name: str) -> t.Any:
        obj = object.__getattribute__(self, "_DataclassProxy__obj")
        path = object.__getattribute__(self, "_DataclassProxy__path")
        val = getattr(obj, name)
        # Normalize to dotted attr path on facade side
        sub_path = f"{path}/{name}"
        return _wrap_src(val, sub_path)

    # for explicit indexing on proxied lists nested under attributes, users will get
    # real list proxies returned from __getattr__, so normal indexing works.


# Destination path builders (xsdata-friendly but generic)


def _xml_class_name(cls: type) -> str:
    """Try xsdata's Meta.name; otherwise use class name."""
    meta = getattr(cls, "Meta", None)
    return getattr(meta, "name", cls.__name__)


def _xml_field_name(cls: type, py_name: str) -> str:
    """Try xsdata field metadata 'name'; otherwise Python field name."""
    fld = cls.__dataclass_fields__[py_name]  # type: ignore[attr-defined]
    meta = fld.metadata or {}
    return t.cast(str, meta.get("name", py_name))


class _TracerState:
    def __init__(self, root_tag: str) -> None:
        self.root_tag = root_tag
        # stack of (xml_element_name, index)
        self.stack: list[tuple[str, int]] = []
        # per-parent-element counters to assign 1-based [n] to siblings
        self.counters: dict[CounterKey, int] = {}
        # collected rules: DEST -> FACADE
        self.rules: RawRulesMapT = {}

    # ---- stack management ----

    def push(self, name: str) -> int:
        parent = tuple(self.stack)
        key = (parent, name)
        idx = self.counters.get(key, 0) + 1  # 1-based for DEST
        self.counters[key] = idx
        self.stack.append((name, idx))
        return idx

    def pop(self) -> None:
        self.stack.pop()

    # ---- path formatting ----

    def current_prefix(self) -> str:
        # e.g., "MTR:MTR[1]/MTR:Sa103S[2]" without namespaces, generic:
        if not self.stack:
            return _escape_step(self.root_tag) + "[1]"
        return "/".join(f"{_escape_step(name)}[{idx}]" for (name, idx) in self.stack)

    def add_leaf(self, field_xml_name: str, src_path: str) -> None:
        # Build full destination path including the leaf element
        dest = self.current_prefix() + f"/{_escape_step(field_xml_name)}[1]"
        # rules map DEST -> FACADE (src_path is in facade token format)
        # Keep the last writer if duplicates occur (first-win/last-win both OK)
        self.rules[dest] = src_path


def _escape_step(name: str) -> str:
    """Escape a step name safely for later regex compilation (kept literal here)."""
    # We keep it as-is; compiler will escape and normalize.
    return name


def _record_scalar_field(
    state: _TracerState, cls: type, field_name: str, value: t.Any
) -> None:
    if isinstance(value, Tagged):
        xml_field = _xml_field_name(cls, field_name)
        state.add_leaf(xml_field, value.path)


def _record_list_field(
    state: _TracerState, cls: type, field_name: str, value: t.Any
) -> None:
    # If the list elements are Tagged scalars, record per index.
    if isinstance(value, (list, tuple)):
        for _, elem in enumerate(value):
            if isinstance(elem, Tagged):
                xml_field = _xml_field_name(cls, field_name)
                # Temporarily push the list item context to compute [i+1]
                state.push(xml_field)
                # Leaf under this item
                state.add_leaf(
                    _xml_field_name(cls, field_name), elem.path
                )  # element name reused
                state.pop()


# Monkey-patch machinery


class TraceContext:
    """
    Context manager that patches destination dataclasses' __init__ and enum lookups,
    and (optionally) lifts helper functions to preserve Tagged values.

    Usage:
        with trace_converter(model_module=..., converter=..., ...) as run:
            result, rules = run(facade_shape)
    """

    def __init__(
        self,
        *,
        model_module: t.Any,
        converter: t.Callable[[t.Any], t.Any],
        lift: tuple[str, ...],
        root_tag: str,
    ) -> None:
        self.model_module = model_module
        self.converter = converter
        self.lift = lift
        self.root_tag = root_tag

        self._orig_inits: dict[type, InitCallable] = {}
        self._patched_classes: list[type] = []
        self._orig_enummeta_getitem: (
            t.Callable[[type[enum.Enum], t.Any], t.Any] | None
        ) = None
        self._lifted: list[LiftRecord] = []
        self._state = _TracerState(root_tag=root_tag)

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

    # ---- core run ----

    def _run(self, facade_root: t.Any) -> tuple[t.Any, RawRulesMapT]:
        # Wrap the facade so reads return Tagged (or proxies)
        proxied = _wrap_src(facade_root, self.root_tag)
        # Execute converter under a fresh state
        self._state = _TracerState(root_tag=self.root_tag)
        result = self.converter(proxied)
        return result, dict(self._state.rules)

    # ---- patch dataclasses ----

    def _iter_destination_classes(self) -> list[type]:
        out: list[type] = []
        for _, obj in vars(self.model_module).items():
            if isinstance(obj, type) and dataclasses.is_dataclass(obj):
                out.append(obj)
        return out

    def _patch_dataclasses(self) -> None:
        for cls in self._iter_destination_classes():
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
                # assign a sibling index for this instance (1-based)
                name = _xml_class_name(__cls)
                self._state.push(name)
                try:
                    # Call the real __init__ first so attributes exist
                    __orig(_self, *args, **kwargs)
                    # Now inspect assigned fields from kwargs by name
                    for f in dataclasses.fields(__cls):
                        if f.name in kwargs:
                            val = kwargs[f.name]
                            if isinstance(val, Tagged):
                                _record_scalar_field(self._state, __cls, f.name, val)
                            elif isinstance(val, (list, tuple)):
                                _record_list_field(self._state, __cls, f.name, val)
                            # nested dataclasses will record deeper leaves on their own in their own init
                finally:
                    self._state.pop()

            type.__setattr__(cls, "__init__", wrapper)
            self._patched_classes.append(cls)

    def _restore_dataclasses(self) -> None:
        with contextlib.suppress(Exception):
            for cls, orig in self._orig_inits.items():
                type.__setattr__(cls, "__init__", orig)

        self._orig_inits.clear()
        self._patched_classes.clear()

    # ---- patch enum meta (unwrap Tagged keys) ----

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
            if isinstance(name, Tagged):
                name = name.value
            getter = self._orig_enummeta_getitem
            if getter is None:
                raise RuntimeError("EnumMeta.__getitem__ patch is not installed")
            return getter(cls, name)

        type.__setattr__(enum.EnumMeta, "__getitem__", patched_getitem)

    def _restore_enum_meta(self) -> None:
        if self._orig_enummeta_getitem is not None:
            type.__setattr__(enum.EnumMeta, "__getitem__", self._orig_enummeta_getitem)
            self._orig_enummeta_getitem = None

    # ---- lift helper functions ----

    def _resolve_lift_target(self, spec: str) -> tuple[types.ModuleType, str] | None:
        """
        Resolve 'name' in converter's globals, or 'pkg.mod:func' fully-qualified.
        Returns (module_object, attribute_name).
        """
        if ":" in spec:
            mod_name, attr = spec.split(":", 1)
            imported_mod = __import__(mod_name, fromlist=[attr])
            return (imported_mod, attr)
        # try converter's globals
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
                # If any arg is Tagged, unwrap the value(s), remember first path
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
                # Re-wrap scalar outputs to keep the path flowing
                if (
                    first_tag_path is not None
                    and not dataclasses.is_dataclass(out)
                    and not isinstance(out, (list, tuple, dict))
                ):
                    return Tagged(out, first_tag_path)
                return out

            setattr(mod, attr, lifted)
            self._lifted.append((mod, attr, t.cast(t.Callable[..., t.Any], orig)))

    def _restore_lift_functions(self) -> None:
        with contextlib.suppress(Exception):
            for mod, attr, orig in self._lifted:
                setattr(mod, attr, orig)

        self._lifted.clear()
