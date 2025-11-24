def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_mersenne_prime(p):
    if not is_prime(p):
        return False
    m = 2 ** p - 1
    return is_prime(m)

a = int(input("Enter a number :"))
print(is_mersenne_prime(3))  