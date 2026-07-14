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
    split_count = 0
    current_beam_columns = set()
    next_beam_columns = set()
    for i, row in enumerate(grid):
        if i == 0:
            # find beam start
            for j, col in enumerate(grid[i]):
                if grid[i][j] == 'S':
                    next_beam_columns.add(j)
        else:
            for k in current_beam_columns:
                if grid[i][k] == '.':
                    next_beam_columns.add(k)
                elif grid[i][k] == '^':
                    next_beam_columns.add(k-1)
                    next_beam_columns.add(k+1)
                    split_count += 1
        current_beam_columns = next_beam_columns
        next_beam_columns = set()
    return split_count

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    grid = parseGrid(allLines)
    solution = countNumSplits(grid)

print(solution)