"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervalsarr = [(interval.start, interval.end) for interval in intervals]
        if len(intervals) == 0:
            return 0
        intervalsarr.sort(key=lambda x: (x[0], x[1]))

        lastend = intervalsarr[0][1]
        rooms = [lastend]
        #res = 1
        for start, end in intervalsarr[1:]:
            foundroom = False
            for i in range(len(rooms)):
                if start < rooms[i]:
                    continue
                foundroom = True
                rooms[i] = end
                break
            if not foundroom:
                rooms.append(end)
                #res = max(res, len(rooms))

        return len(rooms)