class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        for chr in s:
            seen[chr] = seen.get(chr, 0) + 1
        
        for chr in t:
            if chr not in seen:
                return False
            seen[chr] = seen[chr] - 1
        
        for chr in seen:
            if seen[chr] != 0:
                return False
        
        return True