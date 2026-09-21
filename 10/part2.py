import os
from sympy import Matrix, linsolve, symbols, lambdify
import itertools

def parseLines(lines):
    machines = []
    for line in lines:
        machine = parseLine(line)
        machines.append(machine)
    return machines

def parseLine(line):
    bracket = line[line.index('[') + 1 : line.index(']')]
    parens = [p.strip(' (') for p in line[line.index('(') + 1 : line.rindex(')')].split(')')]
    curlybraces = line[line.index('{') + 1 : line.index('}')].split(',')
    machine = {
        "lights": parseLights(bracket),
        "buttons": parseButtons(parens),
        "joltage": parseJoltage(curlybraces)
    }
    return machine

def parseLights(bracket):
    lights = []
    for i in range(0, len(bracket)):
        lights.append(bracket[i] == '#')
    return lights

def parseButtons(parens):
    buttons = []
    for p in parens:
        buttons.append([int(n) for n in p.split(',')])
    return buttons

def parseJoltage(curlybraces):
    return [int(j) for j in curlybraces]

def getSumOfSolutions(machines):
    totalPresses = 0
    for machine in machines:
        print("Machine: " + str(machine))
        machine_solution = getSolution(machine)
        print(machine_solution)
        totalPresses += machine_solution
    return totalPresses

def toMatrix(machine):
    counters = len(machine['joltage'])
    rows = []
    for i in range(counters):
        row = [1 if i in b else 0 for b in machine['buttons']]
        row.append(machine['joltage'][i])
        rows.append(row)
    return Matrix(rows)

def solveSystemOfEquations(m):
    vars = symbols(f'x0:{m.cols - 1}')
    return linsolve(m, *vars)

def isWholeNumber(p):
    return abs(p - round(p)) < 1e-9

def getSolution(machine):
    # one solution is to convert this into a system of linear equations and then solve it with the sympy library
    aug_matrix = toMatrix(machine)
    equations_solution = solveSystemOfEquations(aug_matrix)
    print("equations solution:" + str(equations_solution))
    free = equations_solution.free_symbols
    if(len(free) == 0):
        # found a unique solution, simply add the button presses up
        return sum(list(equations_solution)[0])
    
    # else we still have to solve for the remaining free variables, which we can just do with brute force
    expressions = list(equations_solution)[0]
    free_vars = list(free)
    best = float('inf')

    # find a per-free-variable maximum possible value which we can use to reduce the search space.
    ranges = []
    for v in free_vars:
        button_index = int(str(v)[1:])
        counters = machine['buttons'][button_index]
        ceiling = min(machine['joltage'][c] for c in counters)
        ranges.append(range(ceiling + 1))

    # for logging
    total_combinations = 1
    for r in ranges:
        total_combinations *= len(r)
    print(total_combinations)

    # converts slow rational e.subs() calls into fast floating point native python functions
    formulas = [lambdify(free_vars, e) for e in expressions]

    # main loop for brute forcing every combination of free variables within the ranges we found before
    for i, values in enumerate(itertools.product(*ranges)):
        if i % 1000 == 0:
            print(f"{i:,} / {total_combinations:,}", end='\r') # print current progress on solving this last step

        presses = [f(*values) for f in formulas]
        # lambdify gives floating point results which can read falsely as incorrect, we need to handle those without
        # thowing them out, while still throwing out fractional results like 15/2 presses which are obv. invalid
        if any(not isWholeNumber(p) for p in presses):
            continue
        presses = [round(p) for p in presses]
        if any(p < 0 for p in presses):
            continue
        total = sum(presses)
        if total < best:
            best = total

    print()
    return best

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    machines = parseLines(allLines)
    solution = getSumOfSolutions(machines)

print("SOLUTION: " + str(solution))