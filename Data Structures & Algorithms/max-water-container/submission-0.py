class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute Force - O(n^2)
        #res = 0
        #left and right pointers moving in same direction
        #for l in range(len(heights)):
        #    for r in range(l+1, len(heights)):
        #        area = (r - l) * min(heights[l], heights[r])
        #        res = max(res, area)
        #return res

        #Optimal
        res = 0
        #left and right pointers moving in opposite direction
        l, r = 0, len(heights) - 1

        #execute till left and right pointers dont cross each other
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            #check which height is minimum and move respective pointer
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res