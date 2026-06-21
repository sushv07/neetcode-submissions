class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}
        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)

        for cnt in countMap:
            if countMap[cnt] > len(nums)/2:
                return cnt        