class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Number of valid subarrays found so far
        res = 0
        # Left boundary of the sliding window
        l = 0
        # Product of all elements in the current window nums[l:r + 1]
        product = 1
        # Expand the window by moving the right boundary
        for r in range(len(nums)):
            product *= nums[r]
            # If the product is too large, move the left boundary forward
            # until the product becomes strictly less than k.
            #
            # l <= r prevents removing elements after the window is empty.
            while l <= r and product >= k:
                product //= nums[l]
                l += 1
            # The current window is nums[l:r + 1].
            #
            # Every subarray ending at index r and starting from any index
            # between l and r is valid:
            #
            # nums[l:r + 1]
            # nums[l + 1:r + 1]
            # ...
            # nums[r:r + 1]
            #
            # There are r - l + 1 such subarrays.
            res += (r - l + 1)
        return res