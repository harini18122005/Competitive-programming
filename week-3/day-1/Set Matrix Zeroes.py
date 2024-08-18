class Solution:
    def setZeroes(self, matrix):
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # Check if the first row needs to be set to zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Check if the first column needs to be set to zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        # Use the first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Nullify rows based on markers
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        # Nullify columns based on markers
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # Nullify the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Nullify the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0



        