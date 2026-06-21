class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Brute Force
        numset = set(nums)
        res = 0

        if len(nums) == 0:
            return 0

        for n in nums:
            streak, curr = 0, n

            while curr in numset:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
