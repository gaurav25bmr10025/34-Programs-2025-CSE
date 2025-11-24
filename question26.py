def lucas_sequence(n):
    if n <= 0:
        return []

    if n == 1:
        return [2]
    if n == 2:
        return [2, 1]

    seq = [2, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

a=int(input("enter a number :"))

print(lucas_sequence(a))
