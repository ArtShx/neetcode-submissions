class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        solution = False
        n = len(board)
        m = len(board[0])

        directions = [
            (0, 1),  # right
            (1, 0), # down
            (0, -1),  # left
            (-1, 0), # up
        ]
        
        def dfs(arr, i, r, c, visited):
            nonlocal solution
            #print("CKP1", arr, i, r, c)
            if len(arr) == len(word) or i == len(word):
                if "".join(arr) == word:
                    solution = True
                    return True
                return False
            if solution:
                return True
            if r < 0 or r >= n or c < 0 or c >= m or i >= len(word):
                return False
            
            if board[r][c] != word[i]:
                return False

            #print(arr, r, c)
            arr.append(board[r][c])
            visited.add((r, c))
            if len(arr) == len(word):
                if "".join(arr) == word:
                    solution = True
                    return True
                return False

            for dr, dc in directions:
                if (r+dr, c+dc) in visited:
                    continue
                if dfs(arr[:], i+1, r+dr, c+dc, visited):
                    return True
            visited.remove((r, c))
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs([], 0, i, j, set()):
                        return True
        return False
