class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        i = 1
        total_merges = 0
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1] and intervals[i-1][0] <= intervals[i][1]:
                intervals[i-1][1] = max(intervals[i][1], intervals[i-1][1])
                del intervals[i]
            else:
                i+=1
        return intervals