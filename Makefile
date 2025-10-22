install:
	pip install uv &&\
	uv sync

test:
	uv run python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	uv run black *.py mylib/*.py

lint:
	uv run pylint --disable=R,C --ignore-patterns=test_.*\.py *.py mylib/*.py

#container-lint:
#	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

#deploy:
#	#deploy goes here
		
all: install lint test format
#all: install lint test format deploy
