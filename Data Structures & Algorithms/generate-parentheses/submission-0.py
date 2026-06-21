class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #list - to hold the parenthesis
        stack = []
        #resultant list to hold lists of of parenthesis combinations
        res = []

        def backtrack(openN, closedN):
            #basecase
            if openN == closedN == n:
                res.append("". join(stack))
                return

            #only add a open parenthesis when openN < n
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                #so that we can try a new combination
                stack.pop()

            #only add a closed parenthesis when closedN < openN
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN +1)
                stack.pop()

        backtrack(0,0)
        return res   

        

        