class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = dict()
        self.left = Node(0, None, -2)
        self.right = Node(0, -1, None)
        self.d[-1] = self.left
        self.d[-2] = self.right

    def get(self, key: int) -> int:
        if not key in self.d:
            return -1
        GetNode = self.d[key]
        self.put(key, GetNode.value)
        return GetNode.value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(key)
            self.cap += 1
        self.d[key] = Node(value, self.right.left, -2)
        self.d[self.right.left].right = key
        self.right.left = key
        self.cap -= 1
        if self.cap < 0:
            self.remove(self.left.right)
            self.cap += 1

    def remove(self, key):
        delNode = self.d[key]
        self.d[delNode.left].right = delNode.right
        self.d[delNode.right].left = delNode.left
        del self.d[key]