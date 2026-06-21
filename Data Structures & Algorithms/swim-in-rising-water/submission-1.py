class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # TC O(n log n) and O(n) SC
        N = len(grid)
        # visit hash set to track nodes visited
        visit = set()
        minH = [[grid[0][0], 0, 0]] # (time/height, r, c)
        # helper directions var to traverse neighbors
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            # pop the min height cost 
            t, r, c = heapq.heappop(minH)
            # if we have reached the destination
            if r == N - 1 and c == N - 1:
                return t
            # traverse through all 4 directions
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                # if out of bounds or already in visit hash set, skip the node
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
            

