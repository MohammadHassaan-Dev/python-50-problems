def find_nums_with_digits(nums):
    list1 = []
    for num in nums:
        count = 0
        for i in nums: 
            if i<num:
                count += 1
        list1.append(count)

    return list1

nums = [8,1,2,2,3]
print(find_nums_with_digits(nums))
