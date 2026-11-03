from calc import clamp


def test_above_returns_upper_bound():
    assert clamp(15, 0, 10) == 10
    assert clamp(11, 5, 10) == 10
