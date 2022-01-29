def permuteUnique(nums, counted=set()):

    if len(nums) == 1:
        return [nums]

    res = []
    counted = set()
    n = nums[-1]
    prev_perm = permuteUnique(nums[0:len(nums)-1])

    for perm in prev_perm:
        for i in range(len(perm)+1):
            new_perm = perm[0:i] + [n] + perm[i:]
            # print(new_perm)
            combo = map(lambda i: str(i), new_perm)
            combo_str = "-".join(combo)
            if combo_str not in counted:
                res.append(new_perm)
            counted.add(combo_str)

    return res

nums = [1,1]
nums = [1, 2, 3]
print(permuteUnique(nums))