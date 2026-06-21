class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Brute Force - O(nlogn) TC and O(n) SC
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = []
        for num, cnt in count.items():
            freq.append([cnt,num])
        freq.sort()

        res = []
        while len(res) < k:
            res.append(freq.pop()[1])
        
        return res
            

