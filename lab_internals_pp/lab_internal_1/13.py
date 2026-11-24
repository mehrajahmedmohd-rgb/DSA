a=int(input("enter the value:"))
b=int(input("enter the value:"))
op=input("enter the operators(+,-,/,%,//,**,*)")

if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)    
elif op=="*":
    print(a*b)  
elif op=="/":
    print(a/b)
elif op=="//":
    print(a//b) 
elif op=="**":
    print(a**b)  
else:
    print("invalid operator")              
