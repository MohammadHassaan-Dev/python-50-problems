def SingleNumber(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num

        

    

nums = [2,2,1]
print(SingleNumber(nums))