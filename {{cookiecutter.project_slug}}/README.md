{% set is_open_source = cookiecutter.license != 'KB license' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}
|license| |docs| |coverage| |Security Rating| |Maintainability|

{{ cookiecutter.project_short_description }}

* Free software: {{ cookiecutter.license }}

Features
--------

* Package template: Cookiecutter_ 
* Packaging and dependency management: Poetry_
* Formatter: Black_ and Flake8_
* Type checker: Mypy_
* Tests framework: Pytest_
* Automate and standardize testing: Tox_
* Documentation: Sphinx_

.. |tag| image:: https://img.shields.io/github/v/tag/FabienMeyer/{{ cookiecutter.project_name }}
    :alt: Tag
    :target: https://github.com/FabienMeyer/{{ cookiecutter.project_name }}/tags
  
.. |license| image:: https://img.shields.io/pypi/l/e-lims
    :alt: License
    :target: https://github.com/FabienMeyer/{{ cookiecutter.project_name }}/blob/main/LICENSE

.. |docs| image:: https://readthedocs.org/projects/e-lims/badge/?version=latest
    :alt: Documentation Status
    :target: https://fabienmeyer.github.io/{{ cookiecutter.project_name }}/

.. |coverage| image:: https://codecov.io/gh/FabienMeyer/{{ cookiecutter.project_name }}/branch/main/graph/badge.svg?token=H2L1PG5S5A 
    :alt: Test coverage
    :target: https://codecov.io/gh/FabienMeyer/{{ cookiecutter.project_name }}

.. |Security Rating| image:: https://sonarcloud.io/api/project_badges/measure?project=FabienMeyer_{{ cookiecutter.project_name }}&metric=security_rating
    :alt: Security Rating
    :target: https://sonarcloud.io/project/overview?id=FabienMeyer_{{ cookiecutter.project_name }}

.. |Maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=FabienMeyer_{{ cookiecutter.project_name }}&metric=sqale_rating
    :alt: Maintainability
    :target: https://sonarcloud.io/project/overview?id=FabienMeyer_{{ cookiecutter.project_name }}


.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _Poetry: https://python-poetry.org/
.. _Black: https://black.readthedocs.io/en/stable/
.. _Flake8: https://flake8.pycqa.org/en/latest/
.. _Mypy: http://mypy-lang.org/
.. _Pytest: https://docs.pytest.org/en/stable/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
