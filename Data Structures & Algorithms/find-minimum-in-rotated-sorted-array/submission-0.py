class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Brute Force - O(n) T.C
        #return min(nums)

        #Optimal - O(log n) T.C

        #Initialize resultant value to be the first element - (random, can be any)
        res = nums[0]
        #Initialize left and right pointers
        l, r = 0, len(nums) - 1

        #Perform binary search
        while l <= r:
            #If array is already sorted, return left most element
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            #Binary search begins
            mid = (l+r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                #Search Right 
                l = mid + 1
            else:
                #Search Left
                r = mid - 1

        return res
        