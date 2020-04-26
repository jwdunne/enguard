"""Test output of experiments for features under development."""

import pytest
from pydriller import GitRepository
from tempfile import NamedTemporaryFile
from enguard.experiments import list_staged_files
from flake8.api import legacy as flake8
import subprocess


@pytest.mark.fast
@pytest.mark.integration
def test_list_staged_files(repo: GitRepository):
    """Test list_staged_files returns only staged files."""
    with NamedTemporaryFile(dir=repo.path, delete=False) as staged:
        repo.repo.index.add([staged.name])
        assert staged.name in list_staged_files(repo)


@pytest.mark.fast
@pytest.mark.integration
def test_list_staged_files_is_empty(repo: GitRepository):
    """Test list_staged_Files returns empty list if nothing staged."""
    assert not list_staged_files(repo)


@pytest.mark.slow
@pytest.mark.benchmark
def test_run_flake8_from_python(benchmark):
    @benchmark
    def via_module():
        report = flake8.get_style_guide().check_files(".")
        assert report.total_errors == 0


@pytest.mark.slow
@pytest.mark.benchmark
def test_run_flake8_from_subprocess(benchmark):
    @benchmark
    def via_subprocess():
        subprocess.run("flake8")
