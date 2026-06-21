class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        charset = set()

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            longest = max(longest, r - l + 1)
            charset.add(s[r])
        return longest     

        