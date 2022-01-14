def searchInsert(nums, target):
    if len(nums) == 0: return 0

    mid_idx = len(nums) // 2

    left = nums[:mid_idx]
    right = nums[mid_idx+1:]

    if nums[mid_idx] == target:
        return mid_idx
    elif nums[mid_idx] > target:
        return searchInsert(left, target)
    else:
        result = searchInsert(right, target)
        return result + 1 + mid_idx

print(searchInsert([1,3,5,6], 7))