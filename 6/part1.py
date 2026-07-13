import os
import math

def parseLines(lines):
    """parse the lists of operators and operands from the lines"""
    operands = []
    operators = []
    for i, line in enumerate(lines):
        if len(line) > 0:
            words = line.split()
            if i == 0:
                for w in words:
                    operands.append([int(w)])
            elif words[0] == "*" or words[0] == "+":
                for w in words:
                    operators.append(w)
            else:
                for j, w in enumerate(words):
                    operands[j].append(int(w))
    
    return operands, operators

def sumSolutions(operands, operators):
    """solve each problem and sum them up"""
    result = 0
    for i, op in enumerate(operators):
        if(op == '*'):
            solution = math.prod(operands[i])
            result += solution
        else:
            solution = sum(operands[i])
            result += solution
    return result
            

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    operands, operators = parseLines(allLines)
    solution = sumSolutions(operands, operators)

print(solution)