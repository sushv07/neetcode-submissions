class Solution:
    def rob(self, nums: List[int]) -> int:
        #TC O(n) and O(1) SC
        #max(first element - to handle if only 1 element in input, excluding the first element, excluding the last element)
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2        