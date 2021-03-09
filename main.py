#######################################
#       The Knight's Tour Problem     #
#######################################
# Name: Jefferson Marques Costa Alves #
#              March 2021             #
#######################################
#
# Constants
#
# Start point of the tour
START_X, START_Y = 0, 0
# Board height and width
BOARD_X, BOARD_Y = 8, 8
# Amount cells of the board
MAX = (BOARD_X * BOARD_Y) - 1
# Empty cell
EMPTY = -1
'''
    5       4
6               3
        K
7               2
    8       1
'''
MOVES = [
    # 1
    [1, 2],
    # 2
    [2, 1],
    # 3
    [2, -1],
    # 4
    [1, -2],
    # 5
    [-1, -2],
    # 6
    [-2, -1],
    # 7
    [-2, 1],
    # 8
    [-1, 2],
]
'''
    Is it safe to move the knight to [x, y] position ?
    True - Yes
    False - No
'''
def isSafe(board, x, y):
    # x and y do not go out the board and that position is empty
    if 0 <= x < BOARD_X and 0 <= y < BOARD_Y and board[x][y] == EMPTY:
        return True
    return False
'''
    Recursive function that solves the problem
'''
def knightsTour(board, cont, cx, cy):
    # All the cells were filled ?
    if cont > MAX:
        # Return the filled board
        return board
    # If have cells to fill
    # Try some moves
    for x, y in MOVES:
        # Next move
        nx, ny = cx + x, cy + y
        # is it ok to go to the next move?
        if isSafe(board, nx, ny):
            # Choose that move
            board[nx][ny] = cont + 1
            # Calls recursively with the next point
            if knightsTour(board, cont + 1, nx, ny):
                return True
            # Backtracking
            board[nx][ny] = EMPTY
    # None moves were valid
    return False
'''
    Receives an empty board and returns a filled board with the solution
'''
def solve(board):

    # Initial point
    board[START_X][START_Y] = 1
    # Counter
    cont = 1
    # Calls the recursive function
    if not knightsTour(board, cont, START_X, START_Y):
        print("Doesn't have a solution!")
        exit(0)
    # Return the filled board
    return board
'''
    Shows the solution on the console
'''
def printMatrix(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
'''
    Main function
'''
def main():
    # Create a BOARD_X x BOARD_Y board
    board = [[EMPTY for j in range(BOARD_X)] for i in range(BOARD_Y)]
    # Solves the problem
    result = solve(board)
    # Shows the solution on the console.
    printMatrix(result)
'''
    Initial function of a python program
'''
if __name__ == '__main__':
    main()