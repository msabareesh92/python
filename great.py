a=int(input("enter the first number"))
b=int(input("the second number"))
c=int(input("the third number"))
print(type (a))
if a>b and a>c:
    print("A is greater")
elif b>a and  b>c:
    print("B is greater")
elif a==b and b==c and a==c:
    print ("numbers are =")
else:
    print("c is greater")

