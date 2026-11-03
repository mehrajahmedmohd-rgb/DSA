class solution(object):
    def twosum(self , n ,tar):
        m="fail"
        for i in range (len(n)):
            for j in range(i+1 , len(n)):
                if n[i] + n[j] == tar:
                    return [i,j]

        return m

n = list(map(int,input("enter the array :").split()))
tar = int(input("enter the array to two:"))
sol = solution()
result = sol.twosum(n,tar)
print(result)
