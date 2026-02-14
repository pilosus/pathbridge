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


@dataclasses.dataclass
class _DateLike:
    value: str


@dataclasses.dataclass
class _WithDateLike:
    date_like: _DateLike = dataclasses.field(metadata={"name": "DateLike"})


@dataclasses.dataclass
class _FacadeDeclaration:
    individual_declaration: str
    agent_declaration: str


@dataclasses.dataclass
class _FacadeWithDeclaration:
    declaration: _FacadeDeclaration


@dataclasses.dataclass
class _DeclarationDest:
    individual_declaration: str = dataclasses.field(
        metadata={"name": "IndividualDeclaration"}
    )
    agent_declaration: str = dataclasses.field(metadata={"name": "AgentDeclaration"})

    class Meta:
        name = "Declaration"


@dataclasses.dataclass
class _MtrDest:
    declaration: _DeclarationDest = dataclasses.field(metadata={"name": "Declaration"})

    class Meta:
        name = "MTR"


@dataclasses.dataclass
class Sa110:
    underpaid_tax: str = dataclasses.field(metadata={"name": "UnderpaidTax"})


@dataclasses.dataclass
class _MtrWithSa110:
    sa110: Sa110 = dataclasses.field(metadata={"name": "SA110"})

    class Meta:
        name = "MTR"


@dataclasses.dataclass
class _FacadeSa110:
    sa110: str


@dataclasses.dataclass
class _AddressStructure:
    line: list[str] = dataclasses.field(metadata={"name": "Line"})
    short_line: str = dataclasses.field(metadata={"name": "ShortLine"})
    post_code: str = dataclasses.field(metadata={"name": "PostCode"})

    class Meta:
        name = "MTR_SAaddressStructure"


@dataclasses.dataclass
class _NomineeDetailsDest:
    nominee_address: _AddressStructure = dataclasses.field(
        metadata={"name": "NomineeAddress"}
    )

    class Meta:
        name = "NomineeDetails"


@dataclasses.dataclass
class _MtrWithNominee:
    nominee_details: _NomineeDetailsDest = dataclasses.field(
        metadata={"name": "NomineeDetails"}
    )

    class Meta:
        name = "MTR"


@dataclasses.dataclass
class _FacadeNomineeAddress:
    line: list[str]
    short_line: str
    post_code: str


@dataclasses.dataclass
class _FacadeNominee:
    nominee_address: _FacadeNomineeAddress


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


def _to_date_like(value: str) -> _DateLike:
    return _DateLike(value=value)


def _converter_date_like(src: _Facade) -> _WithDateLike:
    return _WithDateLike(date_like=_to_date_like(src.code))


def _converter_declaration(src: _FacadeWithDeclaration) -> _MtrDest:
    return _MtrDest(
        declaration=_DeclarationDest(
            individual_declaration=src.declaration.individual_declaration,
            agent_declaration=src.declaration.agent_declaration,
        )
    )


def _converter_sa110(src: _FacadeSa110) -> _MtrWithSa110:
    return _MtrWithSa110(sa110=Sa110(underpaid_tax=src.sa110))


def _converter_nominee(src: _FacadeNominee) -> _MtrWithNominee:
    return _MtrWithNominee(
        nominee_details=_NomineeDetailsDest(
            nominee_address=_AddressStructure(
                line=src.nominee_address.line,
                short_line=src.nominee_address.short_line,
                post_code=src.nominee_address.post_code,
            )
        )
    )


def test_trace_converter_records_scalar_and_nested_paths() -> None:
    model_module = types.SimpleNamespace(Outer=_OuterDest, Inner=_InnerDest)

    with trace_converter(
        destination_module=model_module, facade_to_destination=_converter_plain
    ) as run:
        result, rules = run(_Facade(name="alice", code="abc", color_name="RED"))

    assert isinstance(result, _OuterDest)
    assert rules == {
        "OuterXml[1]/NameXml[1]": "root/name",
        "OuterXml[1]/InnerXml[1]/CodeXml[1]": "root/code",
    }


def test_build_rules_matches_trace_converter_output() -> None:
    model_module = types.SimpleNamespace(Outer=_OuterDest, Inner=_InnerDest)
    shape = _Facade(name="bob", code="xyz", color_name="RED")

    via_helper = build_rules(
        destination_module=model_module,
        facade_to_destination=_converter_plain,
        facade_shape=shape,
    )
    with trace_converter(
        destination_module=model_module, facade_to_destination=_converter_plain
    ) as run:
        _result, via_context = run(shape)

    assert via_helper == via_context


