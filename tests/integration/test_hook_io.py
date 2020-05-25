import pytest
from git import Repo

from enguard.hooks import Hook
from enguard.io import FileIO
from enguard.util import repo_path


@pytest.mark.integration
def test_integrate_hook_with_io(repo: Repo):
    hook = Hook("test-hook", repo_path(repo))

    io = FileIO()
    assert not io.exists(hook.path)

    hook.install(io)
    assert io.exists(hook.path)
