class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # bottom-up db - O(n * t) TC and O(t) SC
        # base case - if len(nums) is odd - we can't split it inot 2 equal halves
        if sum(nums) % 2:
            return False

        # dp hash set stores all reachable sums - old sums
        dp = set()
        # initialize it with 0 - if we don't choose any number
        dp.add(0)
        # calculate target value
        target = sum(nums) // 2

        # iterate backwards through each number
        for i in range(len(nums) - 1, -1, -1):
            # to track new sums
            nextDP = set()
            # check if we can reach the target
            # for each number we have 2 possibilities - we choose the cur number or we skip it and take only old sum
            for t in dp:
                # if target reached early - return True
                if(t + nums[i] == target):
                    return True
                # choice 1 - include cur number
                nextDP.add(t + nums[i])
                # choice 2 - skip cur number and just keep old sum
                nextDP.add(t)
            # reset the old reachable sums hashset to point to updated values
            dp = nextDP
        # if target cannot be achieved, return False
        return False
