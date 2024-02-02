#https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_set = set()
        #checking the rows
        for i in range(0,9):
            
            row_set.clear()
            for j in range(0,9):
                if board[i][j] in row_set:
                    return False
                if board[i][j] != ".":
                    row_set.add(board[i][j])
               
        #checking the columns
        for i in range(0,9):
            column_set = set()
            column_set.clear
            for j in range(0,9):
                if board[j][i] in column_set:
                    return False
                if board[j][i] != ".":
                    column_set.add(board[j][i])
                
        
        #checking the 3x3 sub-boxes
        col=0
        for iter in range(0,3):
            for row in range(0,9,3):
                sub_box = set()
                sub_box.clear
                for i in range(row , row + 3):
                    for j in range(col , col + 3):
                        if board[i][j] in sub_box:
                            return False
                        if board[i][j] != ".":
                            sub_box.add(board[i][j])
            col+=3
        
        return True
