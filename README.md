# Project boilerplate

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Project boilerplate I currently use for early-phase projects (as of 2023-07-29).

# Background

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

Set up your project with the data science template:
```
cookiecutter https://github.com/mwtmurphy/project-boilerplate
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


## Acknowledgements

Inspired by:
* [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) (last accessed 2023-07-29).
* [Hypermodern Python](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769) (last accessed 2023-07-29).
* [CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/) (last accessed 2023-07-29).