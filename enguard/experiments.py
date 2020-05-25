"""Experiment with potential solutions."""
import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional

import git

from enguard.util import repo_path

ASSERTION = True


class GitChange(Enum):
    Add = "A"
    Mod = "M"
    Del = "D"


@dataclass(frozen=True)
class GitFile:
    path: Path
    change_type: Optional[GitChange] = None

    @classmethod
    def from_diff_line(cls, base: Path, diff_line):
        change_type, filename = diff_line
        return GitFile(base / filename, change_type)

    def where_change_type(self, change_type: GitChange):
        if change_type is self.change_type:
            return self
        else:
            return GitFile(self.path, change_type)


def list_staged_files(repo: git.Repo) -> List[str]:
    """List staged files in git."""
    diff = repo.git.diff(name_status=True, staged=True)
    return git_files_to_path(repo_path(repo), parse_diff(diff))


def list_files_since_last_push(repo: git.Repo) -> List[str]:
    if repo.active_branch.tracking_branch():
        diff = repo.git.diff("@{push}..HEAD", name_status=True)
    else:
        diff = repo.git.diff("master..HEAD", name_status=True)
    return git_files_to_path(repo_path(repo), parse_diff(diff))


def git_files_to_path(base: Path, files):
    return [GitFile.from_diff_line(base, diff_line) for diff_line in files]


def parse_diff(diff):
    return [parse_diff_line(line) for line in diff.splitlines()]


def parse_diff_line(diff_line: str):
    match = re.match(r"^(A|M|D)\s+(.*)$", diff_line)

    if match is None:
        raise ValueError("diff_line does not have form: mode path")

    change_type, filename = match.groups()
    return GitChange(change_type), filename