def test_trace_converter_lift_preserves_source_path_and_restores_function() -> None:
    model_module = types.SimpleNamespace(Outer=_OuterDest, Inner=_InnerDest)
    original = _normalize

    with trace_converter(
        destination_module=model_module,
        facade_to_destination=_converter_with_lift,
        lift_functions=("_normalize",),
    ) as run:
        _result, rules = run(_Facade(name="alice", code="  abc  ", color_name="RED"))

    assert rules["OuterXml[1]/InnerXml[1]/CodeXml[1]"] == "root/code"
    assert _normalize is original


def test_trace_converter_handles_enum_getitem_with_tagged_key() -> None:
    model_module = types.SimpleNamespace(EnumDest=_EnumDest)

    with trace_converter(
        destination_module=model_module,
        facade_to_destination=_converter_enum_lookup,
    ) as run:
        result, rules = run(_Facade(name="alice", code="abc", color_name="RED"))

    assert result.color is _Color.RED
    assert rules == {"_EnumDest[1]/color[1]": "root/color_name"}


def test_trace_converter_lift_preserves_path_for_non_scalar_outputs() -> None:
    model_module = types.SimpleNamespace(WithDateLike=_WithDateLike, DateLike=_DateLike)
    with trace_converter(
        destination_module=model_module,
        facade_to_destination=_converter_date_like,
        lift_functions=("_to_date_like",),
    ) as run:
        _result, rules = run(_Facade(name="alice", code="abc", color_name="RED"))

    assert rules == {"_WithDateLike[1]/DateLike[1]": "root/code"}


def test_trace_converter_destination_prefix_and_parent_paths() -> None:
    model_module = types.SimpleNamespace(MTR=_MtrDest, Declaration=_DeclarationDest)
    facade = _FacadeWithDeclaration(
        declaration=_FacadeDeclaration(
            individual_declaration="yes",
            agent_declaration="no",
        )
    )

    rules = build_rules(
        destination_module=model_module,
        facade_to_destination=_converter_declaration,
        facade_shape=facade,
        facade_root_tag="mtr",
        destination_prefix="MTR",
    )

    assert rules == {
        "MTR:MTR[1]/MTR:Declaration[1]": "mtr/declaration",
        "MTR:MTR[1]/MTR:Declaration[1]/MTR:IndividualDeclaration[1]": "mtr/declaration/individual_declaration",
        "MTR:MTR[1]/MTR:Declaration[1]/MTR:AgentDeclaration[1]": "mtr/declaration/agent_declaration",
    }


def test_trace_converter_prefers_child_class_name_over_parent_field_metadata() -> None:
    model_module = types.SimpleNamespace(MTR=_MtrWithSa110, Sa110=Sa110)
    rules = build_rules(
        destination_module=model_module,
        facade_to_destination=_converter_sa110,
        facade_shape=_FacadeSa110(sa110="x"),
        facade_root_tag="mtr",
        destination_prefix="MTR",
    )

    assert "MTR:MTR[1]/MTR:Sa110[1]/MTR:UnderpaidTax[1]" in rules
    assert "MTR:MTR[1]/MTR:SA110[1]/MTR:UnderpaidTax[1]" not in rules
    assert rules["MTR:MTR[1]/MTR:Sa110[1]/MTR:UnderpaidTax[1]"] == "mtr/sa110"


def test_trace_converter_prefers_field_name_for_reused_structure_types() -> None:
    model_module = types.SimpleNamespace(
        MTR=_MtrWithNominee,
        Nominee=_NomineeDetailsDest,
        Address=_AddressStructure,
    )
    facade = _FacadeNominee(
        nominee_address=_FacadeNomineeAddress(
            line=["addr line 1"],
            short_line="short",
            post_code="AA1 1AA",
        )
    )
    rules = build_rules(
        destination_module=model_module,
        facade_to_destination=_converter_nominee,
        facade_shape=facade,
        facade_root_tag="mtr",
        destination_prefix="MTR",
    )

    assert (
        "MTR:MTR[1]/MTR:NomineeDetails[1]/MTR:NomineeAddress[1]/MTR:Line[1]/MTR:Line[1]"
        in rules
    )
    assert (
        "MTR:MTR[1]/MTR:NomineeDetails[1]/MTR:MTR_SAaddressStructure[1]/MTR:Line[1]/MTR:Line[1]"
        not in rules
    )
