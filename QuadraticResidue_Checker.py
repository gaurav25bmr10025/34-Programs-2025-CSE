def is_quadratic_residue(a, p):
    if a == 0 or a == 1:
        return True
    return pow(a, (p - 1) // 2, p) == 1

print(is_quadratic_residue(8, 21)) 