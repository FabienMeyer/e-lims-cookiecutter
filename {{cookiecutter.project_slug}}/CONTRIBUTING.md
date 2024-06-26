# Contributing to "{{ cookiecutter.project_slug }}"

First off, thanks for taking the time to contribute! 🎉

The following is a set of guidelines for contributing to "{{ cookiecutter.project_slug }}". These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Enhancements](#suggesting-enhancements)
    - [Pull Requests](#pull-requests)
3. [Style Guides](#style-guides)
    - [Git Commit Messages](#git-commit-messages)
    - [Python Style Guide](#python-style-guide)
4. [Setting Up the Development Environment](#setting-up-the-development-environment)
5. [Running Tests](#running-tests)
6. [Building Documentation](#building-documentation)

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to ["{{ cookiecutter.email }}"].

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

- **Before submitting** a bug report, please check the [existing issues](https://github.com/FabienMeyer/"{{ cookiecutter.project_slug }}"/issues) to see if the issue has already been reported.
- If you find a **Closed** issue that seems like it is the same thing that you are experiencing, include a link to the original issue in your bug report.

#### How Do I Submit A Bug Report?

Bugs are tracked as GitHub issues. Create an issue and provide the following information:

- **Use a clear and descriptive title** for the issue to identify the problem.
- **Describe the exact steps** which reproduce the problem in as many details as possible.
- **Provide specific examples** to demonstrate the steps.
- **Describe the behavior you observed** after following the steps and point out what exactly is the problem with that behavior.
- **Explain which behavior you expected** instead and why.
- **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for "{{ cookiecutter.project_slug }}", including completely new features and minor improvements to existing functionality.

- **Use a clear and descriptive title** for the issue to identify the suggestion.
- **Provide a step-by-step description** of the suggested enhancement in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected** instead and why.
- **Include screenshots and animated GIFs** which help you demonstrate the steps or point out the part of the project which the suggestion is related to.

### Pull Requests

The process described here has several goals:

- Maintain the project's quality
- Fix problems that are important to users
- Engage the community in working toward the best possible project
- Enable a sustainable system for the project's maintainers to review contributions

#### Steps to submit a pull request:

1. Fork the repository.
2. Create a new branch from `main` (or the appropriate branch) for your feature or bug fix.
3. Implement your changes, ensuring that your code adheres to the existing style of the codebase.
4. Add tests that cover your changes (if applicable).
5. Commit your changes using a descriptive commit message.
6. Push your branch to your forked repository.
7. Open a pull request in the main repository.

## Style Guides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
- Limit the first line to 72 characters or less.
- Reference issues and pull requests liberally after the first line.

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) for Python code style.
- Use [Ruff](https://docs.astral.sh/ruff/) for linting.
- Use [Ruff](https://docs.astral.sh/ruff/) forcode formatting.
- Use [Mypy](https://mypy.readthedocs.io/en/stable/#) for type checking.
- Write docstrings for all public methods and classes using [Google style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

## Setting Up the Development Environment

To set up a local development environment:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/FabienMeyer/"{{ cookiecutter.project_slug }}".git
    cd e-lims-cookiecutter
    ```

2. **Install Poetry** (if not already installed):
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Install the dependencies**:
    ```bash
    poetry install --with doc --no-root
    ```

4. **Activate the virtual environment**:
    ```bash
    poetry shell
    ```


## Running Tests, linters and documentation

To run tests, use the following command:

```bash
poetry run tox
```
