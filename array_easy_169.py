def majorityElement(nums):
    checked = {}

    for n in nums:
        if (n not in checked):
            checked[n] = 1
        else:
            checked[n] += 1
        if checked[n] > (len(nums)/2):
            return n

print(majorityElement([1]))