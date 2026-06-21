class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Brute Force - O(n^2) TC and O(n) SC
        numset = set(nums)
        longest = 0

        if len(nums) == 0:
            return 0

        for n in nums:
            streak, curr = 0, n

            while curr in numset:
                streak += 1
                curr += 1
            longest = max(longest, streak)
        return longest

        

                     



