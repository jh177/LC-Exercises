def removeElement(nums, val):
    if len(nums) == 0: return 0
    # if len(nums) == 1 and nums[0] != val: return 1

    i = 0
    j = 1
    k = 0
    
    while i < len(nums):
        if nums[i] == val and j >= len(nums):
            i += 1
        elif nums[i] == val and nums[j] != val:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
            k += 1
        elif nums[i] != val:
            i += 1
            j += 1
            k += 1
        else:
            j += 1
        
    return k


print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(removeElement([0, 0, 1], 2))
