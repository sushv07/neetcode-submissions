class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #Optimal - O(n) TC and O(n) SC

        numset = set(nums)
        #resultant var - to track longest sequence
        longest = 0

        for num in nums:
            length = 0

            #check for the starting range
            if (num-1) not in numset:
                while (num+length) in numset:
                    length += 1
                    longest = max(length, longest)
            
        return longest
        