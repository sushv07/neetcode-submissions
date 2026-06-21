class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # TC O(nlogn + qlogq) and SC - O(n + q)
        intervals.sort()

        minHeap = []
        # a hashmap to store the results of the queries in order
        # a pointer to loop through intervals list
        res, i = {}, 0

        # iterate through the sorted queries list
        for q in sorted(queries):
            # if pointer is in bounds and the left most value of the cur interval is <= q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            # pop all entries from minHeap that are < q
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]

