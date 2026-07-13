import os

def parseLines(lines):
    """parse the two lists from the input data"""
    fresh_ranges = []
    ids = []
    reading_ranges = True
    for line in lines:
        if len(line) == 0:
            reading_ranges = False
            continue
        if reading_ranges:
            fresh_ranges.append(list(map(int, line.split('-'))))
        else:
            ids.append(int(line))
    return fresh_ranges, ids
        
def countFreshIngredients(ranges, ids):
    """count num ingredient ids that exist within at least one of ranges"""
    count = 0
    for id in ids:
        for r in ranges:
            if(id >= r[0] and id <= r[1]):
                count += 1
                break
    
    return count

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    ranges, ids = parseLines(allLines)
    solution = countFreshIngredients(ranges, ids)

print(solution)