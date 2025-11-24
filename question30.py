def is_carmichael(n):
    """Check if n is a Carmichael number."""
    if n < 2:
        return False

    # Must be composite
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            break
    else:
        return False  # prime

    # Check Korselt's criterion
    import math
    for a in range(2, n):
        if math.gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False
    return True

# Example
print("Is 689 Carmichael?", is_carmichael(689))
