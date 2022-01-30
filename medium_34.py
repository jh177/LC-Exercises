def searchRange(nums, target):
    if len(nums) == 0: return [-1,-1]

    first = searchFirst(nums, target)
    if first == -1: return [-1,-1]

    last = searchLast(nums, target)

    return [first, last]



def searchFirst(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            r = mid - 1

    if l < len(nums) and nums[l] == target:
        return l
    return -1


def searchLast(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    if r >=0 and nums[r] == target:
        return r
    return -1
