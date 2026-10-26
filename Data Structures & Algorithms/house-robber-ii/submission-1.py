class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])

        arr = [0 for _ in range(len(nums)-1)]
        arr[0] = nums[0]
        arr[1] = max(nums[1], nums[0])
        
        for i in range(2, len(nums)-1):
            arr[i] = max(arr[i-2] + nums[i], arr[i-1])
        
        arr2 = [0 for _ in range(len(nums)-1)]
        arr2[0] = nums[1]
        arr2[1] = max(nums[2], nums[1])
        
        for j in range(3, len(nums)):
            arr2[j-1] = max(arr2[j-3] + nums[j], arr2[j-2])
        print(arr2, arr)

        return max(arr2[-1], arr[-1])