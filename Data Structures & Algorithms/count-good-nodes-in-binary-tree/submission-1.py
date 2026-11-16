# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        ret = 0

        def dfs(maxRoot, root):
            nonlocal ret
            if not root:
                return
            if maxRoot <= root.val:

                ret += 1
                maxRoot = root.val
            dfs(maxRoot, root.left)
            dfs(maxRoot, root.right)
            

        dfs(root.val, root)

        return ret
