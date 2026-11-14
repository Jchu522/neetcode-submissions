
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        ret = []
        for word in strs:
            anagrams = [0] * 26
            for i in word:
                anagrams[ord(i) - ord('a')] += 1
            if tuple(anagrams) in res:
                res[tuple(anagrams)] += [word]
            else:
                res[tuple(anagrams)] = [word]

        
        for key, val in res.items():
            ret += [val]
        return ret
        
        

        

            

        