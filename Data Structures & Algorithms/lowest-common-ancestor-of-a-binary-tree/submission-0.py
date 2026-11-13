# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        def dfs(root,p,q):
            if not root:
                return root
            if root is p or root is q:
                return root

            left = dfs(root.left, p ,q)
            right = dfs(root.right,p,q)

            if (left and not right) or (right and not left) or (not right and not left):
                return left or right
            if left or right:
                return root
        return dfs(root,p,q)
