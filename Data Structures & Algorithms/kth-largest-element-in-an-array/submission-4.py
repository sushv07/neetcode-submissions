class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #using minHeap - O(nlogk) TC and O(n) SC
        minHeap = []

        #keep pushing the elements
        for n in nums:
            heapq.heappush(minHeap, n)
            #if heap size exceeds k, pop the smallest element - minHeap root
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        #return the root from the heap - the kth largest    
        return minHeap[0]
        