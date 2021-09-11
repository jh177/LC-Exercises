# 674. Longest Continuous Increasing Subsequence

# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

# A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
# 4.

def find_length_of_lcis(nums)
  longest = 1
  count = 1
  (1...nums.length).each do |i|
    if nums[i] > nums[i-1]
      count += 1
      longest = count if count > longest
    else
      count = 1
    end
  end
  longest
end

n1 = [1,3,5,4,7]
n2 = [2,2,2,2,2]

p find_length_of_lcis(n1)
p find_length_of_lcis(n2)