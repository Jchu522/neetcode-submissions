class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                continue
            product *= nums[i]
        
        ret= [product for i in range(len(nums))]

        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(len(ret)):
                    ret[j] = 0 
                ret[i] = product if zero == 1 else 0
                return ret

            ret[i] = ret[i] // nums[i]

        return ret
            
