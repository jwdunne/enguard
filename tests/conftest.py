"""Shared test fixtures."""
import pytest

from tests.util import init_temp_repo


@pytest.fixture
def repo():
    """Set up a new git repo fixture."""
    return init_temp_repo()
