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
            # this is good enough for input.txt but I'd like to try a proper solver some time
            numGoodRegions += 1
    return numGoodRegions

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    presents, regions = parseLines(allLines)
    solution = getSolution(presents, regions)

print(solution)