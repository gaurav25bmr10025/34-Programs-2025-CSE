def sieve(limit):
    is_p = [True] * (limit+1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5)+1):
        if is_p[i]:
            for j in range(i*i, limit+1, i):
                is_p[j] = False
    return [i for i, prime in enumerate(is_p) if prime]

def twin_primes(limit):
    primes = sieve(limit)
    res = []
    for i in range(len(primes)-1):
        if primes[i+1] - primes[i] == 2:
            res.append((primes[i], primes[i+1]))
    return res

a = int(input("Enter a number :"))

print(twin_primes(a))  