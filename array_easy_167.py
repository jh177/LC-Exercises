def twoSum(numbers, target):
    checked = {}
    
    for i, n in enumerate(numbers):
        if (n not in checked):
            checked[target - n] = i
        else:
            return [checked[n]+1, i+1]


print(twoSum([2,7,11,15], 9))