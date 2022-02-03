class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        n = len(nums)
        count = 0

        for i in range(len(nums)-2):
            for j in range(i+3, n+1):
                sub_arr = nums[i:j]
                if self.arithmetic(sub_arr) is False:
                    break
                if self.arithmetic(sub_arr):
                    count += 1

        return count

    def arithmetic(self, arr):
        diff = arr[0] - arr[1]
        for i in range(1, len(arr)-1):
            if arr[i] - arr[i+1] != diff:
                return False
        return True
