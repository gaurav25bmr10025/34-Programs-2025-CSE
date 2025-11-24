
"""
is_perfect_power.py
Standalone script — checks if a number is a perfect power: n = a**b (a>0, b>1).
"""

import math
import sys
import traceback

def integer_nth_root(n: int, k: int) -> int:
    """Return the integer floor of the k-th root of n using binary search."""
    if n < 0 and k % 2 == 0:
        return 0  
    if n < 2:
        return n
    lo, hi = 1, int(n**(1.0/k)) + 2  
    
    while hi**k < n:
        hi *= 2
    while lo <= hi:
        mid = (lo + hi) // 2
        p = mid**k
        if p == n:
            return mid
        if p < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi  

def is_perfect_power(n: int):
    """
    Returns:
      False                  -> if n is not a perfect power
      (True, a, b)           -> if n == a**b with a>0, b>1
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 1:
        return False  

    max_b = int(math.log2(n))  
    for b in range(2, max_b + 1):
        a = integer_nth_root(n, b)
        if a > 1 and a**b == n:
            return True, a, b
    return False

def run_tests():
    tests = [8, 12, 81, 16, 27, 625, 1, 0, 2, 3, 4, 32, 59049]  
    for t in tests:
        res = is_perfect_power(t)
        print(f"{t:6} -> {res}")

if __name__ == "__main__":
    
    try:
        if len(sys.argv) > 1:
            try:
                n = int(sys.argv[1])
            except ValueError:
                print("Please provide an integer. Example: python is_perfect_power.py 81")
                sys.exit(1)
            print(is_perfect_power(n))
        else:
            print("No argument passed — running sample tests:")
            run_tests()
    except Exception:
        print("An unexpected error occurred:")
        traceback.print_exc()
        sys.exit(1)
