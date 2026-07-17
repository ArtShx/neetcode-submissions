class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return max(nums)
        
        cache = [-1] * (n+1)
        cache[0] = nums[0]
        cache[1] = max(nums[1], nums[0])

        def calc(i):
            if not (0 <= i < n):
                return -float("inf")
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(
                calc(i-2) + nums[i],
                calc(i-1), 
                #calc(i-3) + nums[i],
                
            )
            return cache[i]
        
        out =  calc(n-1)
        #print(cache)
        return out