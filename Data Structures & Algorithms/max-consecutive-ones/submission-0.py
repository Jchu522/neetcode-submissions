class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        so = 0
        for i in nums:
            if i == 0:
                so = 0
                continue
            if i == 1:
                so += 1
                ret = max(so, ret)
        return ret
            