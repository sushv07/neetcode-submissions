class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        #to track the moving sum
        self.window_sum = 0
        
    def next(self, val: int) -> float:
        #append the val to the queue
        self.queue.append(val)

        if len(self.queue) > self.size:
            self.window_sum -= self.queue.popleft()
        else:
            0

        self.window_sum += val

        return self.window_sum / min(self.size, len(self.queue))

        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
