"""Test output of experiments for features under development."""

import pytest
from pydriller import GitRepository
from tempfile import NamedTemporaryFile
from enguard.experiments import list_staged_files
from flake8.api import legacy as flake8
import subprocess
from bandit.core import manager as bandit_manager


@pytest.mark.fast
def test_list_staged_files(repo: GitRepository):
    """Test list_staged_files returns only staged files."""
    with NamedTemporaryFile(dir=repo.path, delete=False) as staged:
        repo.repo.index.add([staged.name])
        assert staged.name in list_staged_files(repo)


@pytest.mark.fast
def test_list_staged_files_is_empty(repo: GitRepository):
    """Test list_staged_Files returns empty list if nothing staged."""
    assert not list_staged_files(repo)
