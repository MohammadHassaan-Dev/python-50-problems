def majorityElement(nums):
    n = len(nums)
    maj_element = n / 2 
    count = {}
    for num in nums: 
        if num in count:
            count[num] += 1

        else:
            count[num] = 1

    for element in count:
        if count[element] > maj_element:
            return element

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
