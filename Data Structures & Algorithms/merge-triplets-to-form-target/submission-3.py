class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        curr = [-1, -1, -1]

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            curr = [max(t[0], curr[0]), max(t[1], curr[1]), max(t[2], curr[2])]
        
        return curr == target