import os

def parseGrid(lines):
    """parse the lines into a 2d array of chars"""
    grid = []
    for i, line in enumerate(lines):
        if len(line) > 0:
            grid.append([])
            for j in line:
                grid[i].append(j)
    return grid

def rollAt(grid, i, j):
    """check if there is a roll at [i][j] (if out of bounds, there is no roll)"""
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False
    else:
        return grid[i][j] == '@'
    
def rollAccessible(grid, i, j):
    """check if the roll at [i][j] is accessible"""
    check_coords = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
    adjacent_rolls = 0
    for coords in check_coords:
        if(rollAt(grid, coords[0], coords[1])):
            adjacent_rolls+=1
            if adjacent_rolls >= 4:
                return False
    return True


def solveGrid(grid):
    """find the solution: how many rolls can be removed"""
    accessible_count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if(grid[i][j] == '@'):
                if rollAccessible(grid, i, j):
                    accessible_count += 1
                    print("x", end='')
                else:
                    print('@', end='')
            else:
                print('.', end='')
        print("")
    return accessible_count


solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    grid = parseGrid(allLines)
    solution = solveGrid(grid)

print(solution)