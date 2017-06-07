Project Euler #96: Su Doku
https://www.hackerrank.com/contests/projecteuler/challenges/euler096/submissions/code/46088194

def read_sudoku():
    sudoku = []
    for i in range(9):
        inp_str = input()
        sudoku.append([int(c) for c in inp_str])
    return sudoku

def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            print(sudoku[i][j],sep='',end='')
        print()

def find_numbers(sudoku, i, j):
    numbers = list(range(1,10))
    for x in sudoku[i]:
        if numbers.count(x) != 0: numbers.remove(x)
    for k in range(9):
        x = sudoku[k][j]
        if numbers.count(x) != 0: numbers.remove(x)
    k, m = i // 3, j // 3
    for k1 in range(k*3, k*3 + 3):
        for m1 in range(m*3, m*3 + 3):
            x = sudoku[k1][m1]
            if numbers.count(x) != 0: numbers.remove(x)
    return numbers

def sudoku_solve(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0: 
                possible_values = find_numbers(sudoku, i, j)
                n = len(possible_values)
                if n == 0: return False
                else: 
                    for x in possible_values:
                        sudoku[i][j] = x
                        if (sudoku_solve(sudoku)): return True
                    sudoku[i][j] = 0
                    return False
    return True


sudoku_inp = read_sudoku()
sudoku_out = list(x.copy() for x in sudoku_inp)
solved = sudoku_solve(sudoku_out)
print_sudoku(sudoku_out)