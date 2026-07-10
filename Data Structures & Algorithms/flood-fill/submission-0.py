class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_pixel = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        out = image.copy()
        queue = [[sr, sc]]
        visited = set()

        while queue:
            row, col = queue.pop()
            #print(row, col)
            if out[row][col] == start_pixel:
                out[row][col] = color
            visited.add((row, col))

            if row > 0 and out[row-1][col] == start_pixel and (row-1, col) not in visited:
                queue.append([row-1, col])
            if row < rows-1 and out[row+1][col] == start_pixel and (row+1, col) not in visited:
                queue.append([row+1, col])
            if col > 0 and out[row][col-1] == start_pixel and (row, col-1) not in visited:
                queue.append([row, col-1])
            if col < cols-1 and out[row][col+1] == start_pixel and (row, col+1) not in visited:
                queue.append([row, col+1])

        return out