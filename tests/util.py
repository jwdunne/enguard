import tempfile
from pathlib import Path
from tempfile import NamedTemporaryFile

from git import Repo

from enguard.hooks import hooks_exist
from enguard.util import entry_names

# TODO: Reconsider naming of these e.g for_all_files_in


def init_temp_repo() -> Repo:
    """Init a temporary git repo."""
    dir = tempfile.mkdtemp()
    return Repo.init(dir)


def hooks_ok(entries):
    return hooks_exist(entry_names(entries))


def stage_tmp_file(repo: Repo, prefix=None):
    filename = ""
    with NamedTemporaryFile(
        dir=repo.working_dir, delete=False, prefix=prefix, mode="w"
    ) as staged:
        staged.write("This is some random content")
        filename = staged.name
    repo.index.add([filename])
    return filename


def exit_ok(exit_code):
    return exit_code == 0
