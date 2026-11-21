class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]

        subs = self.subsets(nums[1:])
        temp = []
        for sub in subs:
            sub_copy = sub.copy()
            sub_copy.append(nums[0])
            temp.append(sub_copy)
        subs += temp
        return subs







        # ret = [[]]
        
        # for n in nums:
        #     temp = []
        #     for subset in ret:
        #         subset_copy = subset.copy()
        #         subset_copy.append(n)
        #         temp.append(subset_copy)
        #     ret += temp
        # return ret
           