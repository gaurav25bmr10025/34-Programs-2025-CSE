def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

a = int(input("Enter a number :"))

print(count_divisors(a))  