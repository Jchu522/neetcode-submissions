class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board) , len(board[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        q = []
        copy = []
        for r in range(rows):
            if board[r][0] == "O":
                q.append((r,0))
                copy.append((r,0))
            if board[r][cols-1] == "O":
                q.append((r,cols-1))
                copy.append((r,cols-1))
        
        for c in range(cols):
            if board[0][c] == "O":
                q.append((0,c))
                copy.append((0,c))
            if board[rows-1][c] == "O":
                q.append((rows-1,c))
                copy.append((rows-1,c))
        
    
        
        def bsf(Queue, Turn):
            while Queue:
                r,c = Queue.pop(0)
                board[r][c] = Turn

                for x,y in dirs:
                    x1, y1 = r+x, c+y
                    if 0 <= x1 < rows and 0 <= y1 < cols and board[x1][y1] == "O":
                        board[x1][y1] = Turn
                        Queue.append((x1,y1))
        
        bsf(q,"S")
        queue = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                
        
        




            

    