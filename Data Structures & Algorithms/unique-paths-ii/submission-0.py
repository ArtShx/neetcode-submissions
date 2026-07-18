class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        cache[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        #print(cache)
        """
        -1 = new path
        -2 = obstacle
        n
        """

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            if cache[r][c] >= 0:
                return cache[r][c]
            value = obstacleGrid[r][c]
            if value == 1:
                cache[r][c] = -2
                return cache[r][c]
            a = dfs(r-1, c)
            b = dfs(r, c-1)
            res = 0
            if a > 0:
                res += a
            if b > 0:
                res += b
            cache[r][c] = res
            return cache[r][c]
        
        return max(dfs(m-1, n-1), 0)