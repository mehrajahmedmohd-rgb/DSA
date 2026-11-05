f={}
s1="aabb"
for char in s1:
    if char in f:
        f[char]+=1 
    else:
        f[char]=1

print(s1)