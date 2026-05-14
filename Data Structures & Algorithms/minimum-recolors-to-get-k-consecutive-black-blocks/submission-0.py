class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        res = float("inf")
        n = len(blocks)
        total_black = total_white = 0
        for r in range(n):
            if r - l >= k:
                if blocks[l] == "W":
                    total_white -= 1
                else:
                    total_black -= 1
                l+=1
            
            if blocks[r] == "W":
                total_white += 1
            else:
                total_black += 1
            res = min(res, k-total_black)
            #print(r, res, total_white, total_black)


        return res