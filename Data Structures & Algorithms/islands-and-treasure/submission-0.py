class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #O(m * n) TC and O(m * n)
        #define the dimensions
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            #basecase
            if(r < 0 or r == ROWS or c < 0 or c == COLS or
               (r, c) in visit or grid[r][c] == -1):
               return
            visit.add((r, c))
            q.append([r, c])


        #expand the grid and add the gates to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        dist = 0
        #bfs on all the gates
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                #expand in all 4 directions
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1
        