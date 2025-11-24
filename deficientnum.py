a = int(input("ENTER A NUMBER :"))
c = 0

for i in range (1 , a):
    b = a % i 

    if b == 0 :
        c += i


if c > a :
    print ("Number is not deficient")

else :
    print ("Number is deficient")