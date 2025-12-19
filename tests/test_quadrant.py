from kattis.quadrant import quadrant


def test_quadrant_1():
    assert quadrant(1, 1) == 1


def test_quadrant_2():
    assert quadrant(-1, 1) == 2


def test_quadrant_3():
    assert quadrant(-1, -1) == 3


def test_quadrant_4():
    assert quadrant(1, -1) == 4

