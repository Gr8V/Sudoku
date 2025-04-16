import random

def validSudoku():
    solvedSudoku = [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0]]
    fill_grid(solvedSudoku)
    return solvedSudoku
    
def is_valid(grid, row, col, num):
    if num in grid[row]:
        return False
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    box_start_row = (row//3)*3
    box_start_col = (col//3)*3
    for i in range(box_start_row, box_start_row+3):
        for j in range(box_start_col, box_start_col+3):
            if grid[i][j] == num:
                return False
            
    return True
    
def fill_grid(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                nums = list(range(1,10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if fill_grid(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i,j
    return None

def count_solutions(grid, max_sol = 2):
    empty_cell = find_empty_cell(grid)
    
    if empty_cell == None:
        return 1
    row, col = empty_cell
    total_sol = 0
    for num in range(1,10):
        if is_valid(grid,row,col,num):
            grid[row][col] = num
            
            total_sol += count_solutions(grid, max_sol)
            grid[row][col] = 0
            
            if total_sol >= max_sol:
                break
    return total_sol

def create_unsolved(emptyCells):
    unsolvedSudoku = validSudoku()

    
    positions = [(i,j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    
    removed = 0
    for row, col in positions:
        if removed >= emptyCells:
            break
        backup = unsolvedSudoku[row][col]
        unsolvedSudoku[row][col] = 0
        if count_solutions(unsolvedSudoku) != 1:
            unsolvedSudoku[row][col] = backup
        else:
            removed += 1
            
    return unsolvedSudoku
