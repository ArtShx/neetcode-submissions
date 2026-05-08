class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        if k == len(nums):
            return
    
        k %= len(nums)
        #print(nums, k)
        #print(nums[k:] + nums[:k])
        nums[:] = nums[-k:] + nums[:-k]
        #print("CKP", nums)
        return
