class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ret = 0
        for i in details:
            if int(i[11:13]) > 60:
                ret += 1
        return ret 