
def find_next_cell(puzzle):
    # aim: finds an empty cell that is not filled yet (represented with zero -> 0)
    # input: list of lists
    # output: tuple (row, col) OR tuple (None, None) if there is none

    # looping through rows
    for r in range(9):
        # looping through columns
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c       
    return None, None


def valid_guess(puzzle, guess, row, col):
    # aim: verify if the guesses are valid answers (need to check each row, column, and 3x3 grid)
    # input: list of lists, guess, row, col
    # output: True if valid, False otherwise

    # step 1: check the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # step 2: check the column
    # note: use .append() to create a vertical/column list to loop through and check 
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False 
    
    # step 3: check the 3x3 grid
    # divide the whole puzzle into 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if puzzle[r][c] == guess:
                return False

    # pass all the test -> the guess is valid         
    return True
    

def solve_sudoku(puzzle):
    # aim: utilize backtracking to solve the puzzle by mutating the puzzle to be the solution (if it exists)
    # input: list of lists
    # output: a solution OR unsolvable

    # step 1: pick a cell to start
    row, col = find_next_cell(puzzle)

    # case 1: there are no empty cells left
    if row is None:
        return True 
    
    # case 2: there are empty cells
    # step 2: take a guess between 1 to 9
    for guess in range(1, 10):

        # step 3: check if the guess is valid
        if valid_guess(puzzle, guess, row, col):

            # case 1: if the guess is valid, mutate the puzzle with the guess
            puzzle[row][col] = guess
            # call function recursively with updated puzzle
            if solve_sudoku(puzzle):
                return True
            
        # case 2: if the guess is NOT valid, reset the guess
        # BACKTRACK and try a new number 
        puzzle[row][col] = 0

    # step 4: if none of the guesses work, this means the puzzle is UNSOLVABLE
    return False 



"""
# easy 
if __name__ == '__main__':
    example_board = [
        [0,8,0,6,4,0,0,0,7],
        [7,6,0,5,3,0,9,0,0],
        [0,0,0,0,2,7,0,0,3],
        [1,4,0,9,6,2,0,7,0],
        [2,0,0,3,7,0,0,0,1],
        [0,7,0,0,8,0,4,2,9],
        [5,1,0,0,9,6,8,0,0],
        [0,0,0,0,0,8,7,0,5],
        [0,0,0,7,0,0,0,9,6]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
"""

"""
# master 
if __name__ == '__main__':
    example_board = [
        [0,0,4,0,0,8,0,0,6],
        [0,0,5,2,0,0,1,8,0],
        [0,1,0,0,0,0,0,0,7],
        [0,0,2,0,9,0,0,0,0],
        [0,0,0,0,0,0,0,0,1],
        [0,5,0,0,0,7,3,4,0],
        [4,0,0,7,0,0,0,0,0],
        [0,3,0,0,0,4,8,5,0],
        [0,0,0,0,0,0,0,6,0]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
"""

"""
# invalid board
if __name__ == '__main__':
     example_board = [
        [0,0,9,0,7,0,0,0,5],
        [0,0,2,1,0,0,9,0,0],
        [1,0,0,0,2,8,0,0,0],
        [0,7,0,0,0,5,0,0,1],
        [0,0,8,5,1,0,0,0,0],
        [0,5,0,0,0,0,3,0,0],
        [0,0,0,0,0,3,0,0,6],
        [8,0,0,0,0,0,0,0,0],
        [2,1,0,0,0,0,0,8,7]
    ]
     print(solve_sudoku(example_board))
     print(example_board)
"""