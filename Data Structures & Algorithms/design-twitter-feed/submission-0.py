class Twitter:

    def __init__(self):
        #timestamp for ordering the tweets - smaller value means most recent
        self.count = 0
        self.tweetMap = defaultdict(list) #userId mapped to -> list of [count, tweetId]
        self.followMap = defaultdict(set) #userId mapped to -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] #order starting from latest
        minHeap = []

        #make sure the user follows themselves
        self.followMap[userId].add(userId)
        #get the most recent tweet from both the user and their followees and push them to the minHeap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                #minheap contains list of count/timestamp of the current tweet, current tweetId, followeeId of the user, index of the next recent tweet of the same followee
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        #repeatedly pick the next recent tweet and replace it with the user's older tweets
        while minHeap and len(res) < 10:
            #pop the next most recent tweet from the followee until no more tweets exist for that followee
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            #check if older tweets exist for the same followee and add it to heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)      

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
