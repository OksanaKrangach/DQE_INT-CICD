# run this with the command
#  pytest tests1.py

import pytest


def test_string_upper():
    assert "foo".upper() == "FOO"
