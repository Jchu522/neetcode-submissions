class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ret = ""
        cur = 0
        for i in spaces:
            ret += (s[cur:i] + " ")
            cur = i
        ret += (s[cur:])
        return ret


