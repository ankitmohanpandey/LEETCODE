# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         max_length = 0 
#         st = ""
#         for i in s:
#             if i in st:
#                 st = st[st.index(i) + 1:]
#             st += i
#             max_length = max(max_length, len(st))
#         return max_length
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        seen = set()      # Store unique characters
        left = 0          # Left side of window
        longest = 0       # Best answer

        for right in range(len(s)):

            # Remove characters until duplicate disappears
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add current character
            seen.add(s[right])

            # Update maximum length
            longest = max(longest, right - left + 1)

        return longest