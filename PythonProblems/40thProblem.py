def find_numbers(nums):
    count = 0
    for num in nums: #"12" return 2
        if len(str(num)) %2 == 0:
            count += 1

    return count



nums = [12,345,2,6,7896]
print(find_numbers(nums))