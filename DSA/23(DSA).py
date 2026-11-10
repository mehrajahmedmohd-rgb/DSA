def product_of_array(nums):
    prefix=[]
    suffix=[]
    answer=[]
    current_prefix=1
    for i in nums:
        prefix.append(current_prefix)
        current_prefix *= i

    current_suffix = 1
    for i in range(len(nums)-1,-1,-1):
        suffix.append(current_suffix)
        current_suffix *= nums[i]

    suffix=suffix[::-1]

    for i in range(len(nums)):
        answer.append(prefix[i] * suffix[i])

    return answer

nums= list(map(int,input("enter the number:").split()))
result = product_of_array(nums)
print(result)