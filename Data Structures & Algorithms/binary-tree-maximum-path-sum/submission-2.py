# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = root.val
        
        def maxSum(root):
            if root is None:
                return 0
            leftSum = maxSum(root.left)
            rightSum = maxSum(root.right)
            localMax = root.val + max(0, leftSum, rightSum)
            nonlocal m
            m = max(m, localMax, leftSum + root.val + rightSum)
            return localMax
        maxSum(root)
        return m