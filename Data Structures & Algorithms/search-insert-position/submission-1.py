class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = l + (r-l)//2
            #print(f"{l=} {mid=} {r=} {nums[mid]=}")
            if nums[mid] == target:
                return mid
            if nums[mid] < target and mid+1 < n and target < nums[mid+1]:
                return mid+1
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        if r < 0:
            return 0
        return n