class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Counts = [0] * 26
        s2Counts = [0] * 26
        for i in range(len(s1)):
            s1Counts[ord(s1[i]) - ord('a')] += 1
            s2Counts[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Counts[i] == s2Counts[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Counts[index] += 1
            if s1Counts[index] == s2Counts[index]:
                matches += 1
            elif s1Counts[index] + 1 == s2Counts[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Counts[index] -= 1
            if s1Counts[index] == s2Counts[index]:
                matches += 1
            elif s1Counts[index] - 1 == s2Counts[index]:
                matches -= 1
            l += 1

        return matches == 26
            
