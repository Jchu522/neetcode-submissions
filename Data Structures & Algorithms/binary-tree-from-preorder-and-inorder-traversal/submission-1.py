# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        n = len(preorder)
        inH = {}
        for i in range(n):
            inH[inorder[i]] = i

        # def helper(prestart, preend, instart, inend):
        #     print(preorder)
        #     print(prestart)
        #     root = preorder[prestart]
        #     new_place = inH[root]
        #     print("root =", root, "at", new_place)
        #     # print("preorder full", preorder)
        #     # print("inorder full", inorder)
        #     print("preorder", preorder[prestart:preend])
        #     print("inorder", inorder[instart:inend])
        #     print()
            
        #     if prestart-preend == 0:
        #         return None
            
        #     if prestart-preend == 1:
        #         return TreeNode(root)
            
        #     print("left", prestart+1 >= n)
        #     print(prestart, n)
        #     if prestart+1 >= n:
        #         left = None
        #     else:
        #         left = helper(prestart + 1, new_place + 1, prestart, new_place)
        #     print("right")
        #     if new_place + 2 >= n:
        #         right = None
        #     else:
        #         right = helper(new_place + 2, n, new_place + 2, n)

        #     return TreeNode(root, left, right)

        # return helper(0, n, 0, n)

        def helper(prestart, preend, instart, inend):
            if prestart >= preend:
                return None

            root_val = preorder[prestart]
            mid = inH[root_val]
            left_size = mid - instart

            left = helper(prestart + 1, prestart + 1 + left_size, instart, mid)
            right = helper(prestart + 1 + left_size, preend, mid + 1, inend)

            return TreeNode(root_val, left, right)

        return helper(0, n, 0, n)
