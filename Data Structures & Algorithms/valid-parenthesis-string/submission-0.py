class Solution:
    def checkValidString(self, s: str) -> bool:
        # greedy solution TC O(n) and SC O(1)
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax  = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1 # -1 assuming a closing bracket, and +1 assuming a opening bracket
            # too many closing brackets
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0 # reset, as there can be many otehr possibilities
            
        return leftMin == 0
        