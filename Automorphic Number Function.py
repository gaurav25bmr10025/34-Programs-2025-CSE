a = int(input("Enter a number :"))

sq = a ** 2

digits = len(str(a))

if sq % (10 ** digits) == a:
    print("Automorphic number")
    
else:
    print("NOT Automorphic number")
