def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def order_mod(a, n):
    if gcd(a, n) != 1:
        return None  
    k = 1
    power = a % n
    while power != 1:
        power = (power * a) % n
        k += 1
        if k > n:
            return None  
    return k


print(order_mod(2, 9)) 