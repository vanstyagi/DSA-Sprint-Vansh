# Leetcode 36 - Valid Sudoku

class Solution(object):
    def isValidSudoku(self, board):
        seen = set()
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    row = f"{num} in row {i}"
                    col = f"{num} in col {j}"
                    box = f"{num} in box {i//3}-{j//3}"
                    
                    if row in seen or col in seen or box in seen:
                        return False
                    
                    seen.add(row)
                    seen.add(col)
                    seen.add(box)
        
        return True
