class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Brute Force - O(n)
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return -1

        #Optimal
        # Initialize Pointers for Binary Search
        l, r = 0 , len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            #Case1: If target is the middle element    
            if target == nums[mid]:
                return mid

            #Case2: Locate if we are in the left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    #Search Right
                    l = mid + 1
                else:
                    #Search Left
                    r = mid - 1
            #Locate if we are in the right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    #Search Left
                    r = mid - 1
                else:
                    #Search Right
                    l = mid + 1
        
        return -1
        