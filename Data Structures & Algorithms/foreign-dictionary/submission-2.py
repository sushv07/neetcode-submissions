class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # O(V + N + E) TC and O(V + E) SC
        # build a dictionary to track the neighbors of each of the chars
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            # check 2 consecutive words
            w1, w2 = words[i], words[i + 1]
            # take the min len of both words
            minLen = min(len(w1), len(w2))
            # check for edge cases
            # if length of word1 is > length of word2 and if both words haver the same prefix, return empty string
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # add char to dictionary map, if chars are diff
                    adj[w1[j]].add(w2[j])
                    break
            
        visited = {} # if visited - set to False
        res = []     # if in current path - set to True

        # run dfs
        def dfs(char):
            if char in visited:
                return visited[char]
                
            visited[char] = True
                
            #check all neighbouring nodes
            for neiChar in adj[char]:
                if dfs(neiChar):
                    return True
                
            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)





        