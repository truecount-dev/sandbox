from calc import clamp


def test_below():
    assert clamp(-5, 0, 10) == 0


def test_inside():
    assert clamp(5, 0, 10) == 5
