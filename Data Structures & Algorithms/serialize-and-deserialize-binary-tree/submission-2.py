# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def serial(root):
            nonlocal res
            if root is None:
                res.append("N")
            else:
                res.append(str(root.val))
                serial(root.left)
                serial(root.right)
        serial(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        d = data.split(",")
        if not d:
            return None
        i = -1
        def grow():
            nonlocal d, i
            i += 1            
            if d[i] == "N":
                return None
            node = TreeNode(d[i], None, None)
            node.left = grow()
            node.right = grow()
            return node
        return grow()
