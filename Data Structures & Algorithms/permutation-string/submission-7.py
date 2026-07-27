class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Counts = {}
        s2Counts = {}
        matching = 0

        for s in s1:
            s1Counts[s] = 1 + s1Counts.get(s, 0)
        
        l = 0
        for r in range(len(s2)):
            s2Counts[s2[r]] = 1 + s2Counts.get(s2[r], 0)
            if s2[r] in s1:
                if s2Counts[s2[r]] == s1Counts[s2[r]]:
                    matching += 1
                elif s2Counts[s2[r]] == s1Counts[s2[r]] + 1:
                    matching -= 1
                    

            while (r - l + 1) > len(s1):
                s2Counts[s2[l]] -= 1

                if s2[l] in s1:
                    if s2Counts[s2[l]] == s1Counts[s2[l]]:
                        matching += 1
                    elif s2Counts[s2[l]] == s1Counts[s2[l]] - 1:
                        matching -= 1
                l += 1
            
            if matching == len(s1Counts):
                return True
        
        return False
        

