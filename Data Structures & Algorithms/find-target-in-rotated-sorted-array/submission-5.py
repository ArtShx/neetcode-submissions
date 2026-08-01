class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        cutidx = 0
        while l < r:
            mid = l + (r-l) // 2
            print("CKP1", l, r, mid, nums[mid])
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        cutidx = l

        #print("\nCKP2", cutidx, l, r)
        def bsearch(l, r):
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] == target:
                    return mid
                
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return -1
        found = bsearch(0, cutidx-1)
        if found == -1:
            return bsearch(cutidx, len(nums)-1)
        return found
