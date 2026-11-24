n=int(input("enter the value:"))
fac=1
if n<0:
    print("the num is not exists in negative")
elif n==0:
    print("the zero is one(1)")
else:
    for i in range(1,n+1):
        fac=fac*i        
    print("the factorial is=" , fac) 