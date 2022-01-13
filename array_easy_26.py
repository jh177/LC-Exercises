def removeDuplicates(nums):
    if len(nums) == 0: return 0

    i = 0
    j = 1
    
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    return nums

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))