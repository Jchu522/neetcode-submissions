class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ret = 0 
        temp = 0
        l = 0 
        r = len(heights) - 1
        while l < r:
            temp = min(heights[l], heights[r]) * (r - l )
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1 
            ret = max(ret, temp)

        return ret
