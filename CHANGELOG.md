# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/pilosus/kairos/compare/v0.2.0...HEAD
[v0.2.0]: https://github.com/pilosus/pathbridge/compare/v0.1.0...v0.2.0
[v0.1.1]: https://github.com/pilosus/pathbridge/compare/v0.1.0...v0.1.1
[v0.1.0]: https://github.com/pilosus/pathbridge/compare/v0.0.0...v0.1.0
[v0.0.0]: https://github.com/pilosus/pathbridge/commit/c41ed4282f22ce3cf7c2e0cf2c7a4027efe6ae5b
