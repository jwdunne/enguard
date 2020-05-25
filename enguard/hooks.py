"""
Git hooks module.


"""
import os
from pathlib import Path
from typing import Set
from enguard.io import composeIO

HOOKS_PATH = ".git/hooks"

HOOKS = {
    "applypatch-msg",
    "pre-applypatch",
    "post-applypatch",
    "pre-commit",
    "prepare-commit-msg",
    "commit-msg",
    "post-commit",
    "pre-rebase",
    "post-checkout",
    "post-merge",
    "pre-receive",
    "update",
    "post-receive",
    "post-update",
    "pre-auto-gc",
    "post-rewrite",
    "pre-push",
}


class Hook:
    def __init__(self, hook_name, base_path):
        self.name = hook_name
        self.base = base_path

    @property
    def script(self):
        return hook_script(self.name)

    @property
    def path(self):
        return hooks_path(self.base) / self.name

    def install(self, io):
        if not io.exists(self.path):
            io.write(self.path, self.script, 0o600)


def hooks(path):
    return {Hook(hook, path) for hook in HOOKS}


def install_hooks(path, io):
    for hook in hooks(path):
        hook.install(io)


def hook_script(hook_name: str) -> str:
    return f"""
#!/usr/bin/env bash

set -eu

# enguard start
enguard run-hook {hook_name}
# enguard end
"""


def hooks_path(base: Path) -> Path:
    return base / HOOKS_PATH


def hooks_exist(existing_hooks: Set[str]) -> bool:
    return HOOKS.issubset(existing_hooks)


def missing_hooks(existing_hooks: Set[str]) -> Set[str]:
    return HOOKS - existing_hooks


def install_hook(hook_name: str, base: Path):
    path = hooks_path(base) / hook_name
    with open(path, "w") as f:
        f.write(hook_script(hook_name))
        os.chmod(path, 0o600)
