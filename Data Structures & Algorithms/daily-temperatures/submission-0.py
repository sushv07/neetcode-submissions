class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * len(temperatures)

        for i in range(n):
            j = i+1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
                else:
                    res[i] = 0
                    j += 1
        return res
        