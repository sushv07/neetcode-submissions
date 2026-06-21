class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # O(n * 4 ^ n) TC - n is the number of digits and 4 - digit 9 can have upto 4 char mappings wxyz)
        # O(n) SC
        # resultant list of all combinations
        res = []
        # hashmap - digit to char mappings
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        #recursive function call
        def backtrack(i, curStr):
            # base case
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            #recursive calls incase we still have digits to parse
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        #if input digits is empty, return [] and not [""]
        if digits:
            backtrack(0, "")
        
        return res

        