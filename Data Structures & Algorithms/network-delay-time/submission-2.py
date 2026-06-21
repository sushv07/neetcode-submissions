class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # O(ElogV) TC and O(V + E) SC
        #create and adjacency list for the edges
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # min heap to keep track of the path length and the respective node
        minHeap = [(0, k)]
        # to avoid cycles
        visit = set()
        # resultant time to return
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            # don't need to visit its neighbours if already in visit
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return t if len(visit) == n else -1


        