class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Counts = {}
        for s in s1:
            s1Counts[s] = 1 + s1Counts.get(s, 0)
        
        s2Counts = {}
        l = 0

        for r in range(len(s2)):
            s2Counts[s2[r]] = 1 + s2Counts.get(s2[r], 0)

            while (r - l + 1) > len(s1):
                s2Counts[s2[l]] -= 1
                if s2Counts[s2[l]] == 0:
                    del s2Counts[s2[l]]
                l += 1
            
            if s2Counts == s1Counts:
                return True
        
        return False
        

