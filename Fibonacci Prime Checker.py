import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4
    return int(math.isqrt(x1)) ** 2 == x1 or int(math.isqrt(x2)) ** 2 == x2

def is_fibonacci_prime(n):
    return is_prime(n) and is_fibonacci(n)

a = int(input("Enter a number :"))
print(is_fibonacci_prime(a)) 
