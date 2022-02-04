class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        longest = 0

        for n in n_set:
            if n-1 not in n_set:
                num = n
                streak = 1

                while num+1 in n_set:
                    num +=1
                    streak += 1

                longest = max(longest, streak)
    
        return longest

        
        # if len(nums) == 0: return 0
        # if len(nums) == 1: return 1

        # sorted_nums = sorted(list(set(nums)))

        # slow = 0
        # fast = 0
        # max_len = 1

        # while fast < len(sorted_nums)-1:
        #     if sorted_nums[fast+1] - sorted_nums[fast] == 1:
        #         fast += 1
        #         max_len = max(fast-slow+1, max_len)
        #     else:
        #         fast += 1
        #         slow = fast
        
        # return max_len