class solution(object):
    def duplicate(self ,nums):
        return len(set(nums)) != len(nums)
nums = list(map(int ,input("enter the number :").split()))
sol = solution()
result = sol.duplicate(nums)
print(result)