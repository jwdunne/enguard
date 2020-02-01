"""Test output of experiments for features under development."""

from typing import Tuple
import pytest
import git
from pydriller import GitRepository
from tempfile import NamedTemporaryFile
from enguard import experiments


@pytest.fixture
def git_repo():
    """Set up a new git repo."""
    repo, dir = experiments.init_temp_repo()
    yield repo, dir.name
    dir.cleanup()


def test_experiment_tests(git_repo: Tuple[GitRepository, str]):
    """Test setup for experiments."""
    repo, dirname = git_repo

    with NamedTemporaryFile(dir=dirname, delete=False) as file:
        repo.repo.index.add([file.name])
        assert file.name in repo.files()
