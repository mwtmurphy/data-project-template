env: poetry
	poetry install 

major: pyproject.toml
	poetry version major

minor: pyproject.toml
	poetry version minor
	
patch: pyproject.toml
	poetry version patch

poetry_env:
	poetry init -q
	poetry add --group dev click dvc ipykernel pytest pytest-cov
	poetry add --group dev coverage -E toml

src_tests: pyproject.toml
	poetry run pytest

src_tests_cov: pyproject.toml
	poetry run pytest --cov