class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, k
        n = len(nums)
        firsttime = True
        numset = set()
        for r in range(n):
            #print(r)
            if r - l > k:
                numset.remove(nums[l])
                l+=1
            if nums[r] in numset:
                return True
            numset.add(nums[r])
            #print(numset)

        return False
