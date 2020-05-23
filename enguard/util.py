"""Useful utility functions."""

from pathlib import Path
import tempfile

from git import Repo
from pydriller import GitRepository
from functools import reduce
from typing import Callable, List, TypeVar


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


def prop(name: str):
    return lambda obj: getattr(obj, name)
