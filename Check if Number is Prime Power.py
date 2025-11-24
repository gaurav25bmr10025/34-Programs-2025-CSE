def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_prime_power(n):
    if n <= 1:
        return False
    for p in range(2, int(n ** 0.5) + 2):
        if is_prime(p):
            val = p
            while val <= n:
                if val == n:
                    return True
                val *= p
    return is_prime(n)  

a = int(input("Enter a number :"))
print(is_prime_power(a))  