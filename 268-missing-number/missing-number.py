class Solution(object):
    def missingNumber(self, nums):
        # n = len(nums)
        # return n * (n + 1) / 2 - sum(nums)

        for i in range(len(nums) +1):
            if i not in nums:
                return i