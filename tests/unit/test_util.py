"""Tests project utility functions."""

import os

import pytest

from enguard.util import init_temp_repo
from hypothesis import given
import hypothesis.strategies as st
from operator import add, mul
from functools import partial
from enguard.util import complement, compose, const


@pytest.mark.unit
def test_init_temp_repo_can_be_closed():
    """Test that init_temp_repo cleans up."""
    repo = init_temp_repo()
    assert os.path.isdir(repo.path)
    repo.repo.close()


@given(st.integers(), st.integers(), st.integers())
def test_compose_is_associative(a, b, c):
    f_n = partial(add, a)
    g_n = partial(mul, b)

    n = compose(f_n, compose(g_n, f_n))
    m = compose(compose(f_n, g_n), f_n)

    assert n(c) == m(c)


@pytest.mark.unit
def test_complement():
    t = const(True)
    f = complement(t)
    assert (not t(0)) == f(0)
