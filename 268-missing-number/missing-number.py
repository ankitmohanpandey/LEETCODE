class Solution(object):
    def missingNumber(self, nums):
        # num = len(nums)
        for i in range(len(nums) +1):
            if i not in nums:
                return i