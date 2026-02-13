import dataclasses
import re
import types
from pathlib import Path

import pytest

from pathbridge import translate_location
from pathbridge.cli import CliError, _parse_overrides, main


def test_compile_command_generates_package_with_compiled_rules(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fixtures_dir = tmp_path / "fixtures"
    fixtures_dir.mkdir()
    (fixtures_dir / "__init__.py").write_text("", encoding="utf-8")
    (fixtures_dir / "sample.py").write_text(
        "\n".join(
            [
                "import dataclasses",
                "",
                "@dataclasses.dataclass",
                "class Facade:",
                "    name: str",
                "    codes: list[str]",
                "",
                "@dataclasses.dataclass",
                "class RootXml:",
                '    name: str = dataclasses.field(metadata={"name": "Name"})',
                '    codes: list[str] = dataclasses.field(metadata={"name": "Code"})',
                "",
                "    class Meta:",
                '        name = "Root"',
                "",
                "def convert(src: Facade) -> RootXml:",
                "    return RootXml(name=src.name, codes=src.codes)",
                "",
            ]
        ),
        encoding="utf-8",
    )
    monkeypatch.syspath_prepend(str(tmp_path))

    out_pkg = tmp_path / "generated_rules"
    exit_code = main(
        [
            "compile",
            "--output-package",
            str(out_pkg),
            "--output-module",
            "compiled",
            "--facade-class",
            "fixtures.sample:Facade",
            "--model-module",
            "fixtures.sample",
            "--converter",
            "fixtures.sample:convert",
            "--shape-list-len",
            "2",
            "--rules-root-tag",
            "facade",
        ]
    )

    assert exit_code == 0
    assert (out_pkg / "__init__.py").exists()
    assert (out_pkg / "compiled.py").exists()
    source = (out_pkg / "compiled.py").read_text(encoding="utf-8")
    assert "RAW_RULES" in source
    assert "COMPILED_RULES" in source

    generated = __import__("generated_rules.compiled", fromlist=["*"])
    translated = translate_location(
        "/Root[1]/Code[2]/Code[1]",
        generated.COMPILED_RULES,
    )
    assert translated == "facade/codes[1]"


def test_compile_command_passes_options_in_pipeline_order(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    @dataclasses.dataclass
    class _Facade:
        name: str

    model_module = types.SimpleNamespace()
    call_order: list[str] = []

    def fake_load_object(import_path: str) -> object:
        if import_path == "x:Facade":
            return _Facade
        if import_path == "x:converter":
            return object()
        raise AssertionError(f"Unexpected import path: {import_path}")

    monkeypatch.setattr("pathbridge.cli._load_object", fake_load_object)
    monkeypatch.setattr("pathbridge.cli._load_module", lambda _path: model_module)

    def fake_make_shape(spec: object, *, list_len: int, overrides: object) -> object:
        call_order.append("make_shape")
        assert spec is _Facade
        assert list_len == 3
        assert overrides == {"name": "alice", "count": 2}
        return "shape"

    monkeypatch.setattr("pathbridge.cli.make_shape", fake_make_shape)

    def fake_build_rules(
        *,
        model_module: object,
        converter: object,
        shape: object,
        lift: object,
        root_tag: str,
    ) -> dict[str, str]:
        call_order.append("build_rules")
        assert model_module is not None
        assert converter is not None
        assert shape == "shape"
        assert lift == ["normalize", "pkg.helpers:lift"]
        assert root_tag == "facade"
        return {"B[1]": "a"}

    monkeypatch.setattr("pathbridge.cli.build_rules", fake_build_rules)

    def fake_compile_rules(rules: dict[str, str]) -> list[tuple[re.Pattern[str], str]]:
        call_order.append("compile_rules")
        assert rules == {"B[1]": "a"}
        return [(re.compile("^/B\\[1\\]$", re.IGNORECASE | re.UNICODE), "a")]

    monkeypatch.setattr("pathbridge.cli.compile_rules", fake_compile_rules)

    def fake_write(
        *,
        package_dir: Path,
        module_name: str,
        module_source: str,
    ) -> Path:
        call_order.append("write")
        assert package_dir == tmp_path / "generated"
        assert module_name == "compiled_rules"
        assert "RAW_RULES" in module_source
        assert "COMPILED_RULES" in module_source
        return package_dir / "compiled_rules.py"

    monkeypatch.setattr("pathbridge.cli._write_generated_package", fake_write)

    exit_code = main(
        [
            "compile",
            "--output-package",
            str(tmp_path / "generated"),
            "--facade-class",
            "x:Facade",
            "--model-module",
            "x.models",
            "--converter",
            "x:converter",
            "--shape-list-len",
            "3",
            "--shape-override",
            "name='alice'",
            "--shape-override",
            "count=2",
            "--rules-root-tag",
            "facade",
            "--rules-lift",
            "normalize",
            "--rules-lift",
            "pkg.helpers:lift",
        ]
    )

    assert exit_code == 0
    assert call_order == ["make_shape", "build_rules", "compile_rules", "write"]


def test_parse_overrides_uses_literal_eval_with_string_fallback() -> None:
    parsed = _parse_overrides(["count=2", "name='alice'", "plain=raw-text"])
    assert parsed == {
        "count": 2,
        "name": "alice",
        "plain": "raw-text",
    }

    with pytest.raises(CliError, match="Expected format PATH=VALUE"):
        _parse_overrides(["missing-separator"])
