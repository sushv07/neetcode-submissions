"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # O(n log n) TC and O(1) SC
        intervals.sort(key = lambda i : i.start)

        # iterate through the intervals
        # compare prev and cur interval
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            # overlapping case
            if i1.end > i2.start:
                return False

        return True
            

