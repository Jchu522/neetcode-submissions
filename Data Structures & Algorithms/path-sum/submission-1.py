# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = [(root, targetSum - root.val)]
        while queue:
            root, curr = queue.pop(0)
            if curr == 0 and not root.left and not root.right:
                return True
            if root.left:
                queue.append((root.left, curr-root.left.val))
            if root.right:
                queue.append((root.right, curr-root.right.val))

        return False
            
            
            



        # if not root:
        #     return False

        # def dfs(root: Optional[TreeNode], curr_sum: int):
        #     if not root:
        #         return False

        #     curr_sum += root.val 
        #     if not root.left and not root.right:
        #         return curr_sum == targetSum

        #     left =  dfs(root.left, curr_sum) if root.left else False
        #     right =  dfs(root.right, curr_sum) if root.right else False
        #     return left or right



        # return dfs(root, 0)


