class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP Bottom up approach - TC O(n^2) and SC - O(n)
        # cache future results
        LIS = [1] * len(nums)

        # bottom-up - iterate from backwards
        for i in range(len(nums) - 1, -1, -1):
            # checking for all j > 1, if we can extend the subsequence
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS) 

        