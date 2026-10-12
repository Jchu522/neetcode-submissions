class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxSoFar = -1
        l = 0
        r = len(heights) - 1
        while l < r:
            temp = 0 
            if heights[l] > heights[r]:
                temp = heights[r] * (r-l)
                r -= 1
                
            else:
                temp = heights[l] * (r-l)
                l += 1
                
            
            if ((temp) > maxSoFar):
                maxSoFar = temp

        return maxSoFar
