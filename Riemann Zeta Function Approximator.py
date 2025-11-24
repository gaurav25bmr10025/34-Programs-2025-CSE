def zeta_approx(s, terms):
    total = 0.0
    for n in range(1, terms + 1):
        total += 1 / (n ** s)
    return total

print(zeta_approx(3, 1000)) 
