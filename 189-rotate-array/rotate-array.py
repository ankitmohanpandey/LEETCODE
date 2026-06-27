class Solution:
    def rotate(self, nums, k):
        n = len(nums)

        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1
        reverse(0, n - 1)

        # Step 2
        reverse(0, k - 1)

        # Step 3
        reverse(k, n - 1)