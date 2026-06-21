class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # O(n * m * 4^n) - n * m - dimensions of the board 4^n - dfs function - call stack = len of the word - 4 differnet directions 
        ROWS, COLS = len(board), len(board[0])
        # to keep track of already visited path
        path = set()

        def dfs(r,c, i):
            # basecase: if we have completed the word
            if i == len(word):
                return True
            # edgecases:out-of-bounds / word char not in the path /
            # path/char already visited
            if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            word[i] != board[r][c] or
            (r, c) in path):
                return False
            
            path.add((r,c))
            # perform dfs along all adjacent paths - horizontally and vertically
            res = (dfs(r+1, c, i +1) or
                   dfs(r-1, c, i +1) or
                   dfs(r, c+1, i +1) or
                   dfs(r, c-1, i +1))
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False
       