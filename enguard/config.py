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


def config_path(base: Path) -> Path:
    return base / CONF_PATH
