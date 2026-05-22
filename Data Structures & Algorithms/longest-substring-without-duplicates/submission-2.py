class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        charset = {}
        longest = 0
        current = 0
        left = 0
        for right, char in enumerate(s):
            
            if charset.get(char, -1) >= left:
                left = charset[char] + 1
            charset[char] = right
            current = right - left + 1
            longest = max(longest, current)
            
        return longest