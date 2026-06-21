class Solution:
    def numDecodings(self, s: str) -> int:
        # Space optimized dp solution O(n) TC and O(1) SC
        # define the variables

        # no. of ways to decode from the position i
        dp = 0

        # no. of ways to decode from the position i + 2
        dp2 = 0

        # base case - if empty string (end of string is reached)- also represents no. of ways to decode from position i + 1
        dp1 = 1

        # bottom-up approach - iterate from right to left
        # ways[i] = ways[i+1] + ways[i+2] recurrence relation => reason for bottom-up approach - we need future values first before current value

        for i in range(len(s) - 1, -1, -1):
            # base case
            if s[i] == "0":
                dp = 0
            # take 1 digit and decode remaining    
            else:
                dp = dp1

            #check validity of taking 2 digits and if valid, take 2 digits and decode remaining
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" 
            and s[i + 1] in "0123456"):
                dp += dp2
            # shifting and resetting values for further iterations         
            dp2 = dp1
            dp1 = dp
            dp = 0
        return dp1
        