import pytest
from kattis.r2 import r2


@pytest.mark.parametrize(
    "r1, s, expected",
    [
        (11, 15, 19),
        (0, 10, 20),
        (-5, -3, -1),
    ],
)
def test_r2_parametrized(r1, s, expected):
    assert r2(r1, s) == expected

