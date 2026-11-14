# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, -1000000001, 1000000001)

    def valid(self, root, lower, upper):
        if root is None:
            return True
        elif root.val <= lower or root.val >= upper:
            return False
        else:
            return self.valid(root.left, lower, root.val) and self.valid(root.right, root.val, upper)