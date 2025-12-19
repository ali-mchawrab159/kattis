from kattis.twostones import twostones


def test_twostones_odd():
    assert twostones(1) == "Alice"


def test_twostones_even():
    assert twostones(2) == "Bob"
