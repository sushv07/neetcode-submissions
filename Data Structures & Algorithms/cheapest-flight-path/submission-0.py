class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellmont-ford algo - O(n + (m * k)) TC and O(n) SC
        # prices array initialized to infinity
        prices = [float("inf")] * n
        # initialize price to reach src as 0
        prices[src] = 0

        # iterate k + 1 times to ensure that we consider the stop limit
        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights: # source, destination and price

                if prices[s] == float("inf"): # if price of s is not reachable, skip it
                    continue
            
                # if reachable, check for cheapest and update in tmp array
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]

