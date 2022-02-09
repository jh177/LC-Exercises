# using recursion
# [1] => [[],[1]]
# [1,2] => [[], [1], [2], [1,2]]
# [1,2,3] => 2^(n-1) O(n*2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [[],nums]
        
        new_result = []
        new_ele = nums.pop()
        prev_result = self.subsets(nums)
        for subset in prev_result:
            new_result.append(subset + [new_ele])
        
        return prev_result + new_result