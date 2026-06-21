class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        
        nums.sort(key=lambda x: (freqMap[x], -x))
        return nums

