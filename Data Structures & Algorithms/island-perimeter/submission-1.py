class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()

        def bfs(r:int ,c:int):
            count = 0
            q = [(r,c)]
            visited.add((r,c)) 
            while q:    
                r,c = q.pop(0)
                for x,y in dirs:
                    x1, y1 = r+x, c+y
                    if x1 < 0 or x1 >= rows or y1 >= cols or y1 < 0 or grid[x1][y1] == 0:
                        count += 1
                    elif (x1, y1) not in visited:
                        visited.add((x1, y1))
                        q.append((x1, y1))
                    
            return count
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r,c)
        





