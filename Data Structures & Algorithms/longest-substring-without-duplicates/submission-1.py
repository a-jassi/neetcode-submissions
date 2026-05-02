class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        seenChars = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in seenChars:
                seenChars.remove(s[l])
                l += 1
            
            seenChars.add(s[r])
            res = max(res, len(seenChars))
        
        return res
            

                