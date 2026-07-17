class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # O(E) TC and O(V) SC
        N = len(edges)
        # parent array - ith node -> parent (ranges from 1 to n)
        par = [i for i in range(N + 1)]
        # rank array -> initialized to 1 for all n nodes
        rank = [1] * (N + 1)

        # find the root parent of the node
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        # merge if not connected
        def union(n1, n2):
            #find the root parents of the 2 nodes
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            # attach smaller rank node to higher rank node
            # update rank of parent node
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p1]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        # iterate through the edges list to find the set of nodes with a common parent
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
