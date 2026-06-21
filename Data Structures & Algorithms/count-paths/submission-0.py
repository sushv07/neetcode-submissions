class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # TC O(n * m) and O(n) TC
        # define the last row with all 1's
        row = [1] * n
        # iterate thorugh all other rows except last
        for i in range(m - 1):
            newRow = [1] * n
            # iterate through all other cols except last - since last will be all 1's
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]