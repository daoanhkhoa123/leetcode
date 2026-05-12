from dataclasses import dataclass
# import numpy as np

FULL = set(range(1, 10))

def slice2d(ls, ysf, yst, xsf, xst):
    return [l[xsf:xst] for l in ls[ysf:yst]]

def flatten(ls):
    res = []
    for l in ls:
        res += l
    return set(res)

def find_possible(puzzy):
    for y in range(len(puzzy)):
        for i in range(len(puzzy[0])):
            if puzzy[y][i] == 0:
                return y,i
    return None, None
            
def sudoku2(puzzle):
    """
    the solved puzzle as a 2d array of 9 x 9"""
    

    i,j = find_possible(puzzle)
    if i is None:
        return puzzle
       
    line = set(puzzle[i])
    column = {puzzle[r][j] for r in range(9)}
    bi = (i//3)*3
    bj = (j//3)*3
    box = {puzzle[r][c] for r in range(bi, bi+3) for c in range(bj, bj+3)}
    possible_sols = FULL - line - column - box
    
#     print("_"*10)
#     print(*puzzle, sep="\n")
#     print("aaa", slice2d(puzzle,0,9,j,j+1))
    if not possible_sols:
#         print(line, column, box)
#         print("we got it not fully yeah?")
        return None
    
    
    for sol in possible_sols:        
#         print(possible_sols)
        puzzle[i][j] = sol
        solved = sudoku2(puzzle)
        if solved is not None:
#             print("yay got it yeah?")
            return solved
        puzzle[i][j] = 0

def solve(board):
#     board = np.asarray(board)
#     print(board)
    return sudoku2(board)