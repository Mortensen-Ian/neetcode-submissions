# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        boolList = [True]
        self.helper(root,boolList)
        return boolList[0]

    def helper(self, root, boolList):
        if not root:
            return 0
        l = self.helper(root.left, boolList)
        r = self.helper(root.right, boolList)
        if abs(l - r) > 1:
            boolList[0] = False
        return 1 + max(l, r)