class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        # i reads the group, k writes the group's char
        k = i = 0

        #continue until every char is processed
        while i < n:
            # write group's char
            chars[k] = chars[i]
            # move to the next writing position
            k += 1
            # start checking after the cur char
            j = i + 1

            #move j while chars are same
            while j < n and chars[i] == chars[j]:
                j += 1

            #if the group has more than 1 char , write its count
            if j - i > 1:
                for c in str(j - i):
                    # store one count char
                    chars[k] = c
                    # moev to the next writing position
                    k += 1

            # move to the next group        
            i = j
            
        #return the compressed length
        return k