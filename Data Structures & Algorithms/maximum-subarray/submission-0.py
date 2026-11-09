class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        curMax = 0

        for i in range(len(nums)):
            if curMax < 0:
                curMax = nums[i]
            else:
                curMax += nums[i]
            
            ret = max(ret, curMax)
        return ret