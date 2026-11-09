# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        seen = [(p, q)]
        
        while seen:
            
            node1, node2 = seen.pop(0)
            if node1.val != node2.val:
                return False
            
            if node1.left and not node2.left or node2.left and not node1.left:
                return False
            if node1.right and not node2.right or node2.right and not node1.right:
                return False
            
            seen.append((node1.left,node2.left)) if node1.left and node2.left else None
            seen.append((node1.right,node2.right)) if node1.right and node2.right else None

        return True
            
