import os


class FileIO:
    def exists(self, path):
        return os.path.exists(path)

    def write(self, path, text, mode=0o644):
        with open(path, "w+") as f:
            f.write(text)
            os.chmod(path, mode)


class MemIO:
    NO_WRITE = ()

    def __init__(self, exists_value=True):
        self.exists_value = exists_value
        self.out = self.NO_WRITE

    def exists(self, path):
        return self.exists_value

    def write(self, path, text, mode=0o644):
        self.out = (path, text, mode)


def composeIO(cmds):
    def _cmd(io):
        [cmd(io) for cmd in cmds]

    return _cmd
