class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        while k > 0:
            minval, idx = nums[0], 0
            for i in range(n):
                if nums[i] < minval:
                    idx = i
                    minval = nums[i]
                
            nums[idx] *= multiplier
            k-=1
        return nums
