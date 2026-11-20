class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n,res = len(nums), 0 
        for i in range(n):
            temp = 0
            for j in range(i,n):
                temp += nums[j]
                if temp % k == 0:
                    res += 1
        return res

