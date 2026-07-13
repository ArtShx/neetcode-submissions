import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        
        while k:
            k-=1
            gift = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int(gift ** 0.5))

        return sum(-g for g in gifts)
        