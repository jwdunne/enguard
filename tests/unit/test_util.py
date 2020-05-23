"""Tests project utility functions."""

import os
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from enguard.util import repo_path, init_temp_repo


@pytest.mark.unit
def test_init_temp_repo_can_be_closed():
    """Test that init_temp_repo cleans up."""
    repo = init_temp_repo()
    assert os.path.isdir(repo.path)
    repo.repo.close()
