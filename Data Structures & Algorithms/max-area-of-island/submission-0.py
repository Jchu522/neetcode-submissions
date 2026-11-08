class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r: int, c: int):

            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            count = 1 
            count += dfs(r-1, c)
            count += dfs(r+1, c)
            count += dfs(r, c-1)
            count += dfs(r, c+1)
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(dfs(r,c), maxArea)

        return maxArea





