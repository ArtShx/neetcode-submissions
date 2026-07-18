class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1 for _ in range(n)] for _ in range(m)]

        cache[0][0] = 1
        def dfs(r, c):
            
            if cache[r][c] != -1:
                return cache[r][c]
            a, b = 0, 0
            if r > 0:
                a = dfs(r-1, c)
            if c > 0:
                b = dfs(r, c-1)
            #print(r, c, a, b)
            cache[r][c] = a + b
            return cache[r][c]

        out = dfs(m-1, n-1)
        print(cache)
        return out