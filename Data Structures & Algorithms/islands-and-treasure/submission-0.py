class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        stack = []
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    stack.append((i, j, 0))
        
        inf = 2147483647

        while stack:
            r, c, d = stack.pop(0)
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == -1 or (0 < grid[r][c] < inf):
                continue
            if grid[r][c] > 0:
                grid[r][c] = min(d, grid[r][c])
            d+=1
            stack.append((r+1, c, d))
            stack.append((r, c-1, d))
            stack.append((r-1, c, d))
            stack.append((r, c+1, d))
        return