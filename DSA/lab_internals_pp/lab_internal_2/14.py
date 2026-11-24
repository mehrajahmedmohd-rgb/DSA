import numpy as ts
arr1=([1,2,3,4,5])
arr2=([6,7,8,22,10])

add=ts.add(arr1,arr2)
print(add)

subs=ts.subtract(arr2,arr1)
print(subs)

mu=ts.multiply(arr1,arr2)
print(mu)

di=ts.divide(arr2,arr1)
print(di)

po=ts.power(arr1,arr2)
print(po)