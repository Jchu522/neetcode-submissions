class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        ret = 1
        prev = nums[0]
        temp = ret
        for i in range(1,len(nums)):
            if nums[i] == prev:
                continue
            if nums[i] == prev + 1:
                prev += 1
                temp += 1
            else:
                temp = 1
                prev = nums[i]
            ret = max(temp, ret)
        return ret
            

            

