class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        ret = 0
        
        # 1. Skip trailing spaces at the end of the string
        while i >= 0 and s[i] == " ":
            i -= 1
            
        # 2. Count characters of the last word
        while i >= 0 and s[i] != " ":
            ret += 1
            i -= 1
            
        return ret
                

            