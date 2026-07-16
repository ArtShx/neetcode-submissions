class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [
            (0, 1), # right
            (1, 0), # down
            (0, -1), # left
            (-1, 0), # up
        ]
        #visited = [[False for _ in range(cols)] for _ in range(rows)]
        def dfs(r, c):
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"
            
            for rowdir, coldir in directions:
                newrow = r + rowdir
                newcol = c + coldir
                if newrow < 0 or newrow == rows or newcol < 0 or newcol == cols:
                    continue
                dfs(newrow, newcol)
        
        total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    total += 1
                    dfs(r, c)
        return total