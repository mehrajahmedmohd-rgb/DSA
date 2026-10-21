def fibonacchi(n):
    if n == 0 :
        return 0
    elif n==1:
        return 1
    
    return fibonacchi(n-1)+fibonacchi(n-2)

n=int(input("enter the number:"))
print(fibonacchi(n))