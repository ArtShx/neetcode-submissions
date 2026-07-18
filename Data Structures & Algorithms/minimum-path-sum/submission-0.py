class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        cache[0][0] = grid[0][0]

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return float("inf")
            #print(r, c)
            if cache[r][c] != -1:
                return cache[r][c]
            
            cache[r][c] = min(
                dfs(r-1, c),
                dfs(r, c-1)
            ) + grid[r][c]
            return cache[r][c]
        #print(cache)
        return dfs(m-1, n-1)