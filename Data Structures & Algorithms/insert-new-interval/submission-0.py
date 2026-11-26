class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        start, end = newInterval
        for i in range(len(intervals)):
            if end < intervals[i][0]:
                ret.append(newInterval)
                return ret + intervals[i:]
            elif start > intervals[i][1]:
                ret.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        ret.append(newInterval)
        return ret
    