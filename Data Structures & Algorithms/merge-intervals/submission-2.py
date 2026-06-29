class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        i = 0

        while i < len(intervals):
            j = i + 1
            end = intervals[i][1]

            while j < len(intervals) and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1

            res.append([intervals[i][0], end])
            i = j
        
        return res