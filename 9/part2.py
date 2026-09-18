import os

def parseCoords(lines):
    coords = []
    for line in lines:
        if len(line) > 0:
            coords.append(tuple(map(int, line.split(','))))
    return coords

def isValidRectangle(pair, allCoords):
    # valid if the rectangle specified by pair is not intersected by any line segment
    # in the polygon described by allCoords (a list of the points in the polygon)
    # This isn't actually a generally correct solution, in fact it gives in an incorrect
    # result for sample.txt!  But it does work for input.txt because of the specific shape of
    # input.txt which simplifies down the problem significantly.

    # rectangle vertices
    rx1, rx2 = sorted(x for x, _ in pair["corners"])
    ry1, ry2 = sorted(y for _, y in pair["corners"])
    
    for i in range(0, len(allCoords) - 1):
        # current line segment
        lx1, lx2 = sorted(x for x, _ in allCoords[i:i+2])
        ly1, ly2 = sorted(y for _, y in allCoords[i:i+2])

        # check if this line segment intersects our rectangle
        x_overlap = max(rx1, lx1) < min(rx2, lx2)
        y_overlap = max(ry1, ly1) < min(ry2, ly2)
        x_valid = x_overlap or (lx1 == lx2 and rx1 < lx1 < rx2)
        y_valid = y_overlap or (ly1 == ly2 and ry1 < ly1 < ry2)
        
        if x_valid and y_valid:
            return False
            
    return True
        

def getPairsByRectangleSizeDescending(allCoords):
    allPairs = []
    for i in range(0, len(allCoords)):
            for j in range(i+1, len(allCoords)):
                pointA = allCoords[i]
                pointB = allCoords[j]
                currentRectSize = (abs(pointA[0]-pointB[0]) + 1) * (abs(pointA[1] - pointB[1]) + 1)
                pair = {"corners": [pointA, pointB], "size": currentRectSize}
                allPairs.append(pair)
    return sorted(allPairs, key=lambda x: x['size'], reverse=True)

def getSizeOfLargestValidRectangle(sortedPairs, allCoords):
    for p in sortedPairs:
        if isValidRectangle(p, allCoords):
            print(p) # I can later print the rectangle using visualizer.py
            return p["size"]
    return -1
    
solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    allCoords = parseCoords(allLines)
    sortedPairs = getPairsByRectangleSizeDescending(allCoords)
    allCoords.append(allCoords[0]) # adds the segment between the last point and the first
    solution = getSizeOfLargestValidRectangle(sortedPairs, allCoords)

print(solution)