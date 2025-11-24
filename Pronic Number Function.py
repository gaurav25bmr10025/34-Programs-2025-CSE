n = int(input("Enter a number: "))
i = 0
found = False
while i * (i + 1) <= n:
    if i * (i + 1) == n:
        found = True
        break
    i += 1
    
if found:
    print("Pronic number")

else:
    print("NOT Pronic number")
