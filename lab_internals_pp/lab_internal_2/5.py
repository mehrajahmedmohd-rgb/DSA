#d) Write a python program to find the factorial of a given number using a function 

def my(num):
    fact = 1
    if num < 0:
        print("no")

    elif num == 0:
        print("fact of zero is 1")

    else:
        for i in range(1,num+1) :
            fact = fact * i
    print(f"factorial of {num} is  {fact}")

num=int(input("enter the number:-"))
my(num)                 