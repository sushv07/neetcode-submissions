class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Optimal solution using monotonic decreasing satck - O(n) TC and O(n) SC
        res = [0] * len(temperatures)
        stack = [] #stores a pair (temperature, index)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

