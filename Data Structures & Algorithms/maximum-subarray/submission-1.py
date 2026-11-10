class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        cur = ret
        for i in range(1, len(nums)):
            if cur < 0:
                cur = nums[i]
            else:
                cur += nums[i]
            
            ret = max(cur, ret)

        return ret

