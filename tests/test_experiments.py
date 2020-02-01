"""Test output of experiments for features under development."""

import pytest
from pydriller import GitRepository
from tempfile import NamedTemporaryFile
from enguard.experiments import init_temp_repo, list_staged_files


@pytest.fixture
def repo():
    """Set up a new git repo."""
    repo, dir = init_temp_repo()
    yield repo
    dir.cleanup()


def test_list_staged_files(repo: GitRepository):
    """Test list_staged_files returns only staged files."""
    with NamedTemporaryFile(dir=repo.path, delete=False) as staged:
        repo.repo.index.add([staged.name])
        assert staged.name in list_staged_files(repo)

    with NamedTemporaryFile(dir=repo.path, delete=False) as unstaged:
        assert unstaged.name not in list_staged_files(repo)
