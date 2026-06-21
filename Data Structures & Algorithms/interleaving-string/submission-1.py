class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # TC O(n * m) and SC O(n * m)
        # edge case
        if len(s1) + len(s2) != len(s3):
            return False
        
        # initialize a 2D grid with all values set to False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        # initialize the out of bounds position of both strings to True
        dp[len(s1)][len(s2)] = True

        # work our way from bottom right to top left in the 2D grid
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # considering char of s1
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]

        