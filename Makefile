# We use Bash for complex commands and consistency
SHELL := /bin/bash
# We ensure that ~/.local/bin (where uv can be installed) is in the PATH
PATH := $(HOME)/.local/bin:$(PATH)

install:
	@if ! command -v uv &> /dev/null; then \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	fi
	uv sync

test:
	uv run python -m pytest tests/ -vv --cov=mylib --cov=api --cov=cli 

format:	
	uv run black mylib/*.py cli/*.py api/*.py

lint:
	uv run pylint --disable=R,C --ignore-patterns=test_.*\.py mylib/*.py cli/*.py api/*.py 

refactor: format lint

all: install format lint test
