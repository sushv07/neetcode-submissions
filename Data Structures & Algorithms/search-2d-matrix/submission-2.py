class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #Initialize row and column pointers
        ROWS, COLS = len(matrix), len(matrix[0])
        #Initialize top and bottom pointers
        top, bot = 0, ROWS - 1

        #Isolate which row contains the target - using binary search approach
        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = top + 1
            elif target < matrix[row][0]:
                bot = bot - 1
            else:
                break

        #If not a valid row (target not found in any of the rows), return False
        if not (top <= bot):
            return False

        #If row found, Isolate where the target is in the row found - using binary search
        l, r = 0, COLS - 1
        row = (top + bot) // 2     
        while l <= r:
            m = (l+r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = r - 1
            else:
                return True
        
        return False       
        