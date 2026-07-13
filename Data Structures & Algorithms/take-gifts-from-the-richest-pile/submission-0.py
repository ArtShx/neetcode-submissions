import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        
        while k:
            k-=1
            gift = -heapq.heappop(gifts)
            new = math.floor(math.sqrt(gift))
            heapq.heappush(gifts, -new)

        total = 0
        for g in gifts:
            total+=-g
        return total