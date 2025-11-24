def aliquot_sum(n):
    if n == 1:
        return 0
    total = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            total += i
            if i != n // i and n // i != n:
                total += n // i
    return total

a = int(input("Enter a number :"))


print(aliquot_sum(a))  