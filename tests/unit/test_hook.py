import pytest

from pathlib import Path
from enguard.hooks import Hook, hook_script, install_hooks
from enguard.io import MemIO


@pytest.mark.unit
def test_install_api():
    hook = Hook("test-hook", Path("./"))

    false_io = MemIO(True)
    hook.install(false_io)
    assert false_io.out is MemIO.NO_WRITE

    true_io = MemIO(False)
    hook.install(true_io)
    expected_script = hook_script("test-hook")
    assert true_io.out == (Path("./.git/hooks/test-hook"), expected_script, 0o600)


@pytest.mark.unit
def test_hooks_constructor():
    missing_exec = MemIO(exists_value=False)
    found_exec = MemIO(exists_value=True)

    install_hooks(Path("./"), found_exec)
    assert found_exec.out is MemIO.NO_WRITE

    install_hooks(Path("./"), missing_exec)
    (path, _, mode) = missing_exec.out
    assert isinstance(path, Path)
    assert mode == 0o600
