import os
import subprocess

import pytest
from git import Repo

from enguard.hooks import HOOKS, hooks_path, install_hook
from enguard.util import repo_path
from tests.util import hooks_ok, stage_tmp_file


@pytest.mark.experiments
def test_register_git_hooks(repo: Repo):
    path = hooks_path(repo_path(repo))

    for hook in HOOKS:
        install_hook(hook, repo_path(repo))

    with os.scandir(path) as entries:
        assert hooks_ok(entries)

    stage_tmp_file(repo)

    # Not using capture_output due to 3.6 support
    result = subprocess.run(
        ["git", "commit", "-m", "test"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=repo_path(repo),
    )

    assert result.returncode == 0
