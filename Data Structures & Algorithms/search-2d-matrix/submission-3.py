class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1

        while l <= r:
            mid = (l + r) // 2
            mRow = mid // COLS
            mCol = mid % COLS
            
            if matrix[mRow][mCol] == target:
                return True
            elif matrix[mRow][mCol] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False