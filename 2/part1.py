import os

def parseRanges(rangeStrs):
    ranges = []
    for rangeStr in rangeStrs:
        ranges += [rangeStr.split('-')]
    return ranges

def sumInvalidIDsInRange(start, end):
    """gets the sum of all invalid IDS in the range of [start, end] inclusive"""
    # edge case:  start and end both odd number of digits
    if len(start) % 2 != 0 and len(end) % 2 != 0 and len(start) == len(end):
        return 0
    # base case
    sum = 0
    for i in range(int(start), int(end) + 1):
        i_str = str(i)
        if len(i_str) % 2 != 0:
            continue
        middle = len(i_str) // 2
        first_half = i_str[:middle]
        second_half = i_str[middle:]
        if first_half == second_half:
            sum += i

    return sum

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allRangeStrs = f.read().split(',')
    allRanges = parseRanges(allRangeStrs)
    for r in allRanges:
        solution += sumInvalidIDsInRange(r[0], r[1])

print(solution)