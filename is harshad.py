a = int (input("Enter a number :"))
original_a = a
s= 0
while a > 0 :
    s += a % 10
    a //= 10

    
d = original_a % s 
if d ==0 :
    print ("The number is harshad")

else :
    print("Number is NOT harshad ")


