def multiplicative_persistence(n):
    steps = 0
    while n >= 10:
        prod = 1
        for d in str(n):
            prod *= int(d)
        n = prod
        steps += 1
    return steps

a = int(input("Enter a number :"))

print(multiplicative_persistence(a))