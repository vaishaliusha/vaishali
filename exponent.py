def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter the base: "))
exp=int(input("Enter the  exponential value: "))
   print("enter the Result:",power(base,exp))
