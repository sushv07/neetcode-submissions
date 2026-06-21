class Solution:
    def isValid(self, s: str) -> bool:

        #stack to store the opening brackets
        stack = []
        #hashmap to map each closing bracket with an opening
        containsOpenMap = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            #check if c is a closing bracket
            if c in containsOpenMap:
                if stack and stack[-1] == containsOpenMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False
        