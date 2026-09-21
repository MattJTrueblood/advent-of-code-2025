import os

# dicts can act as FILO stacks with O(1) search complexity so here's a class that does that 
class DictStack:
    def __init__(self, items=()):
        self._d = dict.fromkeys(items)

    def push(self, item):
        self._d[item] = None

    def pop(self):
        if not self._d:
            raise IndexError("pop from empty DictStack")
        return self._d.popitem()[0]

    def peek(self):
        if not self._d:
            raise IndexError("peek from empty DictStack")
        return next(reversed(self._d))

    def __contains__(self, item): return item in self._d
    def __len__(self): return len(self._d)
    def __bool__(self): return bool(self._d)

def parseLines(lines):
    devices = {}
    for line in lines:
        halves = line.split(': ')
        outputs = halves[1].split(' ')
        devices[halves[0]] = outputs
    return devices

def getNumPathsRecursive(devices, route):
    # simple recursive DFS through the graph
    current = route.peek()
    if current == "out":
        return 1
    pathsFromCurrent = 0
    for nextDevice in devices[current]:
        if nextDevice not in route:
            route.push(nextDevice)
            pathsFromCurrent += getNumPathsRecursive(devices, route)
            route.pop()
    return pathsFromCurrent

def getNumPaths(devices):
    return getNumPathsRecursive(devices, DictStack(["svr"]))

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    devices = parseLines(allLines)
    print(devices)
    solution = getNumPaths(devices)

print(solution)