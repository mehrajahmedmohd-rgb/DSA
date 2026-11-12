def twoarray(nums):
    prefix=[]
    suffix=[]
    answer=[]
    count_prefix=1
    for i in nums:
        prefix.append(count_prefix)
        count_prefix *= i
    count_suffix=1
    for i in range(len(nums)-1,-1,-1):
        suffix.append(count_suffix)
        count_suffix *= nums[i]
    suffix = suffix[::-1]
    for i in range(len(nums)):
        answer.append(prefix[i]*suffix[i])
    return answer

nums = list(map(int,input("enter the number:").split()))
result = twoarray(nums)
print(result)