"""Shared test fixtures."""

import pytest
from enguard.util import init_temp_repo


@pytest.fixture
def repo():
    """Set up a new git repo."""
    repo, dir = init_temp_repo()
    yield repo
    dir.cleanup()
