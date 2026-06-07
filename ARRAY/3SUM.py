#question :- https://leetcode.com/problems/3sum/description/
# Step 1: Sort the array
#
# Step 2: Fix one number
#
# Step 3: Use two fingers (left & right)
#
# Step 4:
# Sum small → move left
#
# Sum big → move right
#
# Sum = 0 → found answer


class Solution(object):
    def threeSum(self, nums):

        nums.sort()

        result = []

        for i in range(len(nums)):

            # Skip duplicate starting numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append(
                        [nums[i], nums[left], nums[right]]
                    )

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result