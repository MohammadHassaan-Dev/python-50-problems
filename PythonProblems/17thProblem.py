def smaller_than_current_num(nums):
    smaller = []
    for i in nums: 
        count = 0
        for j in nums:
            if i>j: 
                count += 1

        smaller.append(count)

    return smaller

nums = [8,1,2,2,3]
print(smaller_than_current_num(nums))