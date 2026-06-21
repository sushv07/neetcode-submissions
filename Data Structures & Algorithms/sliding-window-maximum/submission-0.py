class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #output list
        output = []
        #deque for tracking the indices of the largest element in the window
        q = collections.deque()

        l = r = 0

        #sliding window begins
        while r < len(nums):
            #pop smaller elements from the deque before adding new ones
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #pop left most element if it goes out of bounds from window
            if l > q[0]:
                q.popleft()
            
            #check if within the window range, if yes, then append to output list
            if r + 1 >= k:
                output.append(nums[q[0]])
                #increment left only if it is of atleast size k
                l += 1
            r += 1

        return output    




