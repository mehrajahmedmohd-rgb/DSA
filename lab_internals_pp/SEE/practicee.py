'''1.	Write a python program for demonstrating the usage of arithmetic operators. CO1
2.	Write a python program to find the largest number among three numbers. CO1
3.	Write a python program to swap two variables. CO1
4.	Write a python program to read a float value and convert Fahrenheit to Centigrade. CO1
5.	Write a python program to reverse the digits of a given number. CO1
6.	Write a python program to print a number is positive/negative using if-else. CO1
7.	Write a python program to calculate the electricity bill consumed by the user. CO1
8.	Write a python program to print the Fibonacci series up to n numbers. CO1
9.	Write a python program to check whether the given string is palindrome or not. CO1
10.	Write a program to create, concatenate, and print a string and access a substring from a given string. CO1
11.	Write a python program to find the area of a circle. CO1
12.	Write a python program to demonstrate list operations (append, insert, remove, pop). CO3
13.	Write a python program to find the factorial of a given number using a function. CO2
14.	Demonstrate try, except and finally blocks in python. CO4
15.	Write a Python program to demonstrate single inheritance. CO4'''


n=55
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c


name=input("enter:")    
if name==name[::-1]:
    print("palindrone")
else:
     print("palindrone")

str1="mehraj"
str2="ahmed"
str3="siddique"

str4=str1+" "+str2+" "+str3
print(str4)
print(str4[0:3])



name=input("enter the name")

count=0

for ch in name:
    if ch.lower() in "aeiou":
        count+=1

print(name[-1])
print(name[-3:])
print(count)        
print(name.upper())