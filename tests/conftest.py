"""Pytest configuration to import fixtures."""

import json
from pathlib import Path

import pytest

import alchemy

alchemy._test_folder = Path(__file__).parent.resolve()


@pytest.fixture
def standard_file():
    """Return a standard file."""
    return "tests/file_name"
