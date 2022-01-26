class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
                return [nums]

            res = []
            n = nums[-1]
            prev_perm = self.permute(nums[0:len(nums)-1])

            for perm in prev_perm:
                for i in range(len(perm)+1):
                    new_perm = perm[0:i] + [n] + perm[i:]
                    res.append(new_perm)

            return res
