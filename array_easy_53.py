# maximum subarray

def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        if current_sum < 0: current_sum = 0
        current_sum += nums[i]
        if current_sum > max_sum: max_sum = current_sum

    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))