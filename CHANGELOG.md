# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- New ISO 20022 integration example under `tests/integration/iso20022_payments`.
- New OpenAPI JSON Schema integration example under `tests/integration/openapi_json_schema`.

### Changed

- Renamed HMRC integration package path:
  `tests/integration/uk_main_tax_return` ->
  `tests/integration/hmrc_main_tax_return`.
- Expanded documentation examples into a consolidated "Real-life Examples"
  page covering HMRC MTR, OpenAPI JSON Schema, and ISO 20022 integrations.

## [v0.5.0] - 2026-02-15

### Added

- MkDocs documentation site (`mkdocs.yml`) with dedicated pages for:
  getting started, extras, CLI, API reference, and a real-life HMRC MTR example tutorial.
- Documentation build tooling:
  - `make docs-build` and `make docs-serve`
- Read the Docs build configuration via `.readthedocs.yaml`.


## [v0.4.0] - 2026-02-14

### Added

- New `pathbridge compile` CLI command to generate Python modules with
  `RAW_RULES` and `COMPILED_RULES`.
- `pathbridge compile` supports both import references and file-path
  references for facade/destination/converter inputs.

### Changed

- **BREAKING:** Renamed `pathbridge.extras.trace_converter(...)` keyword-only
  parameters:
  - `model_module` -> `destination_module`
  - `converter` -> `facade_to_destination`
  - `lift` -> `lift_functions`
  - `root_tag` -> `facade_root_tag`
- **BREAKING:** Renamed `pathbridge.extras.build_rules(...)` keyword-only
  parameters:
  - `model_module` -> `destination_module`
  - `converter` -> `facade_to_destination`
  - `shape` -> `facade_shape`
  - `lift` -> `lift_functions`
  - `root_tag` -> `facade_root_tag`
- Removed old keyword aliases for the renamed arguments.
- **BREAKING:** Renamed `pathbridge compile` options:
  - `--model-module` -> `--destination-module`
  - `--converter` -> `--facade-to-destination`
  - `--rules-root-tag` -> `--facade-root-tag`
  - `--rules-lift` -> `--lift-functions`
- **BREAKING:** `--output-package` now expects a dotted package name
  (for example `generated.rules`) instead of a filesystem path.
- Added `--output-dir` for choosing where generated package directories are created.


## [v0.3.0] - 2026-02-14

### Fixed

- make shaper resolve type hints/forward refs and support configurable `type_defaults`
- match reference default placeholders ("", 0, {}) and improve `XmlDate`-like defaults
- fix tracer path generation for nested dataclasses, parent rules, and destination prefixing
- preserve lifted tags for non-scalar helper outputs
- refine nested segment naming

### Added

- Extensive integration testing based on the Main Tax Return (MTR v1.1) Schema used by HMRC.

## [v0.2.0] - 2026-02-13

### Added

- A new `pathbridge.extras` toolkit to make rule generation easier.
- `make_shape(...)` to build a realistic sample facade object.
- `trace_converter(...)` to run a converter function with tracing enabled.
- `build_rules(...)` to generate Destination-to-Facade rules in one call.

### Changed

- README now includes an Extras section with a complete example showing how to:
  - build a sample shape,
  - generate rules from a converter,
  - map both scalar and list-item validation errors.
- Improved `build_rules(...)` docstring to better explain how to use it.

## [v0.1.1] - 2026-02-13

### Fixed

- Fixed bug in the compiler that caused incorrect translation of explicit numeric indices in rules,
  see [#2](https://github.com/pilosus/pathbridge/issues/2)

## [v0.1.0] - 2026-02-06

### Added

- Rules compiler: compiles mapping rules into a form optimized for translation.
- Location translator: translates validator locations to application model paths using compiled rules.
- Marshmallow error formatter: converts translated locations and error messages into a Marshmallow-style error dict

## [v0.0.0] - 2026-02-01

### Added

- Initial project structure

[Unreleased]: https://github.com/pilosus/pathbridge/compare/v0.5.0...HEAD
[v0.5.0]: https://github.com/pilosus/pathbridge/compare/v0.4.0...v0.5.0
[v0.4.0]: https://github.com/pilosus/pathbridge/compare/v0.3.0...v0.4.0
[v0.3.0]: https://github.com/pilosus/pathbridge/compare/v0.2.0...v0.3.0
[v0.2.0]: https://github.com/pilosus/pathbridge/compare/v0.1.0...v0.2.0
[v0.1.1]: https://github.com/pilosus/pathbridge/compare/v0.1.0...v0.1.1
[v0.1.0]: https://github.com/pilosus/pathbridge/compare/v0.0.0...v0.1.0
[v0.0.0]: https://github.com/pilosus/pathbridge/commit/c41ed4282f22ce3cf7c2e0cf2c7a4027efe6ae5b
