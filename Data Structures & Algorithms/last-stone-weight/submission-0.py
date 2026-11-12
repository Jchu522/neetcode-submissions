import heapq
import math
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp = [-x for x in stones]
        heapq.heapify(temp)
        
        while len(temp) > 1 :
            a = -1 * heapq.heappop(temp)
            b = -1 * heapq.heappop(temp)
            if a == b:
                continue
            else:
                a = abs(a-b) * -1
                heapq.heappush(temp, a)
        
        if temp:
            return temp[0] * -1
        else:
            return 0
        

            

        
        
