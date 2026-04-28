class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = defaultdict(int)

        for i in range(len(s)):
            seen[s[i]] += 1
            seen[t[i]] -= 1
        
        for counts in seen.values():
            if counts != 0:
                return False

        return True
        