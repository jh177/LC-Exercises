def twoSum(numbers, target):
    # checked = {}
    
    # for i, n in enumerate(numbers):
    #     if (n not in checked):
    #         checked[target - n] = i
    #     else:
    #         return [checked[n]+1, i+1]

    l = 0
    r = len(numbers)-1

    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l+1, r+1]


print(twoSum([2,7,11,15], 9))