"""
Configuration module.

Types:

data Config = Config {
    hooks :: [Hook],
    watchers :: [Watcher],
    guards :: [Guard]
}

data Hook = Hook {
    name :: GitHook,
    patterns :: [TaskPattern]
}

data GitHook = PreCommit | PrePush | PostMerge | ...

data Watcher = Watcher [TaskPattern]

data Guard = Guard {
    name :: String,
    glob :: Glob,
    run  :: [Cmd]
}
"""

from pathlib import Path

import yaml

CONF_PATH = ".enguard.yml"

DEFAULT_CONF = {
    "hooks": {
        "pre-commit": [
            'echo "Add your pre-commit steps here."',
            'echo "Affected files {{ files.affected }}"',
        ],
        "pre-push": [
            'echo "Add your pre-push steps here."',
            'echo "Affected files {{ files.affected }}"',
        ],
        "post-merge": [
            'echo "Add your post-merge steps here."',
            'echo "Affected files {{ files.affected }}"',
        ],
    }
}


class Config:
    def __init__(self, base_path, name=CONF_PATH):
        self.base = base_path
        self.name = CONF_PATH

    @property
    def path(self):
        return self.base / self.name

    @property
    def to_yaml(self):
        return yaml.safe_dump(DEFAULT_CONF)

    def init(self, io):
        if not io.exists(self.path):
            io.write(self.path, self.to_yaml)


def config_path(base: Path) -> Path:
    return base / CONF_PATH


def init_config(base: Path, io):
    return Config(base).init(io)
