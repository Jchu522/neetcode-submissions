class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        rows = cols = len(matrix)
        ret = []

        # 2,0 ,1,0 , 0,0 we are looking backwards
        for c in range(cols):
            temp = []
            for r in range(rows-1, -1, -1):
                temp.append(matrix[r][c])
            ret.append(temp)

        for i in range(rows):
            for j in range(cols):

                matrix[i][j] = ret[i][j]
        