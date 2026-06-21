class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(n) TC and O(1) SC
        #rob1 = best money upto 2 houses back
        #rob2 = best money upto 1 house or previous house

        rob1, rob2 = 0, 0

        #[rob1, rob2, n, n + 1]
        for n in nums:
            #for each house, we have 2 choices - we can either use it or skip it
            newRobBestMoney = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = newRobBestMoney
        
        return rob2
        