class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, curr):
            if start >= len(s):
                res.append(curr[:])
            
            for i in range(start, len(s)):
                if self.isPalindrome(s, start, i):
                    curr.append(s[start:i+1])
                    backtrack(i+1, curr)
                    curr.pop()
        
        backtrack(0, [])
        return res
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
