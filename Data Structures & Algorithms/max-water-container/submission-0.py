class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        area = 0
        maxarea = 0

        while l < r:
            h = min(heights[l], heights[r])
            area = h * (r-l)
            maxarea = max(maxarea, area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxarea
