
import random
from generator import create_unsolved
from generator import is_valid


def print_sudoku(grid):

    # Column headers
    print("    a b c   d e f   g h i")
    print("  +-------+-------+-------+")
    

    for i in range(9):
        row = f"{i+1} | "  # Row label
        for j in range(9):
            row += f"{grid[i][j]} "
            if (j + 1) % 3 == 0:
                row += "| "
        print(row)
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")
            
def print_sudoku_highlighted(grid,selectedRow,selectedCol):
    #Converts column label (a,i) to index
    #if isinstance(selectedCol, str):
    #    selectedCol = ord(selectedCol) - ord('a')

    # Column headers
    print("    a b c   d e f   g h i")
    print("  +-------+-------+-------+")
    

    for i in range(9):
        row = f"{i+1} | "  # Row label
        for j in range(9):
            ishighlighted = selectedRow == i + 1 and selectedCol == j
            if ishighlighted:
                row = row.rstrip()
                row += f"[{grid[i][j]}]"
            else:
                row += f"{grid[i][j]} "
            if (j + 1) % 3 == 0:
                row += "| "
        print(row)
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")
            
    
    
def solve():
    solvedCells = []
    isSolved = False
    while isSolved == False:
        print(solvedCells)
        print_sudoku(Unsolved)
        #back to menu
        selectedCell = input("Enter which cell you want to select \"<row><column>\" :: ")
        if selectedCell in ["exit","restart","end"]:
            break
        #undo
        elif selectedCell == "undo":
            Unsolved[solvedCells[-1][0]][solvedCells[-1][1]] = 0
            print("Undo Successfull!!")
            continue
        
        #turn row and col into indexes
        row, col = [i for i in selectedCell]
        row = int(row)-1
        if isinstance(col, str):
            col = ord(col) - ord('a')
        
        #checks if selected cell is already solved or not
        if (Unsolved[row][col]) != 0:
            print("solved already")
            continue
        
        #prints sudoku with selected cell highlighted
        print_sudoku_highlighted(Unsolved, row+1, col)
        
        #takes value for the selected cell
        value = int(input("Enter Value :: "))
        
        #checks if it is valid and then inputs the value
        if is_valid(Unsolved,row,col,value):
            print("It is valid")
            Unsolved[row][col] = value
            solvedCells.append([row,col])
        else:
            print("It is Not valid")
            
        #checks if it is solved and ends
        unsolvedCells = 0
        for i in Unsolved:
            for j in i:
                if j == 0:
                    unsolvedCells+=1
        if unsolvedCells == 0:
            print("SUDOKU SOLVED!!!!!!!!!!")
            print("SUDOKU SOLVED!!!!!!!!!!")
            print("SUDOKU SOLVED!!!!!!!!!!")
            print("SUDOKU SOLVED!!!!!!!!!!")
            print("SUDOKU SOLVED!!!!!!!!!!")
            break
        

while True:
    
    print("SELECT DIFFICULTY")
    print("[1] Easy")
    print("[2] Medium")
    print("[3] Hard")
    print("[4] Expert")
    difficulty = int()
    try:
        difficulty = int(input(">>>"))
    except ValueError:
        print("Invalid Input. Exiting!")
        exit()

    emptyCells = 0

    match(difficulty):
        case 1:
            emptyCells = random.randint(17,27)
        case 2:
            emptyCells = random.randint(28,31)
        case 3:
            emptyCells = random.randint(32,35)
        case 4:
            emptyCells = random.randint(36,49)
        case _:
            print("Invalid choice. Exiting!")
    
    Unsolved = create_unsolved(emptyCells)
    unsolvedBackup = Unsolved
    solve()