class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dfs(l, r):
            if l == r:
                return piles[l]
            if (l, r) in memo:
                return memo[(l, r)]
            
            memo[(l, r)] = max(
                piles[l] - dfs(l+1, r),
                piles[r] - dfs(l, r-1),
            )

            return memo[(l, r)]

        out = dfs(0, len(piles)-1)
        #print(memo)
        return out > 0
