def is_abundant(n):
    if n < 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total > n

n = int(input("Enter a number: "))
if is_abundant(n):
    print(n, "is an abundant number")
else:
    print(n, "is not an abundant number")
