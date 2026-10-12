class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        Max = 1
        l = 0 
        r = 1
        seen = set([s[0]])
        while r <= len(s) - 1 and l <= len(s) - 1:
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                r += 1
                if Max < r-l:
                    Max = r-l

        return Max

            

