# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def dfs(root):
            nonlocal ret 
            if not root:
                return 
            
            left = dfs(root.left) if root.left else 0
            right = dfs(root.right) if root.right else 0
            ret = max(ret, left + right)
            return max(left, right) + 1


        dfs(root)
        return ret