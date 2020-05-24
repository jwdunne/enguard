# Credits to:
# https://github.com/docker/docker-py/blob/master/Makefile
SHELL := bash

ifndef $(PYTHON_VERSION)
	PYTHON_VERSION = 3.8
endif

DOCKER_TAG = "jwdunne/enguard:$(PYTHON_VERSION)"

.PHONY: all
all: check test

.PHONY: clean
clean:
	find -name "__pycache__" | xargs rm -fr

.PHONY: build
build:
	docker build -t $(DOCKER_TAG) . --build-arg PYTHON_VERSION=$(PYTHON_VERSION)

.PHONY: build-docs
build-docs:
	echo "Building docs"

.PHONY: test
test: test-unit test-experiments test-e2e

.PHONY: test-unit
test-unit: build
	docker run -t $(DOCKER_TAG) pytest tests/unit

.PHONY: test-experiments
test-experiments: build
	docker run -t $(DOCKER_TAG) pytest tests/experiments

.PHONY: test-e2e
test-e2e: build
	docker run -t $(DOCKER_TAG) pytest tests/e2e

.PHONY: check
check: flake8 bandit xenon mypy yamllint

.PHONY: check-docs
check-docs:
	yarn markdownlint '*.md'

.PHONY: flake8
flake8: build
	docker run -t --rm $(DOCKER_TAG) flake8 .

.PHONY: bandit
bandit: build
	docker run -t --rm $(DOCKER_TAG) bandit -r .

.PHONY: mypy
mypy: build
	docker run -t --rm $(DOCKER_TAG) mypy .

.PHONY: xenon
xenon:
	xenon \
		--max-absolute B \
		--max-modules A \
		--max-average A \
		enguard

.PHONY: yamllint
yamllint: build
	yamllint .

.PHONY: check-local
check-local:
	flake8 enguard && \
	bandit -r enguard && \
	mypy enguard && \
	yarn markdownlint '*.md' && \
	yamllint . && \
	xenon \
		--max-absolute B \
		--max-modules A \
		--max-average A \
		enguard

.PHONY: test-local
test-local:
	pytest

.PHONY: local
local: check-local test-local

.PHONY: shell
shell: build
	docker run -it $(DOCKER_TAG) python
