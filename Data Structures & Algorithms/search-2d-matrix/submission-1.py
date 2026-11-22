class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        bot, top = 0, rows-1

        while top >= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                bot = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else:
                break
        
        if not top >= bot:
            return False
            
        l, r = 0, cols - 1
        while r >= l:
            mid = (l + r ) // 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False
