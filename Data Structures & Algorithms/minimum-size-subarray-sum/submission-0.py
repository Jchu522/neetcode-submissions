class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        ret = 9999999999999
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total>= target:
                ret = min(r-l+1, ret)
                total -= nums[l]
                l += 1
                
        return ret if ret != 9999999999999 else 0


                
