class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # O(m^2 * n) TC and SC -> m is the length of the word and n is the no. of words in the input wordList
        if endWord not in wordList:
            return 0
        
        # adjacency list to collect the words that map to a pattern
        nei = defaultdict(list)
        wordList.append(beginWord)
        # populate the adjacency list
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        # a visit hashset to keep track of nodes / words already visited    
        # start with beginWord
        visit = set(beginWord)
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    #iterate through all its neighbours for the pattern
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0    

        