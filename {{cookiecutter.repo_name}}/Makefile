env: start_env
	poetry install 

help: pyproject.toml
	poetry run {{ cookiecutter.repo_name }} --help

major: pyproject.toml
	poetry version major

minor: pyproject.toml
	poetry version minor
	
patch: pyproject.toml
	poetry version patch

run: pyproject.toml
	poetry run {{ cookiecutter.repo_name }}

start_env:
	poetry init -q
	poetry add --group dev click dvc ipykernel pytest pytest-cov
	poetry add --group dev coverage -E toml

test: pyproject.toml
	poetry run pytest

test_with_cov: pyproject.toml
	poetry run pytest --cov