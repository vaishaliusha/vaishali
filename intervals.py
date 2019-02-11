lower=int(input("Enter the lower limit for the range:"))
upper=int(input("Enter the upper limit for the range:"))
print("enter the two intervals in upper and lower:")
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
