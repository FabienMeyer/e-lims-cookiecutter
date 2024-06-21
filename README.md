# e-lims-cruft template

![Tag](https://img.shields.io/github/v/tag/FabienMeyer/e-lims-cookiecutter) 
![License](https://img.shields.io/pypi/l/e-lims) 
![Documentation Status](https://readthedocs.org/projects/e-lims/badge/?version=latest) 
![Test coverage](https://codecov.io/gh/FabienMeyer/e-lims-cookiecutter/branch/main/graph/badge.svg?token=H2L1PG5S5A) 
![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=FabienMeyer_e-lims-cookiecutter&metric=security_rating) 
![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=FabienMeyer_e-lims-cookiecutter&metric=sqale_rating)

## Features

Cruft template used to create Python package.

## Development tools 

* Package template: [Cruft](https://cruft.github.io/cruft/)
* Packaging and dependency management: [Poetry](https://python-poetry.org/)
* Formatter: [Ruff formater](https://docs.astral.sh/ruff/formatter/)
* Linter: [Ruff Linter](https://docs.astral.sh/ruff/linter/)
* Type checker: [Mypy](https://mypy.readthedocs.io/en/stable/#)
* Tests framework: [Pytest](https://docs.pytest.org/en/stable/)
* Automate and standardize testing: [Tox](http://testrun.org/tox/)
* Documentation: [Sphinx](http://sphinx-doc.org/)

## Quickstart

Install cruft.

```bash
pip install cruft
```

Generate a Python package project:
```bash
cruft create https://github.com/FabienMeyer/e-lims-cruft
```