class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        result = []
        m, n = len(matrix), len(matrix[0])
        
        # Define the boundaries of the matrix
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top boundary
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            
            # Traverse from top to bottom along the right boundary
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left along the bottom boundary
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:
                # Traverse from bottom to top along the left boundary
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result



        