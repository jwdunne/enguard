#!/usr/bin/env bash

pytest --cov-config=setup.cfg --cov=enguard -m 'not slow'
