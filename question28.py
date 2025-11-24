def collatz_length(n):
    """Return number of steps for n to reach 1 using Collatz rules."""
    if n <= 0:
        raise ValueError("n must be a positive integer")

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# Example
print("Collatz length of 12 =", collatz_length(18))

