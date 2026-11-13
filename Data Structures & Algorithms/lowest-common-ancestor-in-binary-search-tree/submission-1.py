# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        
        def dfs(root, p, q):
            if not root:
                return root
            if root is p or root is q:
                return root

            left = dfs(root.left, p, q)
            right = dfs(root.right,p, q)

            if (left and not right) or (not left and right) or (not left and not right):
                return left or right

            if left or right:
                return root
        return dfs(root,p,q)
            