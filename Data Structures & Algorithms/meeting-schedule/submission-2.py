"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev = 0
        sorted_intervals = sorted(intervals, key=lambda x: x.start)   
        for i in sorted_intervals:
            if prev <= i.end and prev <= i.start:
                prev = i.end
            else:
                return False
        return True
            