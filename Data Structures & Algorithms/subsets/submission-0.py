class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #O(n * 2^n) TC and O(n) SC

        #output result
        res = []
        #subset lists
        subset = []

        #backtracking function using dfs
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            #decision to SKIP / NOT INCLUDE nums[i]
            subset.pop()
            dfs(i + 1)


        dfs(0)
        return res
        