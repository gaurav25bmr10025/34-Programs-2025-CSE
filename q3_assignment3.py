def mean_of_digits(n):
    total = 0
    count = 0
    for digit in str(n):
        total += int(digit)
        count += 1
    return total / count

n = int(input("Enter a number: "))
print("Mean of digits is", mean_of_digits(n))
