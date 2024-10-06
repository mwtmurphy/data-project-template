env:
ifeq ($(wildcard pyproject.toml),)
	@echo "pyproject.toml does not exist, creating poetry files..."
	poetry init -q
	poetry add --group dev click ipykernel pytest pytest-cov
	poetry add --group dev coverage -E toml
else
	@echo "pyproject.toml exists, installing dependencies..."
	poetry install
endif

major: pyproject.toml
	poetry version major

minor: pyproject.toml
	poetry version minor
	
patch: pyproject.toml
	poetry version patch

src_tests: pyproject.toml
	poetry run pytest

src_tests_cov: pyproject.toml
	poetry run pytest --cov