import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] # min heap
        self.big = [] # max heap
        

    def addNum(self, num: int) -> None:

        heapq.heappush(self.small, num * -1)
        if self.small and self.big and (-self.small[0] > self.big[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        if len(self.small) > len(self.big) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        elif len(self.big) > len(self.small):
            val = heapq.heappop(self.big)
            heapq.heappush(self.small, -val)


        
    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            median =  self.small[0] * - 1
        else:
            median = ((self.small[0] * -1) + (self.big[0])) / 2 

    
        return median
        
        