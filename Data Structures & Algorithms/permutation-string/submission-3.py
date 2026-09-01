class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge case - check
        if len(s1) > len(s2):
            return False
        #count arrays for s1 and s2
        countS1, countS2 = [0] * 26, [0] * 26

        #initial counts for first len(s1) window of s1 and s2
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1

        #populate matches for the initial window
        matches = 0
        for i in range(26):
            matches += (1 if countS1[i] == countS2[i] else 0)

        #sliding window begins from next window position 
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            #check for new char entering the window
            index = ord(s2[r]) - ord('a')
            countS2[index] += 1
            if countS1[index] == countS2[index]:
                matches += 1
            elif countS1[index] + 1 == countS2[index]:
                matches -= 1

            #check for char leaving the window
            index = ord(s2[l]) - ord('a')
            countS2[index] -= 1
            if countS1[index] == countS2[index]:
                matches += 1
            elif countS1[index] - 1 == countS2[index]:
                matches -= 1
            #slide the window
            l += 1
        return matches == 26





        