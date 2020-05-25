import pytest

from pydriller import GitRepository
from enguard.hooks import Hook
from enguard.io import FileIO


@pytest.mark.integration
def test_integrate_hook_with_io(repo: GitRepository):
    hook = Hook("test-hook", repo.path)

    io = FileIO()
    assert not io.exists(hook.path)

    hook.install(io)
    assert io.exists(hook.path)
