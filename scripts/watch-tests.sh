#!/usr/bin/env bash

set -eu

chokidar "**/*.py" -c 'pytest'
