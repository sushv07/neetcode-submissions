class Solution:
    def jump(self, nums: List[int]) -> int:
        # a simplified bfs
        # O(n) TC and O(1) SC
        res = 0
        # pointers to keep track of current window
        l = r = 0

        while r < len(nums) - 1:
            #calculate the farthest jump we can make from the current window
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res