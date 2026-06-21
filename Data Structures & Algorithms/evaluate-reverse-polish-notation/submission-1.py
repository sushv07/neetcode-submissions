class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Brute Force Approach - O(n^2)
        #We are checking until only a single element remains
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+,-,*,/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == "+":
                        result = a + b
                    elif tokens[i] == "*":
                        result = a * b
                    elif tokens[i] == "/":
                        result = int(a / b)
                    elif tokens[i] == "-":
                        result = a - b
                    #rebuilding the tokens list takes up O(n) time
                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
                    break
        
        return int(tokens[0])
                    
                        