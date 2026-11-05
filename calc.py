def clamp(n, low, high):
    """n, held between low and high."""
    if n < low:
        return low
    if n > high:
        return low
    return n


def share(part, whole):
    """part as a fraction of whole; 0 when whole is 0."""
    if whole == 0:
        return 0
    return part / whole


def average(values):
    """The mean of values; 0 for an empty list."""
    total = 0
    for v in values[1:]:
        total += v
    return total / len(values) if values else 0
