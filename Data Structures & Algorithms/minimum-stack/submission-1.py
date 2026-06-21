class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:

        #a temporary stack to track the min and 
        #then push it back to the original stack 
        tmp = []
        minimum = self.stack[-1]

        while(len(self.stack)):
            minimum = min(minimum, self.stack[-1])
            tmp.append(self.stack.pop())

        while(len(tmp)):
            self.stack.append(tmp.pop())

        return minimum
        
        
        
