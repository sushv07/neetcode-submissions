class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # TC O(amount * len(coins)) / SC O(amount)
        # unbounded knapsack dp - bottom up
        # dp array - no. of coins needed to add up to this amount
        dp = [amount + 1] * (amount + 1)
        # base case - no. of coins needed to add up to 0
        dp[0] = 0

        # iterate through every amount - bottom up
        for a in range(1, amount + 1):
            # iterate through every coin - each coin can be used unlimited number of times
            for c in coins:
                #check if current coin can be used
                if a - c >= 0:
                    # min no. of coins needed to add up to an amount -> min(old value, use current coin + no. of coins needed for the remaining amount)
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1 
        