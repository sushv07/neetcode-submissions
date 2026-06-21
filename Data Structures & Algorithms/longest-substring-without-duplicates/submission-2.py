class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window approach - O(n) TC and space O(min(n, m))
        longest = 0
        l = 0
        #hashset to keep track of the substring window
        charset = set()

        for r in range(len(s)):
            while s[r] in charset:
                #remove the left most element from the window as we need to slide it
                charset.remove(s[l])
                l += 1
            longest = max(longest, r - l + 1)
            charset.add(s[r])
        return longest     

        