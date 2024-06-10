"""Alchemy Package."""

from importlib.metadata import PackageNotFoundError, version

# from alchemy.tables import AlchemyTable

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = None
