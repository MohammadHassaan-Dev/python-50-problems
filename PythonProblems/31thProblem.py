def sorted_squares(nums):
    squared_array = [] 
    for i in nums:  
        squared_array.append(i*i)

    squared_array.sort()
    
    return squared_array

nums = [-7,-3,2,3,11]
print(sorted_squares(nums))