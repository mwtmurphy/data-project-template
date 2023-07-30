env: pyproject.toml
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

test: pyproject.toml
	poetry run pytest

test_with_cov:
	poetry run pytest --cov