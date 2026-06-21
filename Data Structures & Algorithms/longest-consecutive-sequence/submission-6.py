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

        #Optimal - O(n) TC and O(n) SC

        numset = set(nums)
        #resultant var - to track longest sequence
        longest = 0

        for num in nums:
            length = 0

            #check for the starting range
            if (n-1) not in numset:
                while (n+length) in numset:
                    length += 1
                    longest = max(length, longest)
            
        return longest

                     



