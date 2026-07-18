class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        cache = [float("inf")] * (amount+1)
        
        def helper(remain):
            if remain == 0:
                return 0
            if cache[remain] != float("inf"):
                return cache[remain]
            
            min_coins_so_far = float("inf")
            for coin in coins:
                if remain-coin >= 0:
                    sub_res = helper(remain-coin)
                    if sub_res != -1:
                        min_coins_so_far = min(min_coins_so_far, sub_res+1)
            cache[remain] = min_coins_so_far if min_coins_so_far != float("inf") else -1
            return cache[remain]
        helper(amount)
        #print(cache)
        return cache[amount] if cache[amount] != float("inf") else -1
