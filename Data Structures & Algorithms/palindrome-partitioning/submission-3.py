class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # O(2^n) TC and O(n) SC -> n is the length of the input string
        # to hold all our valid partitions
        res = []
        # to hold our current list of chosen substrings
        part = []

        def dfs(i):
            # base case
            if i >= len(s):
                res.append(part.copy())
                return
            #check which partitions are palindromes in the entire string    
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    # add the current susbstring to the partition var
                    part.append(s[i: j+1])
                    # run dfs on the rest of the string
                    dfs(j+1)
                    # remove the last added susbstring, so that we chose another palindrome partition next
                    # part.pop() undoes the most recent choice made by the current recursive call, 
                    # allowing the previous call to try a different choice.
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

        