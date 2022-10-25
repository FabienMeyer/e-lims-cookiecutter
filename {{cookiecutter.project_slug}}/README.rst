{% set is_open_source = cookiecutter.license != 'KB license' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

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


.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _Poetry: https://python-poetry.org/
.. _Black: https://black.readthedocs.io/en/stable/
.. _Flake8: https://flake8.pycqa.org/en/latest/
.. _Mypy: http://mypy-lang.org/
.. _Pytest: https://docs.pytest.org/en/stable/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
