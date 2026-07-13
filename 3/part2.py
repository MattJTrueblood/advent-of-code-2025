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
    digits = []
    current_left_bound = -1
    for i in range(13, 1, -1):
        digit_i, digit_index = largestDigit(line[current_left_bound + 1:(i * -1) + 1])
        current_left_bound += digit_index + 1
        digits.append(digit_i)

    return int("".join(map(str, digits)))

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    for line in f:
        solution += processLine(line)

print(solution)
