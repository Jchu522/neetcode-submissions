class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    
    def insert(self, node):
        nxt = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:

            node = self.cache[key]
            node.val = value
            if key in self.cache:
                self.remove(self.cache[key])
                self.insert(self.cache[key])
        else:

            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            
            if len(self.cache) > self.cap:
                lru = self.right.prev
                self.remove(lru)
                del self.cache[lru.key]
            
            
        
