class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # O(n!) TC and O(n^2) SC
        col = set() # to handle same col conflict - tracks c cols
        posDiag = set() # to handle same (row + col) conflicts
        negDiag = set() # to handle same (row - col) conflicts

        #return all possible combinations of N queens 
        res = []

        #initialize n * n board
        board = [["."] * n for i in range(n)]

        #recursive backtracking function
        def backtrack(r):
            # basecase
            if r == n:
                #if all rows are filled, convert the board into a list of strings and save it
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            #if all rows are not yet filled
            for c in range(n):
                # if current col is already in any one of the sets
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                #if current col is not in any of the sets
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                #recurse next row for all other combinations
                backtrack(r + 1)

                #remove the entries from all sets
                #remove the queen from the board
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res



        