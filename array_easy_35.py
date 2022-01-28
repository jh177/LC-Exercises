def searchInsert(nums, target):
    l = 0
    r = len(nums)-1

    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return l

    # if len(nums) == 0: return 0

    # mid_idx = len(nums) // 2

    # left = nums[:mid_idx]
    # right = nums[mid_idx+1:]

    # if nums[mid_idx] == target:
    #     return mid_idx
    # elif nums[mid_idx] > target:
    #     return searchInsert(left, target)
    # else:
    #     result = searchInsert(right, target)
    #     return result + 1 + mid_idx

print(searchInsert([1,3,5,6], 7))