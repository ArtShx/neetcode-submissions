class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        last = nums[0] % 2 == 0
        for i in range(1, len(nums)):
            cur = nums[i] % 2 == 0
            if cur == last:
                return False
            last = cur
        return True