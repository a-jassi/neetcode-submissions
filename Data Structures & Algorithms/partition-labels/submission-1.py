class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen = {}
        for i, c in enumerate(s):
            seen[c] = i
        
        size = 0
        end = 0
        res = []

        for i, c in enumerate(s):
            end = max(end, seen[c])
            size += 1

            if i == end:
                res.append(size)
                size = 0
        
        return res
            

            