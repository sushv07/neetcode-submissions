class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Optimal O(n + m) TC and SC O(m)

        #Edge case check
        if t == "":
            return ""
        
        #2 hashmaps to track count
        countT, window = {}, {}
        #result vars
        res, resLen = [-1, -1], float("infinity")

        #Populate countT map
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        #counters to keep track of counts
        have, need = 0, len(countT)

        #sliding window begins
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            #If count matches, increment have counter
            if c in countT and window[c] == countT[c]:
                have += 1
            
            #while the counts are matching, check if window length is less than 
            #the prev length 
            while have == need:
                #update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                #decrement count in window map for left char
                #pop the left char
                window[s[l]] -= 1

                #if popping the count makes the window map char count lesser than the target char count
                #decrement "have" counter
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                #"pop left and slide"
                l += 1
        l, r = res        
        return s[l:r+1] if resLen != float("infinity") else ""     

            

        
        
        
