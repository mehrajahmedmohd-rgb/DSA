fruits = ("apple" , "banana" , "orange")
print(fruits)

fruits=list(fruits)
fruits.append("cherry")
fruits=tuple(fruits)
print(fruits)

print(fruits[3])

for fruits in fruits:
    print(fruits)

if "banana" in fruits:
    print("yesss founded") 

print(len(fruits))    
