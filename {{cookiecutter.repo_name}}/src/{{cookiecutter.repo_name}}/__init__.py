# src/{{ cookiecutter.repo_name }}/__init__.py

from importlib import metadata

# pulls package version from pyproject.toml file
__version__ = metadata.version(__name__)
