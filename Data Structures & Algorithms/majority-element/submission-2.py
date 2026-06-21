class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      for i in nums:
        count = 0
        for j in nums:
            if i == j:
                count += 1
        if count > len(nums)/2:
            return i       