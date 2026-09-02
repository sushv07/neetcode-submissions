class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Deque to maintain elements in decreasing order.

        # Front always contains the maximum element of the current window.

        maxDeque = deque()

        # Deque to maintain elements in increasing order.

        # Front always contains the minimum element of the current window.

        minDeque = deque()

        # Left pointer of the sliding window

        l = 0

        # Stores the length of the longest valid window found so far

        res = 0

        # Expand the window by moving the right pointer

        for r in range(len(nums)):

            # Remove all smaller elements from the back.

            # They can never become the maximum while nums[r] exists.

            while maxDeque and nums[r] > maxDeque[-1]:

                maxDeque.pop()

            # Add current element to the max deque

            maxDeque.append(nums[r])

            # Remove all larger elements from the back.

            # They can never become the minimum while nums[r] exists.

            while minDeque and nums[r] < minDeque[-1]:

                minDeque.pop()

            # Add current element to the min deque

            minDeque.append(nums[r])

            # If the window becomes invalid, shrink it from the left

            while maxDeque[0] - minDeque[0] > limit:

                # If the element leaving the window is the current maximum,

                # remove it from the front of maxDeque.

                if nums[l] == maxDeque[0]:

                    maxDeque.popleft()

                # If the element leaving the window is the current minimum,

                # remove it from the front of minDeque.

                if nums[l] == minDeque[0]:

                    minDeque.popleft()

                # Move the left pointer to shrink the window

                l += 1

            # Update the maximum valid window length

            res = max(res, r - l + 1)

        return res