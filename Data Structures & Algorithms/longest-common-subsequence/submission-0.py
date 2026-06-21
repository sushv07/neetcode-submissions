class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp approach - TC O(n * m) and SC O(n * m)
        # initialize a 2D grid with all zeroes
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # iterate through the 2D grid in reverse order
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    # 1 + diagonal cell
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # max (right cell, bottom cell)
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]
        