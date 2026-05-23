class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.cache = {}
        self.start, self.end = Node(0, 0), Node(0, 0)
        self.start.right = self.end
        self.end.left = self.start
    
    def remove(self, node: Node):
        node.left.right = node.right
        node.right.left = node.left

    def add(self, node: Node):
        prev = self.end.left
        prev.right, node.left = node, prev
        self.end.left = node
        node.right = self.end


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            removed = self.start.right
            self.remove(removed)
            del self.cache[removed.key]
