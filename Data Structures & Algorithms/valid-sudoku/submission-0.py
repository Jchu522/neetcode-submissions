class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        square = {} #key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                if r not in rows:
                     rows[r] = set()
                if c not in cols: 
                    cols[c] = set()
                if (r//3,c//3) not in square:
                    square[(r//3,c//3)] = set()
                if (val in rows[r] or
                    val in cols[c] or 
                    val in square[(r//3,c//3)]):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                square[(r//3,c//3)].add(val)
        return True



                