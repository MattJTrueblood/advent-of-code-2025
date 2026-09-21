import os

def parseLines(lines):
    presents = []
    regions = []
    for i in range(0, 6):
        current_present_lines = lines[i*5:(i*5)+4]
        current_present = {
            "shape": current_present_lines[1:4],
        }
        current_present["size"] = getPresentSize(current_present)
        current_present = findAllRotations(current_present)
        presents.append(current_present)

    for line in lines[30:]:
        parts = line.split(':')
        region = {
            "dimensions": [int(x) for x in parts[0].split('x')],
            "numPresents": [int(x) for x in parts[1][1:].split(' ')]
        }
        regions.append(region)
    print(presents)
    print(regions)
    return presents, regions

def findAllRotations(present):
    grid = tuple(present['shape'])
    unique_shapes = set()
    for _ in range(4):
        grid = tuple("".join(row) for row in zip(*grid[::-1])) # rotate
        flipped = tuple(row[::-1] for row in grid) # flip
        unique_shapes.add(grid)
        unique_shapes.add(flipped)
    return {
        'shapes': [list(shape) for shape in unique_shapes], 
        'size': present['size']
    }

def getPresentSize(present):
    size = 0
    for row in present["shape"]:
        size += row.count('#')
    return size

def getSolution(presents, regions):
    numGoodRegions = 0
    for region in regions:
        totalRegionSize = region["dimensions"][0] * region["dimensions"][1]
        sumPresentsSize = 0
        for i, presentsCount in enumerate(region['numPresents']):
            sumPresentsSize += presents[i]["size"] * presentsCount
        if sumPresentsSize > totalRegionSize:
            continue # impossible region, too many presents no matter how you arrange them
        else:
            if presentsCanAllFit(presents, region):
                numGoodRegions += 1
    return numGoodRegions

def presentsCanAllFit(presents, region):
    # TODO
    print(presents)
    print(region)
    return True

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    presents, regions = parseLines(allLines)
    solution = getSolution(presents, regions)

print(solution)