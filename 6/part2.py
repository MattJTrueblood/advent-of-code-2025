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


def parseOps(grid):
    """parse the lists of operators and operands from the grid reading right to left top to bottom"""
    operands = []
    operators = []

    current_operands = []
    current_number = ""
    for col in range(len(grid[0])-1, -1, -1):
        for row in range(0, len(grid)):
            val = grid[row][col]
            if val == '*' or val == '+':
                operators.append(val)
            elif val != ' ':
                current_number += val
        if current_number == "":
            operands.append(current_operands)
            current_operands = []
            continue
        current_operands.append(int(current_number))
        current_number = ""

    return operands, operators

def sumSolutions(operands, operators):
    """solve each problem and then sum them up"""
    result = 0
    for i, op in enumerate(operators):
        if(op == '*'):
            solution = math.prod(operands[i])
            result += solution
        else:
            solution = sum(operands[i])
            result += solution
    return result
            

solution = 0
# NOTE:  ADDED A WHITESPACE COLUMN ON THE FAR LEFT EDGE OF INPUT AND SAMPLE TXT
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    grid = parseGrid(allLines)
    operands, operators = parseOps(grid)
    solution = sumSolutions(operands, operators)

print(solution)