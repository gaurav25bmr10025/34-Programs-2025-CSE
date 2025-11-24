def is_highly_composite(n):
    def divisors(x):
        return count_divisors(x)
    n_div = divisors(n)
    for i in range(1, n):
        if divisors(i) >= n_div:
            return False
    return True

a = int(input("Enter a number :"))

print(is_highly_composite(a)) 