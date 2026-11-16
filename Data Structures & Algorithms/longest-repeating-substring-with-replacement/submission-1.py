class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {chr(i):0 for i in range(ord('A'), ord('Z') + 1)}
        l = 0
        r = 0
        ret = 0
        max_freq = 0
        while r < len(s):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])
            r += 1
            if r-l - max_freq <= k:
                ret = max(r-l, ret)
            else:
                while (r-l - max_freq) > k:
                    count[s[l]] -= 1
                    l += 1
        return ret
