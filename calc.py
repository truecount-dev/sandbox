def clamp(n, low, high):
    """n, held between low and high."""
    if n < low:
        return low
    if n > high:
        return high
    return n
