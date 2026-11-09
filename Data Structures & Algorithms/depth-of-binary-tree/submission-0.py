# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ret = 0


        def dfs(node: Optional[TreeNode], cur:int):
            if not node:
                return cur
            cur += 1
            return max((dfs(node.left, cur)), ((dfs(node.right, cur))))

        
        return dfs(root, ret)
