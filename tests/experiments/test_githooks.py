import subprocess
import pytest

from pydriller import GitRepository

from enguard.hooks import HOOKS, hooks_path, install_hook
from tests.util import dir_context, hooks_ok, stage_tmp_file, exit_ok


@pytest.mark.experiments
def test_register_git_hooks(repo: GitRepository):
    path = hooks_path(repo.path)

    for hook in HOOKS:
        install_hook(hook, repo.path)

    dir_context(path, hooks_ok)

    stage_tmp_file(repo)

    result = subprocess.run(
        ["git", "commit", "-m", "test"],
        check=True,
        capture_output=True,
        cwd=repo.path,
        text=True,
    )

    assert exit_ok(result.returncode)
