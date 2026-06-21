class Solution:
    def numDecodings(self, s: str) -> int:
        # dp using caching
        # O(n) TC and O(n) SC
        dp = {len(s): 1}

        def dfs(i):
            # base cases:
            # if end of string or empty string - no. of ways to decode an empty string - 1
            if i in dp:
                return dp[i]
            # if string starts with 0 -> invalid
            if s[i] == "0":
                return 0

            # take 1 digit and calculate no. of ways to decode remaining string
            res = dfs(i + 1)

            # take 2 digits - if valid and calculate the no. of ways to decode remaining string 
            # checking validity of 2 digits
            if (i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456")):
                res += dfs(i+2)
            
            dp[i] = res
            return res        

        return dfs(0)        