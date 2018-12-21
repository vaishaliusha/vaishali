print("enter three numbers:") 
a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the third umber"))
if a>b and a>c:
    print(a, " is largest")
elif b>a and b>c:
    print(b, " is largest")
else:
    print(c, " is largest")
