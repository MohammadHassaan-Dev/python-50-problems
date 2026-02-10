def createTargetArray(nums, index):
    ans = []
    for i in range(len(nums)):
        ans.insert(index[i], nums[i])

    return ans

nums = [1,2,3,4,0]
index = [0,1,2,3,0]
print(createTargetArray(nums, index))