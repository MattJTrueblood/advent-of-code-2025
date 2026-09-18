import os

def parseCoords(lines):
    coords = []
    for line in lines:
        if len(line) > 0:
            coords.append(tuple(map(int, line.split(','))))
    return coords

def getSizeOfLargestRectangle(allCoords):
    largestSize = -1
    for i in range(0, len(allCoords)):
        for j in range(i+1, len(allCoords)):
            pointA = allCoords[i]
            pointB = allCoords[j]
            currentRectSize = (abs(pointA[0]-pointB[0]) + 1) * (abs(pointA[1] - pointB[1]) + 1)
            largestSize = max(largestSize, currentRectSize)
    return largestSize

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    allCoords = parseCoords(allLines)
    solution = getSizeOfLargestRectangle(allCoords)

print(solution)