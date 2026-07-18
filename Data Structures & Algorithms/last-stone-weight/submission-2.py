class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #O(n) TC and O(1) SC
        #for a min Heap, convert to negative numbers
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            #since we have converted into negative values
            #e.g first = -8 and second = -7
            if second > first:
                heapq.heappush(stones, first - second)

        #if no stones remain
        stones.append(0)
        #convert negatives to positives and return
        return abs(stones[0])

        