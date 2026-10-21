def power(x,y):
    if y==0:
        return 1

    return x*power(x, y-1)


x = int (input("enter the value of x :"))
y= int (input("enter the value of y :"))
res = power(x,y)
print(res)