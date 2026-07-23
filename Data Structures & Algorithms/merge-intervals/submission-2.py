class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(n log n) TC and O(n) SC solution - since sorting is involved - sorting based on start values
        intervals.sort(key = lambda i : i[0])
        # initialize the output list with first value - to avoid edge case
        output = [intervals[0]]

        # iterate through the rest of the intervals
        for start, end in intervals[1: ]:
            # initialize with the end value of the most recent value in the output list
            lastEnd = output[-1][1]

            # check if cur interval overlaps with the lastEnd value of the most recent interval, if yes - merge
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)

            # if no overlap, just append to the output list
            else:
                output.append([start, end])
        return output 


        