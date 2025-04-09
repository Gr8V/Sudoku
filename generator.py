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