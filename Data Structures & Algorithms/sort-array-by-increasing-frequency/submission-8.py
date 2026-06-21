class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        #optimal O(nlogn) and SC is O(n) 
        freqMap = {} # number -> count
        #populate countmap directly using hashmap
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        
        nums.sort(key=lambda x: (freqMap[x], -x))
        return nums

