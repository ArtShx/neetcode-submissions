class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arrleft = [0] * n
        arrright = [0] * n

        arrleft[0] = nums[0]
        arrright[-1] = nums[-1]

        for i in range(1, n):
            arrleft[i] = arrleft[i-1] * nums[i]
            arrright[-i-1] = arrright[-i] * nums[-i-1]
        
        #print(arrleft, arrright)
        out = [0] * n
        out[0] = arrright[1]
        out[-1] = arrleft[-2]
        for i in range(1, n-1):
            out[i] = arrleft[i-1] * arrright[i+1]
        return out