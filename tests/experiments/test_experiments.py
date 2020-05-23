"""Test output of experiments for features under development."""

import pytest
from pydriller import GitRepository
from tempfile import NamedTemporaryFile
from enguard.experiments import list_staged_files
from enguard.util import repo_path


@pytest.mark.integration
def test_list_staged_files(repo: GitRepository):
    """Test list_staged_files returns only staged files."""
    path = repo_path(repo)
    with NamedTemporaryFile(dir=path, delete=False) as staged:
        repo.repo.index.add([staged.name])
        assert path / staged.name in list_staged_files(repo)


@pytest.mark.integration
def test_list_staged_files_is_empty(repo: GitRepository):
    """Test list_staged_Files returns empty list if nothing staged."""
    assert not list_staged_files(repo)
