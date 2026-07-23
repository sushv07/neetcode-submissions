class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(n log n) TC and O(1) SC solution - becoz of sorting
        intervals.sort()
        
        # initialize output
        res = 0
        # initialize prevEnd value with the end value of the first interval
        prevEnd = intervals[0][1]

        # iterate through the rest of the intervals
        for start, end in intervals[1:]:
            # if non overlapping
            if start >= prevEnd:
                # update prevEnd  with cur End
                prevEnd = end
            # else, if overlapping
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

        