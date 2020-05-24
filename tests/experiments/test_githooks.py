import os
import subprocess

from pydriller import GitRepository

from enguard.hooks import HOOK_SCRIPT, HOOKS, hooks_path
from tests.util import dir_context, hooks_ok, stage_tmp_file


def test_register_git_hooks(repo: GitRepository):
    path = hooks_path(repo.path)

    for hook in HOOKS:
        with open(path / hook, "w+") as f:
            f.write(HOOK_SCRIPT)
            os.chmod(path / hook, 0o700)

    dir_context(path, hooks_ok)

    stage_tmp_file(repo)

    result = subprocess.run(
        ["git", "commit", "-m", "test"], check=False, capture_output=True, cwd=repo.path
    )
    assert b"Running enguard" in result.stdout
