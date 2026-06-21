class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #O(2^t/m) t - target and m - min value in nums / O(t/m) SC 
        #resultant list
        res = []

        #dfs function if we use the cur candidate value or skip it
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            #decide to use the candidate
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            #decide not to use the candidate
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
