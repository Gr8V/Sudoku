from generator import validSudoku

solvedSudoku = validSudoku()

for i in solvedSudoku:
    print(i, end="\n")