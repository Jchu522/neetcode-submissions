class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        
        for n in nums:
            temp = []
            for subset in ret:
                subset_copy = subset.copy()
                subset_copy.append(n)
                temp.append(subset_copy)
            ret += temp

        return ret
            #take

            #no take

        


            
