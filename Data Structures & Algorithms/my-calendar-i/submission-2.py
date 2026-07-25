class MyCalendar:
    
    def __init__(self):
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.intervals) == 0:
            self._add(startTime, endTime)
            return True

        for start, end in self.intervals:
            if start <= startTime < end or start < endTime < end or startTime <= start < endTime:
                return False
            if end < start:
                break

        self._add(startTime, endTime)
        return True
    
    def _add(self, start, end):
        self.intervals.append((start, end))
        self.intervals.sort(key=lambda x: (x[0], x[1]))
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)