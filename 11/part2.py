import os

def parseLines(lines):
    devices = {}
    for line in lines:
        halves = line.split(': ')
        outputs = halves[1].split(' ')
        devices[halves[0]] = outputs
    devices["out"] = []
    return devices

def getTopographicalOrder(devices):
    numInputsMap = {}
    for device, outputs in devices.items():
        if device not in numInputsMap:
            numInputsMap[device] = 0
        for output in outputs:
            if output not in numInputsMap:
                numInputsMap[output] = 0
            numInputsMap[output] += 1

    readyDevices = ["svr"]
    topoOrder = []
    while len(readyDevices) > 0:
        current = readyDevices.pop()
        outputs = devices[current]
        for output in outputs:
            numInputsMap[output] -= 1
            if numInputsMap[output] == 0:
                readyDevices.append(output)
        topoOrder.append(current)

    return topoOrder

def getNumPathsBetter(devices, start, end, topoOrder):
    numPathsMap = {}
    for device in topoOrder:
        numPathsMap[device] = 0
    numPathsMap[start] = 1
    for device in topoOrder:
        outputs = devices[device]
        for output in outputs:
            numPathsMap[output] += numPathsMap[device]
    return numPathsMap[end]

def getNumPaths(devices):
    topoOrder = getTopographicalOrder(devices)
    svrToFft = getNumPathsBetter(devices, "svr", "fft", topoOrder)
    FftToDac = getNumPathsBetter(devices, "fft", "dac", topoOrder)
    svrToDac = getNumPathsBetter(devices, "svr", "dac", topoOrder)
    dacToFft = getNumPathsBetter(devices, "dac", "fft", topoOrder)
    fftToOut = getNumPathsBetter(devices, "fft", "out", topoOrder)
    dacToOut = getNumPathsBetter(devices, "dac", "out", topoOrder)
    return (svrToFft * FftToDac * dacToOut) + (svrToDac * dacToFft * fftToOut)

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    devices = parseLines(allLines)
    solution = getNumPaths(devices)

print(solution)