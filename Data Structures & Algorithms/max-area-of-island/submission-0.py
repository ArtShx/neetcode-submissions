class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def find_area(row, col, cur_area):
            if grid[row][col] == 0:
                return cur_area
            cur_area += 1
            visited[row][col] = True
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for rd, cd in directions:
                r = row + rd
                c = col + cd
                if r < 0 or r == rows or c < 0 or c == cols:
                    continue
                if visited[r][c]:
                    continue
                cur_area = find_area(r, c, cur_area)
            return cur_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    area = find_area(r, c, 0)
                    #print(r, c, area)
                    maxarea = max(area, maxarea)
                    visited[r][c] = True
        return maxarea