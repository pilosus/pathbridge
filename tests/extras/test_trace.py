import dataclasses
import enum
import types

from pathbridge.extras.trace import build_rules, trace_converter


def _normalize(value: str) -> str:
    return value.strip().upper()


@dataclasses.dataclass
class _Facade:
    name: str
    code: str
    color_name: str


@dataclasses.dataclass
class _InnerDest:
    code: str = dataclasses.field(metadata={"name": "CodeXml"})


@dataclasses.dataclass
class _OuterDest:
    name: str = dataclasses.field(metadata={"name": "NameXml"})
    inner: _InnerDest = dataclasses.field(metadata={"name": "InnerXml"})

    class Meta:
        name = "OuterXml"


class _Color(enum.Enum):
    RED = "red"
    BLUE = "blue"


@dataclasses.dataclass
class _EnumDest:
    color: _Color


def _converter_plain(src: _Facade) -> _OuterDest:
    return _OuterDest(
        name=src.name,
        inner=_InnerDest(code=src.code),
    )


def _converter_with_lift(src: _Facade) -> _OuterDest:
    return _OuterDest(
        name=src.name,
        inner=_InnerDest(code=_normalize(src.code)),
    )


def _converter_enum_lookup(src: _Facade) -> _EnumDest:
    return _EnumDest(color=_Color[src.color_name])


def test_trace_converter_records_scalar_and_nested_paths() -> None:
    model_module = types.SimpleNamespace(Outer=_OuterDest, Inner=_InnerDest)

    with trace_converter(model_module=model_module, converter=_converter_plain) as run:
        result, rules = run(_Facade(name="alice", code="abc", color_name="RED"))

    assert isinstance(result, _OuterDest)
    assert rules == {
        "OuterXml[1]/NameXml[1]": "root/name",
        "_InnerDest[1]/CodeXml[1]": "root/code",
    }


def test_build_rules_matches_trace_converter_output() -> None:
    model_module = types.SimpleNamespace(Outer=_OuterDest, Inner=_InnerDest)
    shape = _Facade(name="bob", code="xyz", color_name="RED")

    via_helper = build_rules(
        model_module=model_module,
        converter=_converter_plain,
        shape=shape,
    )
    with trace_converter(model_module=model_module, converter=_converter_plain) as run:
        _result, via_context = run(shape)

    assert via_helper == via_context


def test_trace_converter_lift_preserves_source_path_and_restores_function() -> None:
    model_module = types.SimpleNamespace(Outer=_OuterDest, Inner=_InnerDest)
    original = _normalize

    with trace_converter(
        model_module=model_module,
        converter=_converter_with_lift,
        lift=("_normalize",),
    ) as run:
        _result, rules = run(_Facade(name="alice", code="  abc  ", color_name="RED"))

    assert rules["_InnerDest[1]/CodeXml[1]"] == "root/code"
    assert _normalize is original


def test_trace_converter_handles_enum_getitem_with_tagged_key() -> None:
    model_module = types.SimpleNamespace(EnumDest=_EnumDest)

    with trace_converter(
        model_module=model_module,
        converter=_converter_enum_lookup,
    ) as run:
        result, rules = run(_Facade(name="alice", code="abc", color_name="RED"))

    assert result.color is _Color.RED
    assert rules == {}
