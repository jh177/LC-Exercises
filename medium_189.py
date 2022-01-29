def rotate(nums, k):
    if k == 0: return nums

    if k > 0:
        for i in range(k):
            n = nums.pop()
            nums.insert(0,n)
    
    if k < 0:
        for i in range(-k):
            n = nums.pop(0)
            nums.append(n)