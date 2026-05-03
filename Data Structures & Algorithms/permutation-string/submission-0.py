class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Counts = [0] * 26
        for s in s1:
            s1Counts[ord(s) - ord('a')] += 1

        windowCounts = [0] * 26
        
        l = 0
        for r in range(len(s2)):
            windowCounts[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 > len(s1):
                windowCounts[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            isPermutation = True
            for i in range(26):
                if s1Counts[i] != windowCounts[i]:
                    isPermutation = False
            
            if isPermutation:
                return True

        return False
            
