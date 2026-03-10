class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        raw = len(matrix) #3
        column = len(matrix[0]) #4
        for m in range(raw-1): #(0,1)
            for n in range(column-1): #(0,1,2)
                if matrix[m][n] != matrix[m+1][n+1]:
                    return False
        return True 
