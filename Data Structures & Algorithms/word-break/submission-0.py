class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp - bottom up
        # initialize a dp array - len(s) + 1 => to handle base case empty string at the end = empyty string can be segmented
        dp = [False] * (len(s) + 1)
        # base case
        dp[len(s)] = True

        # bottom up approach - iterate backwards - since cur solution depends on future solutions
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if((i+len(w)) <= len(s) and s[i: i+ len(w)] == w):
                    dp[i] = dp[i + len(w)]
                #if found the word to be valid, break early
                if dp[i]:
                    break
        return dp[0]
