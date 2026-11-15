# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [0]
        node = []
        self.smallHelper(root, counter, node, k)
        return node[0]

    def smallHelper(self, root, counter, node, k):
        if root is None:
            return
        else:
            self.smallHelper(root.left, counter, node, k)
            counter[0] += 1
            if counter[0] == k:
                node.append(root.val)
            else:
                self.smallHelper(root.right, counter, node, k)
            