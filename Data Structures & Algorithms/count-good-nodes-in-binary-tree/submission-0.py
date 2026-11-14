# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGoodNodes(root, -101)

    def countGoodNodes(self, root, m):
        if root is None:
            return 0
        elif root.val >= m:
            return 1 + self.countGoodNodes(root.left, root.val) + self.countGoodNodes(root.right, root.val)
        else:
            return self.countGoodNodes(root.left, m) + self.countGoodNodes(root.right, m)