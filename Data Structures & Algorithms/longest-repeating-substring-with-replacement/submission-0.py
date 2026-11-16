class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {chr(i):0 for i in range(ord('A'), ord('Z') + 1)}
        l = 0
        r = 0
        ret = 0
        while r < len(s):
            count[s[r]] += 1
            r += 1
            if r-l - max(count.values()) <= k:
                ret = max(r-l, ret)
            else:
                while (r-l - max(count.values()) > k):
                    count[s[l]] -= 1
                    l += 1
        return ret
