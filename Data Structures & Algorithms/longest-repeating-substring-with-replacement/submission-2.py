class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Optimal solution O(n) TC and O(m) SC
        #n - length of input string
        #m - no. of unique chars in the string
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count.get(s[r]))
            #while (r - l + 1) - max(count.values()) > k:
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1 
            res = max(res, r - l + 1)
        return res