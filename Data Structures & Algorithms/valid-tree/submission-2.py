class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # O(V + E) TC and O(V + E) SC
        # valid tree - only iff a graph is fully connected and has no cycles
        # a tree with "n" nodes must have "n-1" edges

        #even if no nodes then valid tree
        if not n:
            return True 

        # build adjacency list for all nodes
        adj = { i: [] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        # pass current node and prev node
        # cycle detection
        def dfs(i, prev):
            # base case
            if i in visit:
                return False
            
            visit.add(i)
            # iterate through the neigbours of the current node
            for j in adj[i]:
                # if the neigbour is the prev node that we came from, skip dfs
                if j == prev:
                    continue
                # perform dfs on node j
                #if dfs finds a visited node - a cycle exists, so return False, else do a dfs on every other neighbour
                if not dfs(j, i):
                    return False
            return True
       
        return dfs(0, -1) and n == len(visit)    



        
        