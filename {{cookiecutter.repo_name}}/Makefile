env: poetry
	poetry install 

major: pyproject.toml
	poetry version major

minor: pyproject.toml
	poetry version minor
	
patch: pyproject.toml
	poetry version patch

poetry:
	poetry init -q
	poetry add --group dev click dvc ipykernel pytest pytest-cov
	poetry add --group dev coverage -E toml

test: pyproject.toml
	poetry run pytest

test_with_cov: pyproject.toml
	poetry run pytest --cov