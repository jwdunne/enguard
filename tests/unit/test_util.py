"""Tests project utility functions."""

import os
from functools import partial
from operator import add, mul

import hypothesis.strategies as st
import pytest
from hypothesis import given

from enguard.util import complement, compose, const
from tests.util import init_temp_repo


@pytest.mark.unit
def test_init_temp_repo_can_be_closed():
    """Test that init_temp_repo cleans up."""
    repo = init_temp_repo()
    assert os.path.isdir(repo.working_dir)
    repo.close()


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
