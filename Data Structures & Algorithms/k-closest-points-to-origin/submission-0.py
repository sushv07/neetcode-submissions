class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #O(n) TC and O(n) SC
        #a list stored in a heap - minHeap [ distance between x and y, x, y]
        minHeap = []
        for x,y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        #convert it to a minHeap
        heapq.heapify(minHeap)
        #result list to return
        res = []

        #pop from the minHeap k times and append to the result
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res

        