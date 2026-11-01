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
