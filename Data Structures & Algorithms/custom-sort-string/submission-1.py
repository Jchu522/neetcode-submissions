class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = [0]*26
        for i in s:
            freq[ord(i)-97] += 1
        
        # print(freq)

        res = ""
        for c in order:
            res += c*freq[ord(c)-97]
            freq[ord(c)-97] = 0
        # print(res)
        
        for i in range(26):
            if freq[i] != 0:
                res += chr(i+97)*freq[i]
        
        return res