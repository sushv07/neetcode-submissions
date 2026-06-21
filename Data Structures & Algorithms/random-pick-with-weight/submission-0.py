class Solution:
    #optimal prefix sum + brute force
    def __init__(self, w: List[int]):
        self.prefix = []
        running_sum = 0

        for n in w:
            running_sum += n
            self.prefix.append(running_sum) 

            self.total = running_sum               

    def pickIndex(self) -> int:

        target = random.randint(1, self.total)
        left = 0
        right = len(self.prefix) - 1

        while left < right:
            mid = (left + right) // 2

            if self.prefix[mid] < target:
                left = mid + 1
            # mid can also be the answer, bit is it the first occurence of prefix sum ranges that contains the target?
            else:
                right = mid
            
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()