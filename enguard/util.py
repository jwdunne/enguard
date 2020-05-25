"""Useful utility functions."""

from pathlib import Path

from git import Repo


def repo_path(repo: Repo) -> Path:
    """Convert a path relative to the repo and returns an absolute path."""
    return Path(repo.working_dir)


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
