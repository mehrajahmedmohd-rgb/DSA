#1) Print the dictionary items 2) access items 3) useget () 4) change values 5) use len() 
dis = {
    "brand" : "bmw" ,
    "model" : "2033cc" ,
    "year" : 2399 
    }

print(dis)

x=dis["brand"]
print(x)

y=dis.get("model")
print(y)

dis["year"]=222222
print(dis)

print(len(dis))