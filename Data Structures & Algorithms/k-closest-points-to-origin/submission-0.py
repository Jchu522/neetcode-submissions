import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        ret = []
        for a,b in points:
            temp = (a**2 + b **2) ** .5
            minHeap.append((temp,a,b))

        heapq.heapify(minHeap)
        for i in range(k):
            temp,a,b = heapq.heappop(minHeap)
            ret.append((a,b))
        return ret
