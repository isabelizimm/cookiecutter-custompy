# cookiecutter-custompy

# Use

To use a cookiecutter template, first [install cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html#install-cookiecutter) and then run 

`cookiecutter https://github.com/isabelizimm/cookiecutter-custompy/`

# Contents
## General
- Code of conduct
- History
- README.md
- python .gitignore

## Dependency Tracking
- requirements/requirements_dev.txt

## Setup
- setup.py
- setup.cfg
- pyproject.toml

## GitHub Actions
### `tests.yml`
- run tests on Ubuntu:latest
- Python versions 3.7-3.10
- codecov

### `docs.yml`
- checks to see if Sphinx docs build

## GitHub issue templates
- Bug report
- Feature request
- Release checklist

## Pre-commit hooks
- check-yaml, end-of-file-fixer, trailing whitespace
- black
- flake8
