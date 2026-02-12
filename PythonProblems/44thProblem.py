def missing_number(nums):
    for i in range(len(nums)+1): 
        if i not in nums:
            return i



nums = [3,0,1]


print(missing_number(nums))