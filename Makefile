env: pyproject.toml
	poetry install

test: noxfile.py
	nox