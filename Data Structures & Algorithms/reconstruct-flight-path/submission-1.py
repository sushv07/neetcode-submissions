class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # O(n!) - TC and O(n) SC
        # adjacency list to store the tickets and their stops
        adj = { src : [] for src, dest in tickets }

        tickets.sort()
        for src, dest in tickets:
            adj[src].append(dest)

        res = ["JFK"]
        def dfs(src):
            # base case
            if len(res) == len(tickets) + 1:
                return True
            # if no path exists
            if src not in adj:
                return False

            temp = list(adj[src])
            # visting the neighbours of the node
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                if dfs(v) : return True
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res




        