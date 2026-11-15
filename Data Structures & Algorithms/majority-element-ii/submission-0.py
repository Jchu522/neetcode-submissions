class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        ret = [] 

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        for num, val in freq.items():
            if val > len(nums) // 3:
                ret += [num]
                
        return ret