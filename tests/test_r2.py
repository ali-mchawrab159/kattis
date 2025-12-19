from kattis.r2 import r2


def test_r2_basic():
    assert r2(11, 15) == 19


def test_r2_negative():
    assert r2(-5, -3) == -1
