"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'

from importlib.metadata import version as _v

# Set version -----------------------------------------------------------------

__version__ = _v("{{ cookiecutter.version }}")

del _v
