import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # you make a heap with the cooldown time (cooldown, "task")
        # increment your cycles each time you add a task or idle
        # we need to sort by count of the task
        cycle = 0
        count = {i:0 for i in range(ord('A'),ord('Z') + 1)}
        heap = []
        time = []
        queue = deque()
        for t in tasks:
            count[ord(t)] += 1

        for key, val in count.items():
            if val > 0:
                heapq.heappush(heap, [-val, chr(key)])

        
        while queue or heap:
            
            if queue:
                if queue[0][0]  == cycle:
                    x,y,z = queue.popleft() 
                    heapq.heappush(heap,[y,z])
            
            if heap:
                val1, key = heapq.heappop(heap) 
                val1 += 1
                if val1 < 0 :
                    queue.append([cycle + n + 1 , val1, key])
            cycle += 1
            


        return cycle 



