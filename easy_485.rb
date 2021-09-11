# 485. Max Consecutive Ones

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

def find_max_consecutive_ones(nums)
  max_count = 0
  count = 0
  (0...nums.length).each do |i|
    if nums[i] == 0
      max_count = count if count > max_count
      count = 0
    else
      count +=1
      max_count = count if count > max_count
    end
  end
  max_count
end

nums = [1,1,0,1,1,1]
p find_max_consecutive_ones(nums)