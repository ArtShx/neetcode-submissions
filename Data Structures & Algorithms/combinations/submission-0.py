class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []

        def backtrack(arr: List[int], index: int):
            if len(arr) == k:
                out.append(list(arr))
                return
            
            for i in range(index, n+1):
                arr.append(i)
                backtrack(arr, i+1)
                arr.pop()

        backtrack([], 1)
        return out