# Leetcode 37 - Sudoku Solver

class Solution(object):
    def solveSudoku(self, board):
        def is_valid(r, c, val):
            for i in range(9):
                if board[r][i] == val or board[i][c] == val or board[3*(r//3) + i//3][3*(c//3) + i%3] == val:
                    return False
            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for ch in map(str, range(1, 10)):
                            if is_valid(i, j, ch):
                                board[i][j] = ch
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True
        
        solve()
