class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: (x[0], x[1]))

        n = len(intervals)
        i = 1
        while i < n:
            if intervals[i-1][0] <= intervals[i][1] and intervals[i][0] <= intervals[i-1][1]:
                #print(intervals[i-1], intervals[i])
                intervals[i-1][0] = min(intervals[i-1][0], intervals[i][0])
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                del intervals[i]
                n -= 1
            else:
                i+=1


        return intervals
