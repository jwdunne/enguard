import os
from tempfile import NamedTemporaryFile

from pydriller import GitRepository

from enguard.hooks import hooks_exist
from enguard.util import entry_names

# TODO: Reconsider naming of these e.g for_all_files_in


def dir_context(path, assertion):
    """Asserts within the context of a directory tree."""
    with os.scandir(path) as entries:
        assert assertion(entries)


def hooks_ok(entries):
    return hooks_exist(entry_names(entries))


def stage_tmp_file(repo: GitRepository):
    with NamedTemporaryFile(dir=repo.path, delete=False) as staged:
        repo.repo.index.add([staged.name])
        return staged.name
