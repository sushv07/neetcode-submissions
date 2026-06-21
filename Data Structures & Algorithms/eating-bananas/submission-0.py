class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #BruteForce - O(m * n)
        #minEatSpeed = 1

        #for minEatSpeed in range(1, max(piles)+1):
        #    totTime = 0
        #    for pile in piles:
        #        totTime += math.ceil(pile/minEatSpeed)

        #    if totTime <= h:
        #        return minEatSpeed

        #return minEatSpeed

        #Optimal - O(log(m) * n)

        #Initialize 2 pointers left and right - range of minEatingSpeed (min = 1 and max = max value of a pile )
        l, r = 1, max(piles)
        #Initialize minEatSpeed - worstcase = 1
        minEatSpeed = 1

        #Perform Binary search on the range of minEatSpeed values
        while l <= r:
            k = (l+r) // 2
            totTime = 0

            for pile in piles:
                totTime += math.ceil(float(pile)/k)

            if totTime <= h:
                minEatSpeed = k
                r = k - 1
            else:
                l = k + 1
        
        return minEatSpeed
        