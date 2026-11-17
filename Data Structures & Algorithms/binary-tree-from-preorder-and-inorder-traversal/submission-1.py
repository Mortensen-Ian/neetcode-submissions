# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = dict()
        for i in range(len(inorder)):
            indices[inorder[i]] = i

        preIndex = 0
        def sprout(left, right):
            if left > right:
                return None
            nonlocal preIndex
            node = TreeNode(preorder[preIndex])
            mid = indices[preorder[preIndex]]
            preIndex+=1
            node.left = sprout(left, mid - 1)
            node.right = sprout(mid + 1, right)
            return node
        return sprout(0, len(inorder)-1)