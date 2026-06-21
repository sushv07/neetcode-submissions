class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #TC - O(m * n)
        #Get the dimensions of the board
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            #basecase:
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        #1. DFS - Capture Unsurrounded regions ( O -> T )
        #check if r is in the border rows and c is in border cols
        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c] == "O" and
                   (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                   capture(r, c)
        
        #2. Capture the Surrounded Regions ( O -> X )
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #3. Uncapture the unsurrounded regions ( T -> O )
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"


        