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
        
def countAllFreshIngredientIds(ranges):
    """count all possible values within the ranges"""
    sorted_ranges = sorted(ranges, key=lambda r: r[0])
    combined_ranges = []
    current_combo = []
    for i, r in enumerate(sorted_ranges):
        if i == 0:
            current_combo = r
            continue
        if r[0] >= current_combo[0] and r[0] <= current_combo[1]:
            current_combo = [current_combo[0], max(current_combo[1], r[1])]
        else:
            combined_ranges.append(current_combo)
            current_combo = [r[0], r[1]]
    combined_ranges.append(current_combo)
 
    count = 0
    for r in combined_ranges:
        count += r[1]-r[0] + 1
    return count

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    ranges, _ = parseLines(allLines)
    solution = countAllFreshIngredientIds(ranges)

print(solution)