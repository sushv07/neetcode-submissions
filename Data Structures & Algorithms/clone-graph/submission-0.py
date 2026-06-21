"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # O(V + E) TC and O(V) SC
        #hashmap to store the original nodes -> mapped to cloned nodes
        oldToNew = {}

        #recusrive dfs to clone
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            #if not already in map, create a copy of the node
            copy = Node(node.val)
            #store the clone in the hash map
            oldToNew[node] = copy
            #recursively clone all its neighbors and store it in the hashmap
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            #return the cloned copy of the starting node
            return copy

        return dfs(node) if node else None
        