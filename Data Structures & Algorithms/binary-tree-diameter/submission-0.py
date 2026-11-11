# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.dfs(root, 0, diameter)
        return diameter[0]
        
    def dfs(self, root, level, m):
        if not root:
            return 0
        l = self.dfs(root.left, level + 1, m)
        r = self.dfs(root.right, level +1, m)
        nodecount = max(l, r)
        m[0] = max(m[0],l+r, level + nodecount)
        return nodecount + 1

