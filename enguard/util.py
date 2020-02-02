"""Useful utility functions."""

import tempfile
from git import Repo
from pydriller import GitRepository


def init_temp_repo():
    """Init a temporary git repo."""
    dir = tempfile.TemporaryDirectory()
    Repo.init(dir.name)
    return GitRepository(dir.name), dir
