import dataclasses
import datetime as dt
import enum

import pytest

from pathbridge.extras.shaper import make_shape


class _Status(enum.Enum):
    OK = "ok"
    FAIL = "fail"


@dataclasses.dataclass
class _Child:
    label: str


@dataclasses.dataclass
class _Model:
    name: str
    count: int
    active: bool
    date: dt.date
    status: _Status
    tags: list[str]
    children: list[_Child]
    meta: dict[str, int]
    maybe: str | None


@dataclasses.dataclass
class _WithOptionalChild:
    value: str
    child: _Child | None


@dataclasses.dataclass
class _ForwardParent:
    child: "_ForwardChild"


@dataclasses.dataclass
class _ForwardChild:
    value: str


class XmlDate:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day


@dataclasses.dataclass
class _WithXmlDate:
    stopped: XmlDate | None


class XmlDateFromString:
    def __init__(self, raw: str) -> None:
        self.raw = raw

    @classmethod
    def from_string(cls, raw: str) -> "XmlDateFromString":
        if raw != "1970-01-01":
            raise ValueError(raw)
        return cls(raw)


@dataclasses.dataclass
class _WithXmlDateFromString:
    stopped: XmlDateFromString | None


def _factory() -> _Model:
    return _Model(
        name="factory",
        count=7,
        active=False,
        date=dt.date(2024, 1, 1),
        status=_Status.FAIL,
        tags=["from-factory"],
        children=[_Child("factory-child")],
        meta={"x": 1},
        maybe=None,
    )


def test_make_shape_builds_truthy_dataclass_graph() -> None:
    shaped = make_shape(_Model, list_len=2)

    assert isinstance(shaped, _Model)
    assert shaped.name == ""
    assert shaped.count == 0
    assert shaped.active is True
    assert isinstance(shaped.date, dt.date)
    assert shaped.status is _Status.OK
    assert shaped.tags == ["", ""]
    assert [c.label for c in shaped.children] == ["", ""]
    assert shaped.meta == {}
    assert shaped.maybe == ""


def test_make_shape_applies_overrides_for_nested_and_indexed_paths() -> None:
    shaped = make_shape(
        _Model,
        list_len=2,
        overrides={
            "name": "alice",
            "children[1].label": "override",
            "meta.k": 99,
        },
    )

    assert shaped.name == "alice"
    assert shaped.children[0].label == ""  # not overridden
    assert shaped.children[1].label == "override"
    assert shaped.meta["k"] == 99


def test_make_shape_with_instance_reuses_same_object() -> None:
    instance = _Model(
        name="n",
        count=1,
        active=True,
        date=dt.date(2024, 1, 1),
        status=_Status.OK,
        tags=["t"],
        children=[_Child("c")],
        meta={"k": 1},
        maybe=None,
    )

    shaped = make_shape(instance, overrides={"children[0].label": "changed"})

    assert shaped is instance
    assert instance.children[0].label == "changed"


def test_make_shape_with_factory_calls_factory() -> None:
    shaped = make_shape(_factory)

    assert shaped.name == "factory"
    assert shaped.children[0].label == "factory-child"


def test_make_shape_populates_pep604_optional_dataclass_fields() -> None:
    shaped = make_shape(_WithOptionalChild)

    assert isinstance(shaped, _WithOptionalChild)
    assert shaped.value == ""
    assert shaped.child is not None
    assert isinstance(shaped.child, _Child)


def test_make_shape_resolves_forward_ref_dataclass_fields() -> None:
    shaped = make_shape(_ForwardParent)

    assert isinstance(shaped, _ForwardParent)
    assert isinstance(shaped.child, _ForwardChild)
    assert shaped.child.value == ""


def test_make_shape_builds_xml_date_like_defaults() -> None:
    shaped = make_shape(_WithXmlDate)

    assert shaped.stopped is not None
    assert isinstance(shaped.stopped, XmlDate)
    assert shaped.stopped.year == 1970


def test_make_shape_builds_xml_date_from_string_defaults() -> None:
    shaped = make_shape(_WithXmlDateFromString)

    assert shaped.stopped is not None
    assert isinstance(shaped.stopped, XmlDateFromString)
    assert shaped.stopped.raw == "1970-01-01"


def test_make_shape_type_defaults_override_builtins() -> None:
    shaped = make_shape(
        _Model,
        list_len=2,
        type_defaults={
            str: "s",
            int: 9,
            _Status: _Status.FAIL,
        },
    )

    assert shaped.name == "s"
    assert shaped.count == 9
    assert shaped.status is _Status.FAIL
    assert shaped.tags == ["s", "s"]
    assert [c.label for c in shaped.children] == ["s", "s"]


def test_make_shape_rejects_unsupported_spec() -> None:
    with pytest.raises(TypeError, match="expects a dataclass class/instance"):
        make_shape(123)
