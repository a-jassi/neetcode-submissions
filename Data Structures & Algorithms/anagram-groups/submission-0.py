class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        # O(n * mlogm) -- n = len(strs), m = len(longest string)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams.setdefault(sorted_s, []).append(s)
        
        return list(anagrams.values())
        