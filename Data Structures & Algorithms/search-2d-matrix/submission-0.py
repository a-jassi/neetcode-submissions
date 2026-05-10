class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowL, rowR = 0, len(matrix) - 1
        rowM = -1

        while rowL <= rowR:
            rowM = (rowL + rowR) // 2
            if target > matrix[rowM][-1]:
                rowL = rowM + 1
            elif target < matrix[rowM][0]:
                rowR = rowM - 1
            else:
                break
        
        if rowM == -1:
            return False
        
        row = matrix[rowM]
        colL, colR = 0, len(row) - 1
        while colL <= colR:
            mid = (colL + colR) // 2
            if row[mid] > target:
                colR = mid - 1
            elif row[mid] < target:
                colL = mid + 1
            else:
                return True
        
        return False