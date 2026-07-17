class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # O(E) TC and O (n) SC 
        # Start with every node as its own component. 
        # For every edge, check whether the two nodes already belong to the same group. 
        # If they don’t, merge the groups and decrease the component count by one. 
        # After processing all edges, the remaining number of groups is the number of connected components.
        # parent nodes array
        par = [i for i in range(n)]
        # rank array - initialized to 1 for all nodes
        # rank stores size of each group
        rank = [1] * n

        # to find the root parent of a node
        def find(n1):
            res = n1

            #path compression
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        #merge different components
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            #if both parents are same. no merge operation
            if p1 == p2:
                return 0
            
            #attach smaller rank node to higher rank node and update rank
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res

        