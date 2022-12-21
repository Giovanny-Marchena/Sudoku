'''
Sudoku Rules:
1. Each row must contain the numbers 1-9 exactly once each
2. Each column must contain the numbers 1-9 exactly once each
3. Each 3×3 box must contain the numbers 1-9 exactly once each
'''

'''
Requirements:
Generate board: Program must generate a 9x9 board with random numbers with blank cells
Code must check rows & col with backtracking, to validate  that the number is valid

'''

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
class Board:
    def __init__(self, board):
        self.board = board

    def print_board(bo):
        for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(bo[i][j])
                else:
                    print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

Board.print_board(board)

