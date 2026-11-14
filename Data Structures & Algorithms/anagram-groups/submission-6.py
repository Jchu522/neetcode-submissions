
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        anagrams = {}

        for word in strs:
            sort = "".join(sorted(word))

            if sort in anagrams:
                anagrams[sort] += [word]
            else:
                anagrams[sort] = [word]
        
        for val in anagrams.values():
            ret += [val]
            
        return ret



        

            

        