class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        res = 0

        l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            maxCount = max(counts.values())

            while (r - l + 1) - maxCount > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
            