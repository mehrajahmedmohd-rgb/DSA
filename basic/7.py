prefix=[]
suffix=[]
nums = [1,2,3,4]

current_prefix=1
for i in nums:
    prefix.append(current_prefix)
    current_prefix *= i
print(prefix)

current_suffix = 1
for i in range(len(nums)-1,-1,-1):
    suffix.append(current_suffix)
    current_suffix *= nums[i]

for i in range(len(nums)):
    print(i)

print(suffix)
