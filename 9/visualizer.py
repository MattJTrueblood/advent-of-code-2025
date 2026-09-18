import os
import matplotlib.pyplot as plt

def parseCoords(lines):
    coords = []
    for line in lines:
        if len(line) > 0:
            coords.append(tuple(map(int, line.split(','))))
    return coords

def draw(allCoords):
    x, y = zip(*allCoords)
    plt.figure()
    plt.fill(x, y, color="green", edgecolor="red", linewidth=5)

    # part 2 solution from sample.txt
    cornerA = [9, 5]
    cornerB = [2, 3]
    rect_x = [cornerA[0], cornerB[0], cornerB[0], cornerA[0]]
    rect_y = [cornerA[1], cornerA[1], cornerB[1], cornerB[1]]
    plt.fill(rect_x, rect_y, color="yellow", edgecolor="purple", linewidth=2)

    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.show()

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample.txt")) as f:
    allLines = f.read().split('\n')
    allCoords = parseCoords(allLines)
    draw(allCoords)
