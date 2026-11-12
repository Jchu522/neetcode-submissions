import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]

        temp = [-x for x in nums]
        heapq.heapify(temp)

        for i in range(k):
            if i == k-1:
                return heapq.heappop(temp) * -1
            heapq.heappop(temp)
            

        