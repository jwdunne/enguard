"""Tests project utility functions."""

import os
from unittest.mock import MagicMock

import pytest
from enguard.util import get_absolute_repo_path, init_temp_repo


@pytest.mark.rapid
def test_absolute_repo_path():
    """Test absolute_repo_path returns absolute path to repo."""
    repo_path = "repo_path"
    repo = MagicMock(path=repo_path)
    expected = os.path.join(repo_path, "test_path")
    assert get_absolute_repo_path(repo, "test_path") == expected


@pytest.mark.fast
def test_init_temp_repo_can_be_closed():
    """Test that init_temp_repo cleans up."""
    repo = init_temp_repo()
    assert os.path.isdir(repo.path)
    repo.repo.close()
