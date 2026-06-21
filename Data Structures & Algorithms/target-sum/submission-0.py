class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # create a hash map to map each sum to the num of ways(count) to form that sum
        # TC O(n * m) and SC O(m)
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            # hash map to store results after using current num
            # not updating dp directly to avoid mixing old and new values
            nextDP = defaultdict(int)
            for total, count in dp.items():
                nextDP[total + num] += count
                nextDP[total - num] += count
            dp = nextDP
        
        return dp[target]


        