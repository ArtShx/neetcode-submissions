"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervalsarr = [(interval.start, interval.end) for interval in intervals]
        if len(intervals) == 0:
            return True
        intervalsarr.sort(key=lambda x: (x[0], x[1]))

        lastend = intervalsarr[0][1]
        for start, end in intervalsarr[1:]:
            if start < lastend:
                return False
            lastend = end
        return True