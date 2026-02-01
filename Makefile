.PHONY: uv deps test test-cov lint format typecheck check clean build publish-test publish

UV_EXTRA_ARGS ?=

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

ruff-check:
	@uv run $(UV_EXTRA_ARGS) ruff check --fix src tests

ruff-format:
	@uv run $(UV_EXTRA_ARGS) ruff format src tests

lint: ruff-format ruff-check

typecheck:
	@uv run $(UV_EXTRA_ARGS) mypy

check: lint typecheck test

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
