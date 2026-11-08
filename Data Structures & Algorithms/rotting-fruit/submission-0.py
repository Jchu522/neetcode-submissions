class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        ret = 0
        queue = []
        fruits = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fruits += 1

        while queue and fruits > 0:

            for i in range(len(queue)):
                r,c = queue.pop(0)
                for x,y in dirs:
                    x1, y1 = x + r, y + c
                    if 0 <= x1 < rows and 0 <= y1 < cols and grid[x1][y1] == 1:
                        grid[x1][y1] = 2
                        fruits -= 1
                        queue.append((x1,y1))
            ret += 1


        if fruits == 0:
            return ret 
        else:
            return -1


                    