import os

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
        machine_solution = getSolution(machine)
        totalPresses += len(machine_solution)
    return totalPresses

def getSolution(machine):
    # get fewest number of button presses to match the lights
    # Method:  brute force all combinations of button presses, starting from 1 button press, then 2 button presses, etc.
    # return the number of button presses in the first combination that matches the lights
    numPresses = 1
    while numPresses <= len(machine["buttons"]):
        for buttonCombination in getCombinations(machine["buttons"], numPresses):
            if checkMachineSolution(buttonCombination, machine["lights"]):
                return buttonCombination
        numPresses += 1
    return -1 # should never happen

def checkMachineSolution(buttonCombination, lightsSolution):
    # see if pressing the buttons will result in the lights matching the solution
    lights = [False] * len(lightsSolution) # all lights are off by default  
    for button in buttonCombination:
        for lightIndex in button:
            lights[lightIndex] = not lights[lightIndex]
    return lights == lightsSolution

def getCombinations(buttons, numPresses):
    # returns all combinations of buttons of length numPresses.
    if numPresses == 1:
        return [[button] for button in buttons]

    combinations = []
    for i in range(0, len(buttons)):
        button = buttons[i]
        remainingButtons = buttons[i + 1:]
        subCombinations = getCombinations(remainingButtons, numPresses - 1)
        for subCombination in subCombinations:
            combinations.append([button] + subCombination)
    return combinations

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    machines = parseLines(allLines)
    solution = getSumOfSolutions(machines)

print(solution)