def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y
    
def did(x,y):
    return x / y

print("1. addition")
print("2.subtraction")
print("3. multiplication")
print("4.division")

choose = input("choose 1,2,3,4:")

if choose == "1":
        num1=float(input("enter the num:"))
        num2=float(input("enter the num:"))
        print(num1, "+" ,num2 ,"= ", add(num1,num2))
    
elif choose == "2":
        num1=float(input("enter the num:"))
        num2=float(input("enter the num:"))
        print(num1 ,"-"  , num2, "= " ,sub(num1,num2))  

elif choose == "3":
        num1=float(input("enter the num:"))
        num2=float(input("enter the num:"))
        print(num1,"*" , num2,  "= ",mul(num1,num2))  
  
elif choose == "4":
    print(num1,  "/" , num2, "= ", did(num1,num2))          

else:
    print("invalid ")