
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        anagrams = defaultdict(list)
        for s in strs:
            a = [0] * 26
            for i in s:
                a[ord(i) - ord('a')] += 1
            anagrams[tuple(a)] += [s]

        for vals in anagrams.values():
            ret.append(vals)
            
        return ret
            







        

            

        