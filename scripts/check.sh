#!/usr/bin/env bash

set -eu

# Python
flake8 enguard
bandit -r enguard
mypy enguard
xenon --max-absolute B --max-modules A --max-average A enguard

# Docs
yarn markdownlint '*.md'

# Config
yamllint .
