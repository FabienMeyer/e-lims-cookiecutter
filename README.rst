============================
E-lims-cookiecutter template
============================
|tag| |license| |docs| |coverage| |Security Rating| |Maintainability|

Cookiecutter template used to create Python package with Poetry ready.

Features
--------

* Package template: Cookiecutter_ 
* Packaging and dependency management: Poetry_
* Formatter: Black_ and Flake8_
* Type checker: Mypy_
* Tests framework: Pytest_
* Automate and standardize testing: Tox_
* Documentation: Sphinx_

==========
Quickstart
==========

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 2.1.1 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/FabienMeyer/e-lims-cookiecutter

.. |tag| image:: https://img.shields.io/github/v/tag/FabienMeyer/e-lims-cookiecutter
    :alt: Tag
    :target: https://github.com/FabienMeyer/e-lims-cookiecutter/tags
  
.. |license| image:: https://img.shields.io/pypi/l/e-lims
    :alt: License
    :target: https://github.com/FabienMeyer/e-lims-cookiecutter/blob/main/LICENSE

.. |docs| image:: https://readthedocs.org/projects/e-lims/badge/?version=latest
    :alt: Documentation Status
    :target: https://fabienmeyer.github.io/e-lims-cookiecutter/

.. |coverage| image:: https://codecov.io/gh/FabienMeyer/e-lims-cookiecutter/branch/main/graph/badge.svg?token=H2L1PG5S5A 
    :alt: Test coverage
    :target: https://codecov.io/gh/FabienMeyer/e-lims-cookiecutter

.. |Security Rating| image:: https://sonarcloud.io/api/project_badges/measure?project=FabienMeyer_e-lims-cookiecutter&metric=security_rating
    :alt: Security Rating
    :target: https://sonarcloud.io/project/overview?id=FabienMeyer_e-lims-cookiecutter

.. |Maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=FabienMeyer_e-lims-cookiecutter&metric=sqale_rating
    :alt: Maintainability
    :target: https://sonarcloud.io/project/overview?id=FabienMeyer_e-lims-cookiecutter

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _Poetry: https://python-poetry.org/
.. _Black: https://black.readthedocs.io/en/stable/
.. _Flake8: https://flake8.pycqa.org/en/latest/
.. _Mypy: http://mypy-lang.org/
.. _Pytest: https://docs.pytest.org/en/stable/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
