class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Brute Force - O(m * nlogn) TC / O (m * n) SC
        #m is the number of input strings  and n is the length of the longest string
        #res = defaultdict(list)

        #for s in strs:
        #    if s.isalpha() or s.isalnum():
        #        sortedS = "".join(sorted(s.lower()))
        #        res[sortedS].append(s)
        #return list(res.values())

        #Optimal - O(m * n) TC / O(m * n) SC
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c.lower()) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())