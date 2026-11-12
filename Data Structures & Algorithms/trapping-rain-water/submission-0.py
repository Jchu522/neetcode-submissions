class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        MaxL = height[0]
        MaxR = height[r]
        ret = 0
        while r >= l:
            if MaxL > MaxR:
                temp = min(MaxR, MaxL) - height[r]
                ret += temp if temp > 0 else 0 
                MaxR = max(height[r], MaxR)
                r -= 1  
                
            elif MaxL <= MaxR:
                temp = min(MaxR, MaxL) - height[l]
                ret += temp if temp > 0 else 0 
                MaxL = max(height[l], MaxL)
                l += 1  
        return ret
            
