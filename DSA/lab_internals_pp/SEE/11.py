try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result =", a // b)

except ZeroDivisionError:
    print("cannot piiii")

finally:
    print("Program Finished.")