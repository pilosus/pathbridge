.PHONY: uv deps test test-cov test-matrix-setup test-matrix lint format typecheck docs-build docs-serve check ci clean build publish-test publish

UV_EXTRA_ARGS ?=
PY_MATRIX ?= 3.10 3.11 3.12 3.13 3.14

uv:
	@which uv >/dev/null 2>&1 || { \
		echo "uv not installed"; \
		exit 1;\
	}

deps: uv
	@uv sync --all-extras

test:
	@uv run $(UV_EXTRA_ARGS) pytest -vvv --rootdir tests .

test-cov:
	@uv run $(UV_EXTRA_ARGS) pytest --cov=pathbridge --cov-report=term-missing --cov-report=html --rootdir tests .

test-matrix-setup: uv
	@uv python install $(PY_MATRIX)

test-matrix: test-matrix-setup
	@set -e; \
	for py in $(PY_MATRIX); do \
		echo "==> Running tests on Python $$py"; \
		uv sync --python $$py --all-extras; \
		uv run --python $$py $(UV_EXTRA_ARGS) pytest -vvv --rootdir tests .; \
	done

ruff-check:
	@uv run $(UV_EXTRA_ARGS) ruff check --fix src tests

ruff-format:
	@uv run $(UV_EXTRA_ARGS) ruff format src tests

lint: ruff-format ruff-check

typecheck:
	@uv run $(UV_EXTRA_ARGS) mypy

docs-build:
	@uv run --extra docs $(UV_EXTRA_ARGS) mkdocs build --strict

docs-serve:
	@uv run --extra docs $(UV_EXTRA_ARGS) mkdocs serve

check: lint typecheck test docs-build

ci: lint typecheck test-matrix

clean:
	rm -rf build/ dist/ *.egg-info/ src/*.egg-info/
	rm -rf .pytest_cache/ .mypy_cache/ .ruff_cache/
	rm -rf htmlcov/ .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +

build: clean
	@uv build

publish-test: build
	@uv publish --index testpypi

publish: build
	@uv publish

all: deps check
