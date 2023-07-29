# Dirta Science

A standardised directory structure for Data Science projects.

# General Use

## Template Layout

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
    │   └── raw            <- Raw data for which experiments can be executed on.
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
    └── {package name}     <- Project package.
        ├── data           <- Module for importing/generating data.
        ├── features       <- Module for preprocessing and cleaning raw data.
        ├── models         <- Module for training and implementing models.
        └── visualisation  <- Module for visualising results.

## Prerequisites

* [GNU Make](https://www.gnu.org/software/make/) (symlink: `make`)
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
    * Any version of Miniconda/Anaconda that supports Python3.9 is okay.

## Creating a Template

Install cookiecutter in your base environment:

```
conda install cookiecutter=1.7.2
```

Create your project with the data science template:
```
cookiecutter https://gitlab.com/mwtmurphy/dirta-science
```

Prompts will then follow on screen for the remaining project setup. After this, you're free to tackle your project. Enjoy!

# Developers Guide

## Setup

After installing the prerequisites stated above, create the virtual environment for this project with:

```
make env
```

Activate the environment and install dependencies with:

```
conda activate dirta-science
poetry install
```

Should you only want to install core dependencies, add the flag `--no-dev`. After this, you're free to develop your changes.

## Running Tests

All tests are located in [tests](/tests) and can be run with:

```
make tests
``` 

## Contributors

* **Mitchell Murphy**
    * Maintainer
    * Updated template to work with Conda & Poetry (v2.0.0)
    * Updated template to work with virtualenv and added CRISP-DM documentation (v1.0.0)

Contributors are advised to follow [PEP 8 guidelines](https://www.python.org/dev/peps/pep-0008/) for code layout.

Outstanding issues (tasks, bugs, etc.) can be found in the Issues tracker. Log any completed issues in the contributors list above.

## License

This project is licensed under the [MIT License](./LICENSE).

## Acknowledgements

* This project is a personalised theme for [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/).
* This theme is originally based on [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/).
* The template documents are created from the [CRISP-DM guide](docs/crisp_dm.pdf) data mining guide.