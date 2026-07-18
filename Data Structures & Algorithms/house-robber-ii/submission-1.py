class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 0:
            return 0
        if n == 2:
            return max(nums)

        arr1 = nums[:-1]
        arr2 = nums[1:]

        cache1 = [-1] * (n-1)
        cache1[0] = nums[0]
        cache1[1] = max(nums[0], nums[1])

        cache2 = [-1] * (n-1)
        cache2[0] = nums[1]
        cache2[1] = max(nums[1], nums[2])

        def dfs(i, arr, cache):
            if i < 0 or i >= n-1:
                return -float("inf")
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(
                dfs(i-2, arr, cache) + arr[i],
                dfs(i-1, arr, cache)
            )
            return cache[i]
        
        out1 = dfs(n-2, arr1, cache1)
        out2 = dfs(n-2, arr2, cache2)
        #print(cache1, cache2)
        return max(out1, out2)