class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #TC O(m * n) and SC O(m * n)
        #define dimensions of the grid
        ROWS, COLS = len(heights), len(heights[0])
        #hashsets to track which positions in grid can flow to pac and atl oceans
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            #basecase
            if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            #expand all 4 neighbouring directions 
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        #track cells that can flow to pac and atlantic oceans from the 1st and last row
        for c in range(COLS):
            dfs(0,c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        #track all the cells that can reach both pac and atlantic oceans from the 1st and last columns
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        #expand through every cell in the grid to check which cells reach both oceans and add it to the result as a sublist
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


        