class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h_sorted = sorted(heights)
        out = 0

        for i in range(len(heights)):
            if h_sorted[i] != heights[i]:
                out+=1
        return out