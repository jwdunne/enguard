import tempfile
from pathlib import Path

from git import Repo

from enguard.experiments import GitChange, GitFile


class GitPush:
    pass


class GitDriver:
    @classmethod
    def pushable_clone(cls):
        bare_repo_dir = tempfile.mkdtemp()
        bare_repo = Repo.init(bare_repo_dir, bare=True)
        assert bare_repo.bare

        repo_dir = tempfile.mkdtemp()
        return cls.from_repo(bare_repo.clone(repo_dir))

    @classmethod
    def from_repo(cls, repo: Repo):
        return cls(repo)

    def __init__(self, repo: Repo):
        self.repo = repo
        self.index = repo.index

    def commit(self):
        return

    def _tmp_file(self):
        with tempfile.NamedTemporaryFile(
            dir=self.repo.working_dir, delete=False, mode="w"
        ) as staged:
            staged.write("This is some random content")
            return staged.name

    def stage(self):
        filename = self._tmp_file()
        self.index.add([filename])
        return GitFile(self.path / filename)

    def add(self, commitmsg):
        file = self.stage()
        self.index.commit(commitmsg)
        return file

    def push(self):
        self.repo.remote().push()

    def modify(self, file: GitFile):
        with open(file.path, "w") as f:
            f.write("This is some new data")
        self.index.add([str(file.path)])

    def branch(self, branch="test/branch"):
        branch = self.repo.create_head("test/branch", "HEAD")
        self.repo.head.reference = branch

    @property
    def is_pristine(self):
        return not self.repo.git.status(porcelain=True)

    @property
    def path(self):
        return Path(self.repo.working_dir)
