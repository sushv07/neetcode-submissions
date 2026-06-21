class Solution:
    def isValid(self, s: str) -> bool:

        #stack to store the opening brackets
        stack = []
        #hashmap to map each closing bracket with an opening bracket
        containsOpenMap = {")" : "(", "}" : "{", "]" : "["}

        #Iterate through the each character in the string
        for c in s:
            #check if char is a closing bracket
            if c in containsOpenMap:
                #if the stack is not empty and if top of the stack contains a matching opening bracket
                #pop it from the stack
                #else return False , since no matching bracket in stack
                if stack and stack[-1] == containsOpenMap[c]:
                    stack.pop()
                else:
                    return False
            #if stack contains an opening bracket, add it to the stack
            else:
                stack.append(c)

        #If stack is empty after all the iterations, return True else return False
        if not stack:
            return True
        else:
            return False
        