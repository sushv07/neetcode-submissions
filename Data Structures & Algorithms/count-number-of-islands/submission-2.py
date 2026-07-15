class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #O(m * n) TC and O(m * n) SC
        # base case
        if not grid:
            return 0

        # dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        # hashset to track the visited positions
        visit = set()
        # to track the number of islands
        islands = 0

        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                #while queue is not empty, pop a cell
                row, col = q.popleft()
                #expand all its neighbours in all 4 directions
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))            

        #expand the island after a "1" is found
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands