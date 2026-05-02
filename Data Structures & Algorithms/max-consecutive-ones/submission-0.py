class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                ans = max(ans, current)
            else:
                current = 0
        return ans