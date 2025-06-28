# Leetcode 73 - Set Matrix Zeroes

class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        row_zero = False

        # Step 1: Mark zeroes in first row & column
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True

        # Step 2: Set zeroes based on marks
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Step 3: Handle first column
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # Step 4: Handle first row
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0
