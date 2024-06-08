from pathlib import Path
import pytest

import alchemy
import json

alchemy._test_folder = Path(__file__).parent.resolve()

@pytest.fixture
def standard_file():
    return "tests/folder_name"