# Project boilerplate

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Boilerplate I use for projects at any maturity level.

# Background

> Description to be added.

## Install

`python==3.10.12` and `cookiecutter==2.2.3` are prerequesites to work with this template.

## Usage

Open your CLI, navigate to the directory where you want the project located and run:

```
cookiecutter https://github.com/mwtmurphy/project-boilerplate
```

You will be prompted for information on the project. After completing these questions, your directory will be created with the following:

- Makefile: shortcut commands to run and test code.
- Documentation: template documentation for questions associated with the project lifecycle (based on CRISP-DM).
- Environment management: `poetry` for managing versioning, python and package dependencies.
- Notebook directory: exploratory-phase work (using jupyter).
- Data directory: exploratory-phase data (if not using remote storage).
- Source directory: production code to be deployed.

## Acknowledgements

Inspired by:
- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) (last accessed 2023-07-29).
- [Hypermodern Python](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769) (last accessed 2023-07-29).
- [CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/) (last accessed 2023-07-29).
