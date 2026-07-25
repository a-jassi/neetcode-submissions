class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        
        l = r = 0

        while l < len(word1) and r < len(word2):
            res.append(word1[l])
            res.append(word2[r])
            l += 1
            r += 1
        
        for i in range(l, len(word1)):
            res.append(word1[i])
        
        for i in range(r, len(word2)):
            res.append(word2[i])
        
        return "".join(res)
    
        
