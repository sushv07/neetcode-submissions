class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #2 pointers - left (buying) / right (selling)
        l, r = 0, 1
        #maxProfit
        maxP = 0

        while r < len(prices):
            #check if buying price is lower than selling price
            #if yes, calculate profit and maxProfit
            #else, update left pointer
            #sliding window approach - O(n) T.C / O(1) S.C 
            #left pointer updates based on condition
            #right pointer keeps incrementing after every iteration
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        return maxP                


        