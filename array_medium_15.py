def threeSum(nums):
    sorted_nums = sorted(nums)
    res = []

    for i in range(0, len(sorted_nums)):

        if i and sorted_nums[i] == sorted_nums[i-1]: continue

        j = i+1
        k = len(sorted_nums)-1

        target = -sorted_nums[i]

        print(target)

        while j < k:
            if sorted_nums[j]+sorted_nums[k] > target:
                k -= 1
            elif sorted_nums[j]+sorted_nums[k] < target:
                j += 1
            else:
                res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                while j<k and sorted_nums[j] == sorted_nums[j+1]:
                    j += 1
                while j<k and sorted_nums[k] == sorted_nums[k-1]:
                    k -= 1
                j += 1
                k -= 1

    return res


nums = [-1,0,1,2,-1,-4]
# nums = [-1,0,1,2,-1,-4]
# nums = [1, 2, -2, -1]
# nums = [3, 0, -2, -1, 1, 2]
# nums = [-1, 0, 1]
# nums = [0, 0, 0]
# nums = [-2, 0, 1, 1, 2]
print(threeSum(nums))