class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # TC O(n * logn) and SC O(n) - greedy solution
        # default base case
        if len(hand) % groupSize:
            return False
        
        # hashmap to keep track of counts
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        # minHeap to keep track of start range
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                # if not present in hashmap
                if i not in count:
                    return False
                count[i] -= 1
                # if the element we plan tpo pop is not the min value in minHeap, returnm False
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
        