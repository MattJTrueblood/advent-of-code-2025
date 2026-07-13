import os
import math


def processLine(line, current):
    """applies the instruction, returns (num_clicks from this instruction, new position)"""
    n = int(line[1:])
    next = 0
    if(line[0] == 'L'):
        next = current - n
    else:
        next = current + n
    if(next == 0):
        return 1, next % 100
    elif(next < 0):
        return math.floor(abs(next) / 100) + (1 if current > 0 else 0), next % 100
    else:
        return math.floor(next / 100), next % 100

current = 50
solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    for line in f:
        clicks, current = processLine(line, current)
        solution += clicks

print(solution)