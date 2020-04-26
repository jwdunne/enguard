# Enguard

Build tight feedback loops. In minutes.

TODO: Insert 5 minute setup gif

<!-- omit in toc -->

## Table of Contents

- [Enguard](#enguard)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
    - [Initialise](#initialise)
    - [Configuration](#configuration)
    - [Running actions](#running-actions)
    - [Watching for changes](#watching-for-changes)
  - [Why Enguard](#why-enguard)
    - [The Solution](#the-solution)
    - [Real-time Feedback](#real-time-feedback)
    - [Stopping Common Build Failures](#stopping-common-build-failures)

## Getting Started

To install:

```bash
pip install enguard
enguard init
```

## Usage

```text
Usage: enguard [command] [flags]

Displays help info.

Options:

    -f, --enguardrc=FILE    Use enguard file (default: .enguardrc)
    --verbose               Provide more feedback
    -v, --version           Output Enguard's version

Commands:

    - init
    - run
    - watch
```

### Initialise

```text
Usage: enguard init [options]

Initialises enguard hooks and enguard config file.
```

Example:

```bash
enguard init
```

`enguard init` creates a new config file, if one doesn't exist, and initialise
git hooks for a project. This command should be run in each local development
environment.

> \*_Tip:_ Use one command to initialise your project for new developers. This is
> the natural home for `enguard init`

### Configuration

Configure your project using Enguard's `.enguard.yml` config file:

```yaml
hooks:
  ['pre-commit', 'pre-push']:
    - lint-*
    - test-*
  pre-push:
    - lint

guards:
  lint-python:
    hooks: ['pre-commit', 'pre-push'],
    glob: "**/*.py",
    steps:
      - 'echo {{ info.diff }} | flake8 --diff'
      - 'bandit -r {{ info.affected }}'
      - 'mypy --incremental'
      - run: |
          xenon \
            --max-absolute B \
            --max-modules A \
            --max-average A

  test-python:
    hooks: ['pre-commit', 'pre-push']
    glob: "**/*.py"
    stategy: 'coverage'
    steps:
      - 'pytest --cov-config='setup.cfg' --cov='enguard'

  lint-docs:
    hooks: ['pre-commit', 'pre-push']
    glob: '**/*.md'
    steps:
      - 'yarn run markdownlint {{ info.affected }}'

  lint-config:
    hooks: ['pre-commit', 'pre-push']
    glob: '**/*.yml'
    steps:
      - 'yamllint {{ info.affected }}'
```

```python
import enguard

PY_FILES = "**/*.py"
DOC_FILES = "**/*.md"

@enguard.guard('lint-python', glob=PY_FILES)
def lint_python(info):
    # Lint affected python files before every push and commit
    ...

@enguard.guard('test-python', glob=PY_FILES, strategy="coverage")
def test_python(info):
    # Run python unit tests before every commit
    ...

@enguard.guard('lint-docs', glob=DOC_FILES)
def lint_docs(info):
    # Run markdownlint, vale, etc
    ...

@enguard.guard('lint-config', glob=CONF_FILES)
def lint_config(info):
    # Run yamllint
    ...
```

TODO: Flesh out example configuration

### Running actions

```text
Usage: enguard run hook_name
```

Example:

```bash
$ enguard run pre-commit
$ echo "Failed? $?"
0
```

Running `enguard run` with a hook name simulates the actions you have configured
for the hook. This is the same command that git calls when running hooks.

### Watching for changes

Usage:

```text
Usage: enguard watch
```

Example:

```bash
$ enguard watch
TODO: Work out interface for watch mode
```

## Why Enguard

Your build fails in CI. A linting issue. You forgot to lint before pushing. To
tell you that, your CI server:

1. Initialises the environment
2. Checks out your project
3. Installs (or loads cached) dependencies
4. Analyses all files
5. Runs all tests, from fastest to slowest
6. Builds your project
7. Deploys

This takes time and costs your company money in server usage. And the feedback
takes minutes, disrupting your flow.

### The Solution

To solve this problem, you need to catch common failures **fast**. Instant
feedback is best. In real-time, before each commit, before each push and after
every merge.

But linting all files and running all tests is still slow - limiting feedback
throughput. And, worse, harming your flow.

### Real-time Feedback

With Enguard, you can refine this feedback loop further. With a watcher, you can
get feedback on affected files in real time.

### Stopping Common Build Failures

To stop common build failures, Enguard guards against commiting and pushing
files that will break the build. But not on every file. Enguard limits the
fileset to affected files only.
