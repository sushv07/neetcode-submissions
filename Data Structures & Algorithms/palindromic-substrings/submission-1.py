class Solution:
    def countSubstrings(self, s: str) -> int:
        # TC O(n^2) and SC O(1)
        res = 0
        # expand both front and backwards for odd and even length
        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i+1)
        return res

    # helper function to count the number of palidromic substrings
    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res    