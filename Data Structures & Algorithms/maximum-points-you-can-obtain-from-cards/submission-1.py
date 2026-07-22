class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l, r = 0, n-1
        sumprefixr = [0] * k
        sumprefixl = [0] * k
        sumprefixl[0] = cardPoints[0]
        sumprefixr[0] = cardPoints[-1]

        for i in range(1, k):
            sumprefixl[i] = sumprefixl[i-1] + cardPoints[i]
            sumprefixr[i] = sumprefixr[i-1] + cardPoints[n-i-1]

        # get only left or only right
        total = max(sumprefixl[-1], sumprefixr[-1])

        for i in range(k-1):
            total = max(
                sumprefixl[i] + sumprefixr[k-i-2],
                total
            )
            #print(i, k-i-2, total)

        #print(sumprefixl, sumprefixr)
        return total