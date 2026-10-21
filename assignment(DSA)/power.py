def power(n,m):
    if m==0:
        return 1

    return  n * power(n,m-1)

n = int (input("enter the value of x: "))
m = int(input("enter the value of y: "))
res= power(n,m)
print(res)