class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #using quickSelect
        #using the idea - when arary is sorted, the index len(nums) - k gives the position of the kth largest
        #O(n^2) TC and O(n) SC  
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                #if current number less than or equal to pivot, swap and increment p
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            #swap, but p remains same
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)

        