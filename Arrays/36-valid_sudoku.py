'''
36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3x3 subboxes of the grid must contain the digits 1-9 without repetition.
'''

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # check every row
        for row in board:
            row_elements_set = set()
            for element in row:
                if element != '.' and element in row_elements_set:
                    return False
                row_elements_set.add(element)
        # check every column
        for column in range(9):
            column_elements_set = set()
            for row in range(9):
                element = board[row][column]
                if element != '.' and element in column_elements_set:
                    return False
                column_elements_set.add(element)

        # check every subbox
        for row_index in range(3):
            for column_index in range(3):
                subbox_elements_set = set()
                for row in range(3):
                    for column in range(3):
                        element = board[row_index * 3 + row][column_index * 3 + column]
                        if element != '.' and element in subbox_elements_set:
                            return False
                        subbox_elements_set.add(element)

        return True
            
if __name__ == '__main__':
    solution = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    
    print(solution.isValidSudoku(board))

    board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    print(solution.isValidSudoku(board))

