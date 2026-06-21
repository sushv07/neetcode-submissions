class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # brute force TC O(n^2) and SC O(n)
        freqMap = {}
        #populate count map using loops
        for num in nums:
            count = 0
            for n in nums:
                if n == num:
                    count += 1
            freqMap[num] = count
        #For each number x, 
        #I create a sorting key (freqMap[x], -x). 
        #Python sorts tuples from left to right. 
        #The first value sorts by frequency in ascending order. 
        #If two numbers have the same frequency, 
        #the second value -x makes larger numbers come first, 
        #which gives descending order among ties.
        nums.sort(key=lambda x: (freqMap[x], -x))

        return nums


        