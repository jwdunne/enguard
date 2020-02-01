"""Experiment with potential solutions."""

import tempfile
import git
from pydriller import GitRepository

ASSERTION = True


def init_temp_repo():
    """Init a temporary git repo."""
    dir = tempfile.TemporaryDirectory()
    git.Repo.init(dir.name)
    return GitRepository(dir.name), dir
