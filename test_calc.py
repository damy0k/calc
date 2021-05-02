import pytest
from calc import *

def test_add():
    assert 7 == add(2, 5)
    assert 2 == add(1,1)

def test_sub():
    assert -3 == sub(2, 5)
    assert 6 == sub(-2, -8)

def test_mul():
    assert 4 == mul(2, 2)

def test_div():
    with pytest.raises(ZeroDivisionError):
        div(2, 0)