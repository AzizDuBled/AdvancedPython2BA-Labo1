import pytest
import utils

def test_fact():
    assert utils.fact(4) == 24


def test_roots():
    assert utils.roots(0,1,-1) == [1,0]


def test_integrate():
    assert utils.integrate(1, 0, 1) == 1

