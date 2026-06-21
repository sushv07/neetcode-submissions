# O(1) TC for get and put / O(n) SC - hash map
# Node Class - storing key and value
# Pointers for prev and next nodes
class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # hash map to map key to respective node

        #dummy nodes to help insert and remove operations
        self.left, self.right = Node(0, 0), Node(0, 0)
        #pointers for dummy nodes
        self.left.next, self.right.prev = self.right, self.left   

    def remove(self, node):
        #get the neighbours of the node
        prev, nxt = node.prev, node.next
        #connect the neighbours to disconnect the node
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        #get the neighbours where you need to insert the new node
        prev, nxt = self.right.prev, self.right
        #update the pointers to include the new node and connect it with its neighbours
        prev.next = nxt.prev = node
        node.next, node.prev = self.right, prev

    def get(self, key: int) -> int:
        #check if key is in cache map, 
        #if yes, remove it from the linked list and then insert it back (LRU to MRU)
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        #check if key is in cache map
        #if yes, remove it before updating or inserting the new key-value
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #check if list is at capacity, if yes, remove it
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            #also, delete it from cache map
            del self.cache[lru.key]
        
