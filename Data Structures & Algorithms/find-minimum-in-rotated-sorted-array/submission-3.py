class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = (r + l) // 2
        while l < r:
            mid = (r + l) // 2
            if nums[r] < nums[mid]:
                
                l = mid + 1
            else:
                # r = mid because we havent checked mid yet
                r = mid 
            
        
        return nums[l]
