class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # TC O(n^2 log n) and SC - O(n)
        N = len(points)
        # create an adjacency list for the edges
        adj = {i: [] for i in range(N)}   # [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # prim's algorithm
        res = 0
        # hash set to track all the nodes visited
        visit = set()
        # minHeap to track the min cost along the path
        minH = [[0, 0]]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            # if already in visit set, skip and move to next node
            if i in visit:
                continue
            res += cost
            visit.add(i)
            # check all its neighbours
            for neiCost, nei in adj[i]:
                # if neighbours not in visit set, then push to minHeap
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res
