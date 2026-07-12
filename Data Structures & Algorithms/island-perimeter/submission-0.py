class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def dfs(row, col, perimeter):
            #print("new dfs", row, col, perimeter)
            if visited[row][col]:
                return perimeter
            if grid[row][col] != 1:
                return perimeter + 1
            #print("ckp1", row, col, perimeter)
            visited[row][col] = True
            directions = [[row-1, col], [row, col+1], [row+1, col], [row, col-1]]
            for r, c in directions:
                
                if r < 0 or r == rows or c < 0 or c == cols:
                    # hit a wall
                    perimeter += 1
                    #print("add", r, c, perimeter)
                    continue
                perimeter = dfs(r, c, perimeter)
            return perimeter
        
        ri = None
        ci = None
        for r in range(rows):
            if ri and ci:
                break
            for c in range(cols):
                if grid[r][c] == 1:
                    ri = r
                    ci = c
                    break

        return dfs(ri, ci, 0)