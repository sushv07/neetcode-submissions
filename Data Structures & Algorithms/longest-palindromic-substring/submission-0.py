class Solution:
    def longestPalindrome(self, s: str) -> str:
        #O(n^2) TC and O(n) SC
        res = ""
        resLen = 0

        for i in range(len(s)):
            #start expanding backwards
            #odd length 
            l, r = i, i
            #while left and right pointers are in bounds
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                #expand backwards
                l -= 1
                r += 1

            #even length
            l, r = i, i + 1
            #while left and right pointers are in bounds
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                #expand backwards
                l -= 1
                r += 1
        return res