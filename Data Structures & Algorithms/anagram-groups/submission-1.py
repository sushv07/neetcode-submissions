class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #BruteForce
        #res = defaultdict(list)
        #for s in strs:
        #    sortedS = "".join(sorted(s))
        #    res[sortedS].append(s)
        #return list(res.values())

        #Optimal
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # to store the count of each char in each string
            #loop through each char in the string and populate this count array
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())



        


        