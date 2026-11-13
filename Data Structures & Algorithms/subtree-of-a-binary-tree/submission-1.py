# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        d = deque([root])
        while d:
            for i in range(len(d)):
                n = d.popleft()
                if self.TreeEqual(n, subRoot):
                    return True
                if n.left:
                    d.append(n.left)
                if n.right:
                    d.append(n.right)
        return False

    def TreeEqual(self, root1, root2):
        if root1 is None or root2 is None:
            return root1 is None and root2 is None
        elif root1.val == root2.val:
            return self.TreeEqual(root1.left, root2.left) and self.TreeEqual(root1.right, root2.right)
        else:
            return False