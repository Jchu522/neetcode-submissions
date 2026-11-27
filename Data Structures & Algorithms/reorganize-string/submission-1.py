import heapq
from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        count = {}
        ret = []
        for ch in s:
            count[ch] = 1 + count.get(ch, 0)

        for key, val in count.items():
            heapq.heappush(maxHeap, (-val,key))
        hold = []
        while maxHeap:
            val, ch = heapq.heappop(maxHeap)
            ret.append(ch)
            val += 1
            if val == 0:
                if hold:
                    prev_val, prev_ch = hold.pop(0)
                    heapq.heappush(maxHeap, (prev_val, prev_ch))
                continue
            hold.append((val,ch))
            if len(hold) > 1:
                prev_val, prev_ch = hold.pop(0)
                heapq.heappush(maxHeap, (prev_val, prev_ch))
        

        if hold:
            if hold[0][0] < -1:
                return ""
            elif hold[0][1] == ret[-1]:
                return ""
            else:
                ret.append(hold[0][1])
        return "".join(ret)
            
            


        
        

        