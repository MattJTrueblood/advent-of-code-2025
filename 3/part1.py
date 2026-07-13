import os

def largestDigit(line):
    """return (largest digit in string, index of first appearance)"""
    largest = -1
    largest_index = -1
    for i, c in enumerate(line):
        if int(c) > largest:
            largest = int(c)
            largest_index = i
    return largest, largest_index

def processLine(line):
    """get largest joltage in line"""
    first_digit, index = largestDigit(line[:-2])
    second_digit, _ = largestDigit(line[index+1:-1])
    return (first_digit * 10) + second_digit

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    for line in f:
        solution += processLine(line)

print(solution)