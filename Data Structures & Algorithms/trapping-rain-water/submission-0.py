class Solution:
    def trap(self, height: List[int]) -> int:
        #Brute Force - O(n^2) TC and O(1) SC
        #if height == 0:
        #    return 0

        #res = 0
        #n = len(height)

        #Calculates leftMax and rightMax for every iteration
        #for i in range(n):
        #    leftMax = rightMax = height[i]

        #    for j in range(i):
        #        leftMax = max(leftMax, height[j])
        #    for k in range(i+1, n):
        #        rightMax = max(rightMax, height[k])

        #    res += min(leftMax, rightMax) - height[i]
        
        #return res

        #Optimal O(n) TC and O(1) SC
        # Two pointer approach
        if height == 0:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            #basis of shifting left and right pointers - which ever is shorter - smaller side is the bottleneck
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res