def singleNumber(nums):
    checked = {}
    for num in nums:
        if num not in checked:
            checked[num] = 1
        else:
            checked[num] -= 1
    
    for k, v in checked.items():
        if v == 1:
            return k

print(singleNumber([4,1,2,1,2]))