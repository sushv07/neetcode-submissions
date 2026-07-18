class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #using maxHeap
        #each task takes 1 unit of time
        #aim is to minimize idle time
        #O(n * m) TC - n is the number of tasks and m is the idle time units and O(n) space complexity

        #create Hashmap for the list of tasks and their counts
        count = Counter(tasks)
        #create maxHeap list with negatives
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        #to track time units
        time = 0
        #create a deque to track pairs [cnt, idleTime]
        q = deque()

        #loop through the heap or q until elements exist 
        while maxHeap or q:
            time += 1
            if maxHeap :
                #decremt the cnts as you pop from the maxHeap
                cnt = 1 + heapq.heappop(maxHeap)
                #if cnt is not zero, append to the queue
                if cnt:
                    q.append([cnt, time + n])
            #if the time in queue and time units match, push back to heap
            # If the first task in the cooldown queue is done cooling down, 
            # put it back into the heap so it can be used again.
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time





        