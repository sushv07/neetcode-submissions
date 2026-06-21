class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        #Initialize value as empty list, if key not present
        values = self.timeMap.get(key, [])
        
        #Binary Search on the list of values
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l+r) // 2
            #if a valid value is found, then assign it to the result, 
            #and continue with binary search
            #if end of list, return the result
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res        
