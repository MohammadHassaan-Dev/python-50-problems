def find_nums_with_digits(nums):
    count = 0
    for num in nums: #"1"
        num = str(num)
        if len(num) %2 == 0:
            count += 1

    return count

nums = [555,901,482,1771] 
print(find_nums_with_digits(nums))
