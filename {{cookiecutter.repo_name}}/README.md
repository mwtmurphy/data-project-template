# {{ cookiecutter.project_title }}
 
{{ cookiecutter.project_description }}.

# General Use

## Project Layout

    ├── LICENSE
    │
    ├── .env               <- Environment variables used in project.
    │
    ├── Makefile           <- Makefile with shortcut commands (e.g. environment setup, testing).
    │
    ├── README.md          <- The top-level README for users/developers of this project.
    │
    ├── data
    │   ├── interim        <- Intermediate data that has been preprocessed/transformed.
    │   ├── processed      <- The final, canonical data sets for modelling.
    │   └── raw            <- Sample data for which experiments can be executed on.
    │
    ├── docs               <- Terminology, manuals, and all other explanatory materials
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          
    │   ├── exploratory    <- Exploratory Jupyter Notebooks used in project research.
    │   └── reports        <- Formalised report notebooks, which can be exported into HTML.
    │
    ├── requirements.txt   <- Requirements file for reproducing the analysis environment
    │
    ├── setup.py           <- Setup file making `src` importable (pip install -e .) 
    │
    ├── tests              <- Tests for project package
    │
    └── {{ cookiecutter.pkg_name }}                <- Project package.
        ├── data           <- Module for importing/generating data.
        ├── features       <- Module for preprocessing and cleaning raw data.
        ├── models         <- Module for training and implementing models.
        └── visualisation  <- Module for visualising results.

## Prerequisites

This project requires:

* [GNU Make](https://www.gnu.org/software/make/) (symlink: `make`)
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
    * Any version of Miniconda/Anaconda that supports Python3.9 is okay.

~ Refer to any additional software needed to be installed prior to setting up the development environment, and how to install it, here. ~

## User Guide

~ A guide for how to use the end product of this project. ~

# Developers Guide

## Setup

After installing the prerequisites stated above, create the virtual environment for this project with:

```
make env
```

Activate the environment and install dependencies with:

```
conda activate {{ cookiecutter.pkg_name.replace('_', '-') }}
poetry install
```

Should you only want to install core dependencies, add the flag `--no-dev`. After this, you're free to develop your changes.

~ Provide a step-by-step guide to getting any additional aspects of the development environment running. ~

## Running Tests

All tests are located in [tests](/tests) and can be run with:

```
make tests
``` 

~ Explain the automated tests for this project ~

## Contributors

* **{{ cookiecutter.project_author }}**
    * Maintainer

Contributors are advised to follow [PEP 8 guidelines](https://www.python.org/dev/peps/pep-0008/) for code layout.

Outstanding issues (tasks, bugs, etc.) can be found in the Issues tracker. Log any completed issues in the contributors list above.

## License

~ Reference to the license used in this project ~

## Acknowledgements

This project layout is based on v2.0.0 of [Dirta Science](https://gitlab.com/mwtmurphy/dirta-science).

~ A hat tip to any other research, inspirations, code, etc. used in this project ~