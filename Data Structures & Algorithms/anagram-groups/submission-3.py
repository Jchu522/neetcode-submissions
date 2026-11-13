
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

        for val in anagrams.values():
            ret += [val]

        return ret

            

        