class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(index: int, arr: List[int], total: int):
            if total == target:
                ans.append(list(arr))
                return
            
            if total > target or index >= len(candidates):
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                arr.append(candidates[i])
                backtrack(i + 1, arr, total + candidates[i])
                arr.pop()

        backtrack(0, [], 0)
        return ans


        