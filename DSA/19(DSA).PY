class solution(object):
    def duplicate(self , n):
        seen = set()
        for i in n:
            if i in seen:
                return True
            seen.add(i)
        return false


n=list(map(int,input("enter the array :").split()))
sol  = solution()
print(sol.duplicate(n))
            