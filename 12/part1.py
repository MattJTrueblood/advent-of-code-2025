import os

def parseLines(lines):
    return {}

def getSolution():
    return -1

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample.txt")) as f:
    allLines = f.read().split('\n')
    devices = parseLines(allLines)
    solution = getSolution()

print(solution)