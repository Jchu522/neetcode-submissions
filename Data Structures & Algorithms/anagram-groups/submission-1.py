class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        if len(strs) == 1:
            return [strs]
        for word in strs:
            temp = sorted(word)
            temp = "".join(temp)
            if temp in ana:
                ana[temp] += [word]
            else:
                ana[temp] = [word]
        ret = []

        for key in ana.keys():
            ret += [ana[key]]

        return ret
