def polygonal_number(s, n):
    """Return the n-th s-gonal number."""
    if s < 3:
        raise ValueError("s must be >= 3 for polygonal numbers")
    return ((s - 2) * n * n - (s - 4) * n) // 2

# Example
print("8th hexagonal number =", polygonal_number(7, 9))
