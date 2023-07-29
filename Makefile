env: pyproject.toml
	poetry install

tests:
	poetry run python tests/test_repo_setup.py
