class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #TC O(m * n) and SC O(m * n)
        #queue to track the rotten oranges
        q = deque()
        time, fresh = 0, 0

        #dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])
        #expand the grid to fetch fresh and rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        #directions that span horizontally and vertically in the grid
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                #perform multisource bfs for each of the rotten oranges
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    #if in bounds and fresh, then make it rotten
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 1):
                        #if out of bounds or no fresh oranges, skip
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1

         