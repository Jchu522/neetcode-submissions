class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev == nums[i]:
                return prev
            prev = nums[i]