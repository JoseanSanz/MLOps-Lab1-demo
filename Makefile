install:
	pip install uv &&\
	uv sync

test:
	uv run python -m pytest tests/ -vv --cov=main --cov=mylib #test_*.py

format:	
	uv run black mylib/*.py cli/*.py api/*.py #*.py

lint:
	uv run pylint --disable=R,C --ignore-patterns=test_.*\.py mylib/*.py cli/*.py api/*.py #*.py

#container-lint:
#	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

#deploy:
#	#deploy goes here
		
all: install lint test format
#all: install lint test format deploy
