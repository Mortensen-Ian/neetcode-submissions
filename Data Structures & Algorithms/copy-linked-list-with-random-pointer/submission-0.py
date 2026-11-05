"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = dict()
        return self.Build(head, visited)

    def Build(self, curNode, visited):
        if curNode:
            if curNode not in visited:
                newNode = Node(curNode.val, None, None)
                visited[curNode] = newNode
                newNode.random = self.Build(curNode.random, visited)
                newNode.next = self.Build(curNode.next, visited)
                return newNode
            else:
                return visited[curNode]
        