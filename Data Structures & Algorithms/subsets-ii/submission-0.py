class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #O(n * 2^n) TC and O(2^n) SC - output list
        #resultant list of subsets
        res = []
        #sort the input list to efficiently eliminate duplicates
        nums.sort()

        #recursive backtracking function   
        def backtrack(i, subset):
            #base case
            if i == len(nums):
                #we create a copy becoz we will be modifying the subset lists further
                res.append(subset.copy())
                return

            #All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            #pop becoz we won't be including it next
            subset.pop()

            #All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i+1, subset)

        backtrack(0, [])
        return res



        