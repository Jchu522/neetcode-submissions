class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if t == "":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c,0)

        has, need = 0, len(countT)
        res = [-1,-1]
        resLen = 9999999
        l = 0
        for r, ch in enumerate(s):
            window[ch] = 1 + window.get(ch,0)
            if ch in countT and countT[ch] == window[ch]:
                has += 1
                
            while has == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    has -=1
                l += 1

        l,r = res
        return s[l:r+1] if resLen != 9999999 else ""