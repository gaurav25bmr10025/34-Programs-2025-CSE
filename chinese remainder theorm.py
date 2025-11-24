def mod_inverse(a, m):
    
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m

def crt(remainders, moduli):
    from functools import reduce
    total = 0
    prod = reduce(lambda a, b: a * b, moduli)
    for r, m in zip(remainders, moduli):
        p = prod // m
        inv = mod_inverse(p, m)
        total += r * inv * p
    return total % prod


print(crt([2, 3, 1], [3, 4, 5])) 
