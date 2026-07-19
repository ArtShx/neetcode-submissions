class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        right = len(nums)-1
        i = 0
        while i <= right:
            #print(i, nums[i], right, k)
            if nums[i] == val:
                nums[i] = nums[right]
                right -= 1
            else:
                k+=1
                i+=1
        
        return k