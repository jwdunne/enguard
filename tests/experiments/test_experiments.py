"""Test output of experiments for features under development."""

import pytest
from pydriller import GitRepository

from enguard.experiments import list_staged_files
from enguard.util import repo_path
from tests.util import stage_tmp_file


@pytest.mark.integration
def test_list_staged_files(repo: GitRepository):
    """Test list_staged_files returns only staged files."""
    filename = stage_tmp_file(repo)
    assert repo_path(repo) / filename in list_staged_files(repo)


@pytest.mark.integration
def test_list_staged_files_is_empty(repo: GitRepository):
    """Test list_staged_Files returns empty list if nothing staged."""
    assert not list_staged_files(repo)
