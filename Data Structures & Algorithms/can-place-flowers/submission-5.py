class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        i = 0
        m = len(flowerbed)
        while i < m:
            #print(i)
            if flowerbed[i]:
                i += 2
                continue
            
            if (i < m-1 and flowerbed[i+1] == 0) or (i == m-1):
                n-=1
                if n == 0:
                    return True
                flowerbed[i] = 2
                i += 2
                continue
            i+=1
        #print(flowerbed)
        return False
            