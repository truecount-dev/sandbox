from calc import clamp, share


def test_below():
    assert clamp(-5, 0, 10) == 0


def test_inside():
    assert clamp(5, 0, 10) == 5


def test_share():
    assert share(1, 4) == 0.25
