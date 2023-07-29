env: pyproject.toml
	conda create -n {{ cookiecutter.pkg_name.replace('_', '-') }} python={{ cookiecutter.python_version }} poetry=1.1.6

tests:
	poetry run python -m unittest discover -s tests -p "test*.py"
