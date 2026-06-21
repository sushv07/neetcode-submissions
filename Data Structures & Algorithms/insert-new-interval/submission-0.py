class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # TC O(n) and SC O(n)
        # output list - for new set of intervals
        res = []

        # iterate through the list of intervals
        for i in range(len(intervals)):
            # edge cases
            # if new interval comes before the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                #appending the remaing sublists
                return res + intervals[i:]
            # if new interval comes after the current interval - but we don't append the new Interval yet as there are chances that it might overlap with others
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # if new interval is overlapping with the remaining intervals
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        #if newInterval doesn't fit any of the above cases, append it at the end
        res.append(newInterval)

        return res

        