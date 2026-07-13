import os

def parseRanges(rangeStrs):
    """convert a list of strings in format "A-B" to a list of pairs of strings [A,B] """
    ranges = []
    for rangeStr in rangeStrs:
        ranges += [rangeStr.split('-')]
    return ranges

def sumInvalidIDsInRange(start, end):
    """gets the sum of all invalid IDS in the range of [start, end] inclusive"""
    sum_invalid_ids = 0
    for i in range(int(start), int(end) + 1):
        i_str = str(i)
        i_is_invalid = False
        for j in range (2, len(i_str) + 1):
            # try splitting i into j equally sized blocks
            if len(i_str) % j == 0:
                block_size = len(i_str) // j
                all_blocks = [i_str[k: k+ block_size] for k in range(0, len(i_str), block_size)]
                if all(block==all_blocks[0] for block in all_blocks):
                    i_is_invalid = True;
                    break

        if i_is_invalid:
            sum_invalid_ids += i

    return sum_invalid_ids

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allRangeStrs = f.read().split(',')
    allRanges = parseRanges(allRangeStrs)
    for r in allRanges:
        solution += sumInvalidIDsInRange(r[0], r[1])

print(solution)