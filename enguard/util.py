"""Useful utility functions."""

import os
import tempfile

from git import Repo
from pydriller import GitRepository


def init_temp_repo() -> GitRepository:
    """Init a temporary git repo."""
    dir = tempfile.mkdtemp()
    Repo.init(dir)
    return GitRepository(dir)


def get_absolute_repo_path(repo: GitRepository, path: str) -> str:
    """Convert a path relative to the repo and returns an absolute path."""
    return os.path.join(repo.path, path)
