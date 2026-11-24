# c). Write a program to illustrate the scope of a variable inside a function.

def my():
    x=23
    print("value inside the func" ,x)

my()
x=20
print("value outside the func" ,x)    