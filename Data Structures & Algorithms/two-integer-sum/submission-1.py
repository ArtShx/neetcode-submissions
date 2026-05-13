class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hmap = {}
        for i in range(n):
            #print(hmap)
            remain = target - nums[i]
            if nums[i] in hmap:
                return [hmap[nums[i]], i]
            hmap[remain] = i