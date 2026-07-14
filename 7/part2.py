import os
import math

def parseGrid(lines):
    """parse the lines into a 2d array of chars"""
    grid = []
    for i, line in enumerate(lines):
        if len(line) > 0:
            grid.append([])
            for j in line:
                grid[i].append(j)
    return grid

def countNumSplits(grid):
    """track how many tachyons are in each row (across timelines) row by row"""
    current_beam_columns = [0] * len(grid[0])
    next_beam_columns = [0] * len(grid[0])
    for i, row in enumerate(grid):
        if i == 0:
            # find beam start
            for j, col in enumerate(grid[i]):
                if col == 'S':
                    next_beam_columns[j] = 1
        else:
            for j, col in enumerate(current_beam_columns):
                if grid[i][j] == '.' and col > 0:
                    next_beam_columns[j] += col
                elif grid[i][j] == '^' and col > 0:
                    next_beam_columns[j-1] += col
                    next_beam_columns[j+1] += col
        current_beam_columns = next_beam_columns
        next_beam_columns = [0] * len(grid[0])
    return sum(current_beam_columns)
    

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    grid = parseGrid(allLines)
    solution = countNumSplits(grid)

print(solution)