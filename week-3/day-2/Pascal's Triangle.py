class Solution:
    def generate(self, numRows):
        triangle = []
        
        for i in range(numRows):
            # Start each row with '1'
            row = [1] * (i + 1)
            
            # Each triangle element (except the first and last) is the sum of the two elements above it
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            # Append the current row to the triangle
            triangle.append(row)
        
        return triangle
