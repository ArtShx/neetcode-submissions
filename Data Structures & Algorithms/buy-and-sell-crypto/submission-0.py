class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        n = len(prices)
        for l in range(n):
            for r in range(l+1, n):
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit, profit)
        return maxprofit