start=int(input("enter the value:"))
end=int(input("enter the value:"))

for n in range(start,end+1):
    if n>0:
        for i in range(2,n):
            if n%i==0:
                break   

        else:
            print(n)        