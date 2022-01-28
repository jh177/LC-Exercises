def rotate(nums, k):
    if k == 0: return nums

    if k > 0:
        l = 0
        r = l+k
        while r < len(nums):
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
    
    if k < 0:
        r = len(nums)-1
        l = r + k
        while l > -1:
            nums[l], nums[r] = nums[r], nums[l]
            l -= 1
            r -= 1

    return nums