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

    output_dir = tmp_path / "out"
    exit_code = main(
        [
            "compile",
            "--output-dir",
            str(output_dir),
            "--output-package",
            "generated.rules",
            "--output-module",
            "compiled",
            "--facade-class",
            "fixtures.sample:Facade",
            "--destination-module",
            "fixtures.sample",
            "--facade-to-destination",
            "fixtures.sample:convert",
            "--shape-list-len",
            "2",
            "--facade-root-tag",
            "facade",
        ]
    )

    assert exit_code == 0
    out_pkg = output_dir / "generated" / "rules"
    assert (output_dir / "generated" / "__init__.py").exists()
    assert (out_pkg / "__init__.py").exists()
    assert (out_pkg / "compiled.py").exists()
    source = (out_pkg / "compiled.py").read_text(encoding="utf-8")
    assert "RAW_RULES" in source
    assert "COMPILED_RULES" in source

    monkeypatch.syspath_prepend(str(output_dir))
    generated = __import__("generated.rules.compiled", fromlist=["*"])
    translated = translate_location(
        "/Root[1]/Code[2]/Code[1]",
        generated.COMPILED_RULES,
    )
    assert translated == "facade/codes[1]"


def test_compile_command_accepts_file_path_references(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fixture_file = tmp_path / "sample_module.py"
    fixture_file.write_text(
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

    output_dir = tmp_path / "out"
    exit_code = main(
        [
            "compile",
            "--output-dir",
            str(output_dir),
            "--output-package",
            "generated.rules",
            "--output-module",
            "compiled",
            "--facade-class",
            f"{fixture_file}:Facade",
            "--destination-module",
            str(fixture_file),
            "--facade-to-destination",
            f"{fixture_file}:convert",
            "--shape-list-len",
            "2",
            "--facade-root-tag",
            "facade",
        ]
    )

    assert exit_code == 0

    monkeypatch.syspath_prepend(str(output_dir))
    generated = __import__("generated.rules.compiled", fromlist=["*"])
    translated = translate_location(
        "/Root[1]/Code[2]/Code[1]",
        generated.COMPILED_RULES,
    )
    assert translated == "facade/codes[1]"


def test_compile_command_file_paths_share_package_module_identity(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pkg_dir = tmp_path / "pkg"
    pkg_dir.mkdir()
    (pkg_dir / "__init__.py").write_text("", encoding="utf-8")
    (pkg_dir / "facade.py").write_text(
        "\n".join(
            [
                "import dataclasses",
                "",
                "@dataclasses.dataclass",
                "class Facade:",
                "    name: str",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (pkg_dir / "destination.py").write_text(
        "\n".join(
            [
                "import dataclasses",
                "",
                "@dataclasses.dataclass",
                "class RootXml:",
                '    name: str = dataclasses.field(metadata={"name": "Name"})',
                "",
                "    class Meta:",
                '        name = "Root"',
                "",
            ]
        ),
        encoding="utf-8",
    )
    (pkg_dir / "converter.py").write_text(
        "\n".join(
            [
                "import pkg.destination as d",
                "import pkg.facade as f",
                "",
                "def convert(src: f.Facade) -> d.RootXml:",
                "    return d.RootXml(name=src.name)",
                "",
            ]
        ),
        encoding="utf-8",
    )

    output_dir = tmp_path / "out"
    exit_code = main(
        [
            "compile",
            "--output-dir",
            str(output_dir),
            "--output-package",
            "generated.rules",
            "--output-module",
            "compiled",
            "--facade-class",
            f"{pkg_dir / 'facade.py'}:Facade",
            "--destination-module",
            str(pkg_dir / "destination.py"),
            "--facade-to-destination",
            f"{pkg_dir / 'converter.py'}:convert",
            "--shape-list-len",
            "1",
            "--facade-root-tag",
            "facade",
        ]
    )

    assert exit_code == 0

    monkeypatch.syspath_prepend(str(output_dir))
    generated = __import__("generated.rules.compiled", fromlist=["*"])
    assert generated.RAW_RULES
    translated = translate_location("/Root[1]/Name[1]", generated.COMPILED_RULES)
    assert translated == "facade/name"


def test_compile_command_passes_options_in_pipeline_order(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    @dataclasses.dataclass
    class _Facade:
        name: str

    destination_module = types.SimpleNamespace()
    call_order: list[str] = []

    def fake_load_object(import_path: str) -> object:
        if import_path == "x:Facade":
            return _Facade
        if import_path == "x:converter":
            return object()
        raise AssertionError(f"Unexpected import path: {import_path}")

    monkeypatch.setattr("pathbridge.cli._load_object", fake_load_object)
    monkeypatch.setattr("pathbridge.cli._load_module", lambda _path: destination_module)

    def fake_make_shape(spec: object, *, list_len: int, overrides: object) -> object:
        call_order.append("make_shape")
        assert spec is _Facade
        assert list_len == 3
        assert overrides == {"name": "alice", "count": 2}
        return "shape"

    monkeypatch.setattr("pathbridge.cli.make_shape", fake_make_shape)

    def fake_build_rules(
        *,
        destination_module: object,
        facade_to_destination: object,
        facade_shape: object,
        lift_functions: object,
        facade_root_tag: str,
    ) -> dict[str, str]:
        call_order.append("build_rules")
        assert destination_module is not None
        assert facade_to_destination is not None
        assert facade_shape == "shape"
        assert lift_functions == ["normalize", "pkg.helpers:lift"]
        assert facade_root_tag == "facade"
        return {"B[1]": "a"}

    monkeypatch.setattr("pathbridge.cli.build_rules", fake_build_rules)

    def fake_compile_rules(rules: dict[str, str]) -> list[tuple[re.Pattern[str], str]]:
        call_order.append("compile_rules")
        assert rules == {"B[1]": "a"}
        return [(re.compile("^/B\\[1\\]$", re.IGNORECASE | re.UNICODE), "a")]

    monkeypatch.setattr("pathbridge.cli.compile_rules", fake_compile_rules)

    def fake_write(
        *,
        output_dir: Path,
        package_name: str,
        module_name: str,
        module_source: str,
    ) -> Path:
        call_order.append("write")
        assert output_dir == tmp_path / "out"
        assert package_name == "generated.rules"
        assert module_name == "compiled_rules"
        assert "RAW_RULES" in module_source
        assert "COMPILED_RULES" in module_source
        return output_dir / "generated" / "rules" / "compiled_rules.py"

    monkeypatch.setattr("pathbridge.cli._write_generated_package", fake_write)

    exit_code = main(
        [
            "compile",
            "--output-dir",
            str(tmp_path / "out"),
            "--output-package",
            "generated.rules",
            "--facade-class",
            "x:Facade",
            "--destination-module",
            "x.models",
            "--facade-to-destination",
            "x:converter",
            "--shape-list-len",
            "3",
            "--shape-override",
            "name='alice'",
            "--shape-override",
            "count=2",
            "--facade-root-tag",
            "facade",
            "--lift-functions",
            "normalize",
            "--lift-functions",
            "pkg.helpers:lift",
        ]
    )

    assert exit_code == 0
    assert call_order == ["make_shape", "build_rules", "compile_rules", "write"]


def test_compile_command_emit_raw_skips_compile_rules(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    @dataclasses.dataclass
    class _Facade:
        name: str

    monkeypatch.setattr(
        "pathbridge.cli._load_object",
        lambda path: _Facade if path == "x:Facade" else object(),
    )
    monkeypatch.setattr("pathbridge.cli._load_module", lambda _path: object())
    monkeypatch.setattr(
        "pathbridge.cli.make_shape",
        lambda spec, *, list_len, overrides: "shape",
    )
    monkeypatch.setattr(
        "pathbridge.cli.build_rules",
        lambda **_kwargs: {"Root[1]/Name[1]": "facade/name"},
    )

    def fail_compile(_rules: dict[str, str]) -> list[tuple[re.Pattern[str], str]]:
        raise AssertionError("compile_rules must not be called for --emit raw")

    monkeypatch.setattr("pathbridge.cli.compile_rules", fail_compile)

    captured_source: dict[str, str] = {}

    def fake_write(
        *,
        output_dir: Path,
        package_name: str,
        module_name: str,
        module_source: str,
    ) -> Path:
        _ = (output_dir, package_name, module_name)
        captured_source["text"] = module_source
        return tmp_path / "out" / "generated" / "rules" / "compiled_rules.py"

    monkeypatch.setattr("pathbridge.cli._write_generated_package", fake_write)

    exit_code = main(
        [
            "compile",
            "--output-dir",
            str(tmp_path / "out"),
            "--output-package",
            "generated.rules",
            "--facade-class",
            "x:Facade",
            "--destination-module",
            "x.models",
            "--facade-to-destination",
            "x:converter",
            "--emit",
            "raw",
        ]
    )

    assert exit_code == 0
    assert "RAW_RULES" in captured_source["text"]
    assert "COMPILED_RULES" not in captured_source["text"]


def test_compile_command_emit_compiled_omits_raw_rules(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    @dataclasses.dataclass
    class _Facade:
        name: str

    monkeypatch.setattr(
        "pathbridge.cli._load_object",
        lambda path: _Facade if path == "x:Facade" else object(),
    )
    monkeypatch.setattr("pathbridge.cli._load_module", lambda _path: object())
    monkeypatch.setattr(
        "pathbridge.cli.make_shape",
        lambda spec, *, list_len, overrides: "shape",
    )
    monkeypatch.setattr(
        "pathbridge.cli.build_rules",
        lambda **_kwargs: {"Root[1]/Name[1]": "facade/name"},
    )
    monkeypatch.setattr(
        "pathbridge.cli.compile_rules",
        lambda _rules: [
            (re.compile("^/Root\\[1\\]/Name\\[1\\]$", re.IGNORECASE), "facade/name")
        ],
    )

    captured_source: dict[str, str] = {}

    def fake_write(
        *,
        output_dir: Path,
        package_name: str,
        module_name: str,
        module_source: str,
    ) -> Path:
        _ = (output_dir, package_name, module_name)
        captured_source["text"] = module_source
        return tmp_path / "out" / "generated" / "rules" / "compiled_rules.py"

    monkeypatch.setattr("pathbridge.cli._write_generated_package", fake_write)

    exit_code = main(
        [
            "compile",
            "--output-dir",
            str(tmp_path / "out"),
            "--output-package",
            "generated.rules",
            "--facade-class",
            "x:Facade",
            "--destination-module",
            "x.models",
            "--facade-to-destination",
            "x:converter",
            "--emit",
            "compiled",
        ]
    )

    assert exit_code == 0
    assert "COMPILED_RULES" in captured_source["text"]
    assert "RAW_RULES" not in captured_source["text"]


def test_parse_overrides_uses_literal_eval_with_string_fallback() -> None:
    parsed = _parse_overrides(["count=2", "name='alice'", "plain=raw-text"])
    assert parsed == {
        "count": 2,
        "name": "alice",
        "plain": "raw-text",
    }

    with pytest.raises(CliError, match="Expected format PATH=VALUE"):
        _parse_overrides(["missing-separator"])
