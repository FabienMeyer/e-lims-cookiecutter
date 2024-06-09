# E-lims-cookiecutter template

![Tag](https://img.shields.io/github/v/tag/FabienMeyer/e-lims-cookiecutter) ![License](https://img.shields.io/pypi/l/e-lims) ![Documentation Status](https://readthedocs.org/projects/e-lims/badge/?version=latest) ![Test coverage](https://codecov.io/gh/FabienMeyer/e-lims-cookiecutter/branch/main/graph/badge.svg?token=H2L1PG5S5A) ![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=FabienMeyer_e-lims-cookiecutter&metric=security_rating) ![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=FabienMeyer_e-lims-cookiecutter&metric=sqale_rating)

Cookiecutter template used to create Python package with Poetry ready.

## Features

* Package template: [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
* Packaging and dependency management: [Poetry](https://python-poetry.org/)
* Formatter: [Black](https://black.readthedocs.io/en/stable/)
* Linter: [Ruff](https://docs.astral.sh/ruff/)
* Type checker: [Mypy](https://mypy.readthedocs.io/en/stable/#)
* Tests framework: [Pytest](https://docs.pytest.org/en/stable/)
* Automate and standardize testing: [Tox](http://testrun.org/tox/)
* Documentation: [Sphinx](http://sphinx-doc.org/)

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 2.1.1 or higher):

```bash
pip install -U cookiecutter
```

Generate a Python package project:
```bash
cookiecutter https://github.com/FabienMeyer/e-lims-cookiecutter
```