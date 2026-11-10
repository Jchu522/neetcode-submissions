class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = []
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))
        counter = 0
        while q:
            counter += 1
            for i in range(len(q)):
                rows , cols = q.pop(0)
                for x, y in dirs:
                    x1 , y1 = rows + x, cols + y
                    if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and grid[x1][y1] != -1 and grid[x1][y1] > counter:
                        grid[x1][y1] = counter
                        q.append((x1,y1))

