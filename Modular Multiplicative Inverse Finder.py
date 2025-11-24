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


print(mod_inverse(4, 19))  
