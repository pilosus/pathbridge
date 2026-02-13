# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

...

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

[Unreleased]: https://github.com/pilosus/kairos/compare/v0.1.1...HEAD
[v0.1.1]: https://github.com/pilosus/pathbridge/compare/v0.1.0...v0.1.1
[v0.1.0]: https://github.com/pilosus/pathbridge/compare/v0.0.0...v0.1.0
[v0.0.0]: https://github.com/pilosus/pathbridge/commit/c41ed4282f22ce3cf7c2e0cf2c7a4027efe6ae5b
