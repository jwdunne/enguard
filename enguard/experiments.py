"""Experiment with potential solutions."""

import tempfile
import os
import git
from pydriller import GitRepository

ASSERTION = True


def init_temp_repo():
    """Init a temporary git repo."""
    dir = tempfile.TemporaryDirectory()
    git.Repo.init(dir.name)
    return GitRepository(dir.name), dir


# TODO: Simplify with GitPython GitCmd
def list_staged_files(repo: GitRepository):
    """List staged files in git."""
    entry_items = repo.repo.index.entries.items()
    entries = [path for (path, _) in entry_items]
    return [os.path.join(repo.path, name) for (name, _) in entries]
