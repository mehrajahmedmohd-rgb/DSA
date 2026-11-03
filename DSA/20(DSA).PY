class solution(object):
    def duplicate(self , n):
        return len(set(n)) != len(n)

n = list(map(int,input("enter the number :").split()))
sol = solution()
print(sol.duplicate(n))