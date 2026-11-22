from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key in self.timeMap:
            times = self.timeMap[key]
            l, r = 0, len(times) - 1
            
            while r >= l:
                mid = (r + l) // 2
                res = times[mid][1]
                if res == timestamp:
                    return times[mid][0]
                elif res > timestamp:
                    r = mid - 1
                else:
                    result = times[mid][0]
                    l = mid + 1
            
        return result
        
