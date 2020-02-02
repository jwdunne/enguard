"""Experiment with potential solutions."""

from typing import List

import git
from enguard.util import get_absolute_repo_path
from pydriller import GitRepository

ASSERTION = True


def list_staged_files(repo: GitRepository) -> List[str]:
    """List staged files in git."""
    client = git.cmd.Git(repo.path)
    filenames = client.diff(name_only=True, staged=True).splitlines()
    return [get_absolute_repo_path(repo, filename) for filename in filenames]
