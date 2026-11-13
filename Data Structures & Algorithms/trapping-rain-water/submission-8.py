class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        maxR = height[r]
        maxL = height[l]
        ret = 0
        while r > l:

            if maxR > maxL:
                l += 1

                maxL = max(height[l], maxL)
                
                ret += maxL - height[l] 

            else:
                r -= 1
                maxR = max(height[r], maxR)
                ret += maxR - height[r] 
        
        return ret