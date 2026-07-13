import os

def processLine(line, current):
    """applies the instruction, returns new position"""
    n = int(line[1:])
    if(line[0] == 'L'):
        current -= n
    else:
        current += n
    return current % 100

current = 50
solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    for line in f:
        current = processLine(line, current)
        if(current == 0):
            solution += 1

print(solution)