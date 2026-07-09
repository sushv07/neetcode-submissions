class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # If we've considered all numbers
            if i == len(nums):
                if total == target:
                    res.append(cur.copy())
                return

            # Try using nums[i] 0, 1, 2, ... times
            count = 0
            while total + count * nums[i] <= target:
                # Add nums[i] count times
                for _ in range(count):
                    cur.append(nums[i])

                dfs(i + 1, cur, total + count * nums[i])

                # Backtrack
                for _ in range(count):
                    cur.pop()

                count += 1

        dfs(0, [], 0)
        return res