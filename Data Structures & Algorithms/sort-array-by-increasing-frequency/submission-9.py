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
        
        nums.sort(key=lambda x: (freqMap[x], -x))

        return nums


        