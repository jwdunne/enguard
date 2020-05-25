"""Useful utility functions."""

import tempfile
from pathlib import Path

from git import Repo
from pydriller import GitRepository


def init_temp_repo() -> GitRepository:
    """Init a temporary git repo."""
    dir = tempfile.mkdtemp()
    Repo.init(dir)
    return GitRepository(dir)


def repo_path(repo: GitRepository) -> Path:
    """Convert a path relative to the repo and returns an absolute path."""
    return Path(repo.path)


def identity(x):
    return x


def compose(f, g):
    return lambda x: f(g(x))


def complement(f):
    return lambda x: not f(x)


def entry_names(entries):
    return {file.name for file in entries}


def const(x):
    return lambda _: x
