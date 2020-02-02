"""Experiment with potential solutions."""

from typing import List
import tempfile
import os
import git
from pydriller import GitRepository

ASSERTION = True


def list_staged_files(repo: GitRepository) -> List[str]:
    """List staged files in git."""
    client = git.cmd.Git(repo.path)
    filenames = client.diff(name_only=True, staged=True).splitlines()
    return [os.path.join(repo.path, filename) for filename in filenames]
