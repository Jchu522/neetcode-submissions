"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        res, count = 0,0

        
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        if len(start) == 1 and len(end) == 1:
            return 1
        l = 0
        r = 0
        while l < len(intervals) and r < len(intervals):
            res = max(count,res)
            if start[l] < end[r]:
                count += 1
                l+=1
            else:
                count -= 1
                r+=1
        res = max(count,res) 
        return res
            

            
            

        
