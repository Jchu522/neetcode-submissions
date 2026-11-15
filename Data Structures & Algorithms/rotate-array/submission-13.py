class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        k = k % len(nums)
        for i in range(len(nums)-k, len(nums)):
            temp.append(nums[i])
        
        temp += nums[:len(nums)-k]

        for i, val in enumerate(temp):
            if i < len(nums):
                nums[i] = val 
        

