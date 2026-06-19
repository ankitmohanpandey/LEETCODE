# Question: https://leetcode.com/problems/container-with-most-water/
#
# Approach:
# Step 1: Two pointers at ends (left & right)
#
# Step 2: Calculate area = min(height[left], height[right]) * width
#
# Step 3: Move pointer with smaller height
#
# Step 4: Keep track of max area
#
# Step 5: Repeat until pointers meet


class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        lpointer = height[0]
        rpointer = height[-1]
        result = min(lpointer, rpointer) * (len(height) - 1)
        while l < r:
            if lpointer < rpointer:
                l += 1
                lpointer = height[l]
                new_area = min(lpointer, rpointer) * (r - l)
                if new_area > result:
                    result = new_area

            else:
                r -= 1
                rpointer = height[r]
                new_area = min(lpointer, rpointer) * (r - l)
                if new_area > result:
                    result = new_area

        return result
