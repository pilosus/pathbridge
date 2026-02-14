Prepare a release for version $ARGUMENTS.

Steps:
1. Update `version` in `pyproject.toml` to the given version (without a `v` prefix).
2. Run `make deps` to sync the lockfile.
3. Update `CHANGELOG.md` with the new version.
4. Run `make check-matrix` to make sure linting and tests pass on the new version.
5. Show the user what changed so they can verify before committing.