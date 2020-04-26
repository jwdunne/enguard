#!/usr/bin/env bash

set -eu

flake8 enguard
bandit -r enguard
mypy enguard
xenon --max-absolute B --max-modules A --max-average A enguard
