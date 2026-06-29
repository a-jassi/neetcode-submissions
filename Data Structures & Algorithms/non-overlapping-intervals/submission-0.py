class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0

        i = 0
        while i < len(intervals):
            j = i + 1
            end = intervals[i][1]

            while j < len(intervals) and end > intervals[j][0]:
                end = min(end, intervals[j][1])
                res += 1
                j += 1
            
            i = j
        
        return res
            