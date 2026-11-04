class solution(object):
    def duplicate(self , nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False
nums = list(map(int,input("enter the number :").split()))
sol = solution()
result = sol.duplicate(nums)
print(result)
            