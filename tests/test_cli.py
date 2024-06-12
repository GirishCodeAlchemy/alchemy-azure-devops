import subprocess
import sys
from unittest import mock
import pytest

def test_version():
    result = subprocess.run([sys.executable, "-m", "alchemy.cli", "version"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "version" in result.stdout

def test_export_data():
    result = subprocess.run([
        sys.executable, "-m", "alchemy.cli", "export_data",
        "--mode", "csv",
        "--meta_data_xls", "metadata.xlsx",
        "--output_path", "output/"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Invoke export code" in result.stdout

def test_filter_data():
    result = subprocess.run([
        sys.executable, "-m", "alchemy.cli", "filter_data",
        "--mode", "csv",
        "--meta_data_xls", "metadata.xlsx"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Invoke filter" in result.stdout

def test_unknown_command():
    result = subprocess.run([sys.executable, "-m", "alchemy.cli", "unknown"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Unknown command: unknown." in result.stdout
