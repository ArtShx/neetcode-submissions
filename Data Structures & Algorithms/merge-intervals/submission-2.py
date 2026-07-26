class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        i = 1
        write_idx = 0
        for read_idx in range(1, len(intervals)):
            if intervals[write_idx][0] <= intervals[read_idx][1] and intervals[read_idx][0] <= intervals[write_idx][1]:
                intervals[write_idx][1] = max(intervals[write_idx][1], intervals[read_idx][1])
            else:
                write_idx += 1
                intervals[write_idx] = intervals[read_idx]
        return intervals[:write_idx+1]