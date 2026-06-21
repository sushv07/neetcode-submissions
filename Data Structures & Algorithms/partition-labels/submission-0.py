class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # O(n) TC and O(1) SC solution 
        # hashmap to track char's last index in s
        lastIndex = {}

        # populate hash map
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res
        