"""Sphinx configuration."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))

import {{ cookiecutter.project_slug }}

# -- General configuration ---------------------------------------------
extensions = [
	'sphinx.ext.autodoc',
	'sphinx_autodoc_typehints',
	'sphinx.ext.doctest',
	'sphinx.ext.intersphinx',
	'sphinx.ext.todo',
	'sphinx.ext.coverage',
	'sphinx.ext.viewcode',
	'myst_parser',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = '{{ cookiecutter.project_name }}'
package = '{{cookiecutter.project_slug}}'
author = '{{ cookiecutter.full_name }}'
copyright = '{% now 'local', '%Y' %}, {}'.format(author)
version = '{{ cookiecutter.version }}'
release = '{ cookiecutter.version }}'
language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True


# -- Options for HTML output -------------------------------------------
html_theme = 'sphinx_rtd_theme'

# -- Options for HTMLHelp output ---------------------------------------
htmlhelp_basename = '{{ cookiecutter.project_slug }}doc'

# -- Options for LaTeX output ------------------------------------------
latex_elements = {}

latex_documents = [
    (master_doc, '{{ cookiecutter.project_slug }}.tex',
     '{} Documentation'.format(project),
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------
man_pages = [
    (master_doc, '{{ cookiecutter.project_slug }}',
     '{} Documentation'.format(project),
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------
texinfo_documents = [
    (master_doc, '{{ cookiecutter.project_slug }}',
     '{} Documentation'.format(project),
     author,
     '{{ cookiecutter.project_slug }}',
     """{{ cookiecutter.project_short_description }}""",
     'Miscellaneous'),
]

intersphinx_mapping = {'python': ('https://docs.python.org/3/', None)}
set_type_checking_flag = True
always_document_param_types = True
