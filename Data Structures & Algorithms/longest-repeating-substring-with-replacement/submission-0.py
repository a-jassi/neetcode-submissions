class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] += 1

            mostCommonCount = 0
            for count in counts.values():
                if count > mostCommonCount:
                    mostCommonCount = count
            
            while (r - l + 1) - mostCommonCount > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res