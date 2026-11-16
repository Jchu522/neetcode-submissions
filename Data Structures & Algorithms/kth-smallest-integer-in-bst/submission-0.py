# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minHeap = []
        queue = [root]
        k = k-1
        while queue:
            node = queue.pop(0)
            minHeap.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        heapq.heapify(minHeap)
        for i in range(k):
            heapq.heappop(minHeap)
        return minHeap[0]
        

