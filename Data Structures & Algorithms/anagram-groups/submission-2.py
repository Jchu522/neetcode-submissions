
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        ret = []
        for s in strs:
            sort = "".join(sorted(s))
            if sort not in anagrams:
                anagrams[sort] = [s]
            else:
                anagrams[sort] += [s]

        for key, val in anagrams.items():
            ret += [val]

        return ret

            

        