from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        ret = 0

        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = "0"
            while queue:

                r,c = queue.popleft()

                for x,y in dirs:
                    x1, y1 = r+x, c+y
                    if 0 <= x1 < rows and 0 <= y1 < cols and grid[x1][y1] == "1":
                        grid[x1][y1] = "0"
                        queue.append((x1,y1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    ret += 1
                    bfs(r,c)
        return ret