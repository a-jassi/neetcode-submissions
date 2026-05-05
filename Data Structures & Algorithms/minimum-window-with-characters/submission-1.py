class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
    
        tChars, windowChars = {}, {}
        for char in t:
            tChars[char] = 1 + tChars.get(char, 0)

        need = len(tChars)
        have = 0

        resL = resR = 0
        resLen = float('infinity')

        l = 0

        for r in range(len(s)):            
            windowChars[s[r]] = 1 + windowChars.get(s[r], 0)

            if s[r] in tChars and windowChars[s[r]] == tChars[s[r]]:
                have += 1
            
            while need == have:
                if (r - l + 1) < resLen:
                    resL = l
                    resR = r
                    resLen = r - l + 1
                
                windowChars[s[l]] -= 1
                if s[l] in tChars and windowChars[s[l]] < tChars[s[l]]:
                    have -= 1

                l += 1
        
        return s[resL:resR+1] if resLen != float('infinity') else ""
                
            


            

