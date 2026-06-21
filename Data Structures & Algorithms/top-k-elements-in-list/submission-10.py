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

        #Optimal Solution - Bucket Sort - O(n) TC and O(n) SC

        if len(nums) == 0 or k == 0:
            return []

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for num, freq_count in count.items():
            freq[freq_count].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



            

