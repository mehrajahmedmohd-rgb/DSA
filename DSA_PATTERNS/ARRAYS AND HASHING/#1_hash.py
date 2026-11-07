def sol(n,tar):
    seen={}
    for i in range(len(n)):
        c = tar - n[i]
        if c in seen:
            return [seen[c],i]
            
        else:
            seen[n[i]] = i

n=list(map(int,input("enter the numbers").split()))
tar=int(input("enter the target:"))
print(sol(n,tar))