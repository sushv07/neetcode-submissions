class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        #Optimal solution

        freq = {} #map num -> count
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        res = []
        # 1 .... n
        for count in range(1, len(nums) + 1):
            #from constraints
            for value in range(100, -101, -1):
                if value in freq and freq[value] == count:
                    res.extend([value] * count)
        
        return res



        
        