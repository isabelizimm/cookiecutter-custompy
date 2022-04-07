{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{%- endif %}


def test_setup():
    """Set up test fixtures, if any."""
    assert "mock" == "mock"

